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

## Environment Variables
| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `GREETING_TYPE` | No | default | Type of greeting to return in response |
| `DB_PATH` | No | greetings.db | Path to SQLite database file |

## API Endpoint

### GET /

Returns a JSON response with:
- `message`: Hello World message from the database
- `greeting_type`: Value from GREETING_TYPE environment variable

Example response:
```json
{
    "message": "Hello, World!",
    "greeting_type": "development"
}
```

## Database

The application uses SQLite with a simple structure:
- Table: `greetings`
- Column: `message` (TEXT)

The database and table are created automatically on first request if they don't exist.
