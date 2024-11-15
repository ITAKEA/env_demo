# Simple Hello World Microservice

A simple Flask microservice that serves a "Hello World" message from a SQLite database with environment variable configuration.

## Components

- `app.py`: Main Flask application with SQLite integration
- `requirements.txt`: Python dependencies
- `Dockerfile`: Container configuration using gunicorn
- `.env`: Environment variables configuration
- `.dockerignore`: Files to exclude from Docker build
- `.gitignore`: Files to exclude from git

## Dependencies

- Flask: Web framework
- Gunicorn: Production WSGI server
- Python-dotenv: Environment variable management
- SQLite3: Database (built into Python)

## Docker Setup

### Building the Image
To build the Docker image, run the following command in the project directory:
```bash
docker build -t hello-world-service .
```

### Running the Container
To run the container with default environment variables:
```bash
docker run -d -p 8080:80 hello-world-service
```

To run with custom environment variables:
```bash
docker run -d -p 8080:80 \
  -e GREETING_TYPE=production \
  -e DB_PATH=/home/database.db \
  -e SERVICE_URL=http://myservice.com \
  -v $(pwd):/home \
  hello-world-service
```

Note: The volume mount (-v) is needed if you want to persist the SQLite database file outside the container.

The service will be available at http://localhost:8080

## Environment Variables
| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `GREETING_TYPE` | No | default | Type of greeting to return in response |
| `DB_PATH` | No | greetings.db | Path to SQLite database file |
| `SERVICE_URL` | No | http://example.com | URL of the service |

## API Endpoint

### GET /

Returns a JSON response with:
- `message`: Hello World message from the database
- `greeting_type`: Value from GREETING_TYPE environment variable
- `service_url`: Value from SERVICE_URL environment variable

Example response:
```json
{
    "message": "Hello, World!",
    "greeting_type": "development",
    "service_url": "http://localhost:8080"
}
```

## Database

The application uses SQLite with a simple structure:
- Table: `greetings`
- Column: `message` (TEXT)

The database and table are created automatically on first request if they don't exist.
