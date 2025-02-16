# HR Agent - SellScale Helix

An AI-powered HR assistant that helps HR professionals craft effective recruiting strategies and outreach messages.

## Features

- AI-powered chat interface for recruitment assistance
- Real-time message sequence crafting
- Automated sequence suggestions
- Professional outreach templates
- Conversation history tracking
- Real-time chat updates via WebSocket

## Tech Stack

### Frontend
- React 19.0.0
- TypeScript
- Socket.IO Client
- Axios for API communication
- CSS for styling

### Backend
- Flask
- Flask-CORS
- Flask-SQLAlchemy
- OpenAI GPT-4 integration
- PostgreSQL
- Python-dotenv

## Prerequisites

- Node.js (v16 or higher)
- Python 3.8+
- PostgreSQL
- OpenAI API key

## Getting Started

### Backend Setup

1. Navigate to the backend directory:

```bash
cd backend
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file with the following variables:

```bash
SECRET_KEY=your_secret_key
OPENAI_API_KEY=your_openai_api_key
DATABASE_URL=postgresql://user:password@localhost/helix
```

4. Initialize the database:

```bash
python database/db_init.py
```

5. Run the Flask application:

```bash
flask run
```

### Frontend Setup

1. Navigate to the frontend directory:

```bash
cd frontend
```

2. Install dependencies:

```bash
npm install
```

3. Create a `.env` file:

```bash
REACT_APP_API_BASE_URL=http://localhost:5000
```

4. Run the React application:

```bash
npm start
```

The application will be available at `http://localhost:3000`.

## Project Structure

### Frontend

The frontend directory structure is organized as follows:

- `frontend/`
  - `src/`
    - `components/` - Contains all React components
    - `services/` - Houses API and Socket service implementations
    - `config/` - Configuration files and settings
    - `types/` - TypeScript type definitions and interfaces
    - `App.tsx` - Main application component

### Backend 

The backend directory is structured as:

- `backend/`
  - `routes/` - API route handlers and endpoints
  - `services/` - Business logic and core functionality
  - `database/` - Database models and initialization scripts
  - `app.py` - Main application entry point

## API Endpoints

- `POST /chat` - Send messages to the AI assistant
- `GET /sequence` - Retrieve saved sequences
- `POST /sequence` - Save new sequences

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Security

- Never commit `.env` files containing sensitive information
- Add the following to your `.gitignore`:
```bash
# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local
```