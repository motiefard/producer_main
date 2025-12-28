# Producer Main

A Django-based project for system status monitoring with Kafka integration.

## Prerequisites

- Python 3.x
- pip
- Docker and Docker Compose
- Git

## Installation

### 1. Clone the Repository

```bash
git clone git@github.com:motiefard/producer_main.git
cd producer_main
```

### 2. Activate Virtual Environment

```bash
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Navigate to Producer Directory

```bash
cd producer/
```

### 5. Start Docker Containers

Run the containers from `docker-compose.yml`:

```bash
sudo docker-compose up -d
```

## Running the Application

### Start the Django Development Server

```bash
./manage.py runserver
```

Once the server is running, you can access:

- **API Root**: http://127.0.0.1:8000/api/
- **API Documentation**: http://127.0.0.1:8000/api/docs/

## Running Components

### System Status Producer

To run the producer and send messages to Kafka:

```bash
python3 system_status_producer.py
```

### Kafka Consumer

To run the Kafka consumer:

```bash
python3 manage.py consume_system_status
```

## Project Structure

```
producer_main/
├── producer/
│   ├── manage.py
│   ├── docker-compose.yml
│   ├── requirements.txt
│   ├── system_status_producer.py
│   └── system_monitor/
│       └── management/
│           └── commands/
│               └── consume_system_status.py
└── venv/
```

## Notes

- Make sure Docker containers are running before starting the producer or consumer
- The virtual environment should be activated before running any Python commands
- Ensure all dependencies are installed from `requirements.txt` before running the application

