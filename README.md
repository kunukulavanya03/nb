# nb

Backend API for nb

## Tech Stack

- **Frontend**: React
- **Backend**: FastAPI + SQLAlchemy
- **Frontend Source**: GitHub ([Repository](https://github.com/HimaShankarReddyEguturi/Hotelbookinguidesign))

## Project Structure

```
nb/
├── frontend/          # Frontend application
├── backend/           # Backend API
├── README.md          # This file
└── docker-compose.yml # Docker configuration (if applicable)
```

## Getting Started

### Prerequisites

- Node.js 18+ (for frontend)
- Python 3.11+ (for Python backends)
- Docker (optional, for containerized setup)

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Backend Setup

```bash
cd backend
# Follow backend-specific setup instructions in backend/README.md
```

## Features

- User registration and authentication
- Note creation, editing, and deletion
- Note list retrieval

## API Endpoints

- `POST /api/register` - Registers a new user.
- `POST /api/login` - Logs a user into the application.
- `POST /api/password-reset` - Resets a user's password.
- `GET /api/notes` - Retrieves a list of all notes for the current user.
- `POST /api/notes` - Creates a new note for the current user.
- `PUT /api/notes/{note_id}` - Edits an existing note for the current user.
- `DELETE /api/notes/{note_id}` - Deletes a note for the current user.

## License

MIT
