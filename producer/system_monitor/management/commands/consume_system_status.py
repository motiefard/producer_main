import json
import time
from kafka import KafkaConsumer
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime
from system_monitor.models import SystemStatus

KAFKA_TOPIC = 'system-status'
KAFKA_BROKER = 'localhost:9092'
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds


class Command(BaseCommand):
    help = 'consume system-status messages from Kafka'

    def handle(self, *args, **options):
        consumer = KafkaConsumer(
            KAFKA_TOPIC,
            bootstrap_servers=KAFKA_BROKER,
            value_deserializer=lambda v: json.loads(v.decode('utf-8')),
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='system-status-consumers',
        )

        self.stdout.write(self.style.SUCCESS('Kafka consumer started...'))

        try:
            for message in consumer:
                self.process_message_with_retry(message.value)
        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING('\nStopping consumer...'))
        finally:
            consumer.close()
            self.stdout.write(self.style.SUCCESS('Kafka consumer closed.'))


    def process_message_with_retry(self, data):
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                self.process_message(data)
                return
            except Exception as e:
                print(
                    f"Error processing message (attempt {attempt}): {data}"
                )
                if attempt < MAX_RETRIES:
                    time.sleep(RETRY_DELAY)
                else:
                    print("Message failed after max retries")

    
    def process_message(self, data):
        """
        parse json and save to db
        """
        SystemStatus.objects.create(
            timestamp=parse_datetime(data['timestamp']),
            ram_total=data['ram']['total'],
            ram_used=data['ram']['used'],
            ram_free=data['ram']['free'],
            cpu_percent=data['cpu']['percent'],
            disk_total=data['disk']['total'],
            disk_used=data['disk']['used'],
            disk_free=data['disk']['free'],
            raw_data=data, 
        )
        self.stdout.write(self.style.SUCCESS(f"saved"))
