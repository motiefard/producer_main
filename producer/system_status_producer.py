import psutil
import json
import time
from datetime import datetime
from kafka import KafkaProducer


class SystemStatsProducer:
    topic = 'system-status'
    
    def __init__(self):
        """Initialize Kafka producer with JSON serialization"""
        self.kafka_producer = KafkaProducer(
            bootstrap_servers='localhost:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        print(f"Kafka producer initialized. Connecting to localhost:9092")

    def get_system_stats(self):
        """Collect system statistics (RAM, CPU, Disk)"""
        memory = psutil.virtual_memory()
        ram_info = {
            'total': memory.total,
            'used': memory.used,
            'free': memory.free,
            'percent': memory.percent
        }
        
        cpu_info = {
            'percent': psutil.cpu_percent(interval=1),
        }
        
        disk = psutil.disk_usage('/')
        disk_info = {
            'total': disk.total,
            'used': disk.used,
            'free': disk.free,
        }
        
        data = {
            'timestamp': datetime.now().isoformat(),
            'ram': ram_info,
            'cpu': cpu_info,
            'disk': disk_info
        }
        return data

    def send_message(self, message):
        """Send message to Kafka topic"""
        try:
            # Send message to topic
            send_msg = self.kafka_producer.send(self.topic, message)
            print(f"message sent successfully to system_status topic")
            return True
        except Exception as e:
            print(f"error sending message to system_status topic: {e}")
            return False

    def close(self):
        """Close Kafka connection"""
        self.kafka_producer.close()
        print('Kafka producer is closed')


def runner():
    """sending every 10 seconds"""
    producer = SystemStatsProducer()
    
    try:
        print("Starting system stats producer...")
        print("Press Ctrl+C to stop")
        while True:
            data = producer.get_system_stats()
            
            # Send to Kafka
            success_sent = producer.send_message(data)
            
            if success_sent:
                print(f"Sent: {data['timestamp']} - CPU: {data['cpu']['percent']}%, "
                      f"RAM: {data['ram']['percent']}%, Disk: {data['disk']['used']:.1f}%")
            
            # Wait 10 seconds before next-send
            time.sleep(10)
            
    except KeyboardInterrupt:
        print("\nStopping producer...")
    finally:
        producer.close()


if __name__ == "__main__":
    runner()