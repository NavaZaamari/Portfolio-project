# Portfolio Project

A personal portfolio web application, containerized with Docker for easy setup and deployment.

## 🧰 Tech Stack

- **Frontend:** HTML, SCSS, CSS, JavaScript
- **Backend:** Python
- **Containerization:** Docker & Docker Compose

## 📁 Project Structure

```
Portfolio-project/
├── core/                 # Core application code
├── dockerfile            # Docker image definition
├── docker-compose.yml    # Multi-container orchestration
├── requirements.txt      # Python dependencies
├── .gitattributes
├── .gitignore
├── LICENSE
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started/) and Docker Compose installed
- (Optional, for local non-Docker setup) Python 3.x

### Run with Docker (recommended)

```bash
# Clone the repository
git clone https://github.com/NavaZaamari/Portfolio-project.git
cd Portfolio-project

# Build and start the containers
docker-compose up --build
```

Once the containers are running, open your browser and navigate to the configured local address (e.g. `http://localhost:PORT`) to view the site.

To stop the application:

```bash
docker-compose down
```

### Run Locally (without Docker)

```bash
git clone https://github.com/NavaZaamari/Portfolio-project.git
cd Portfolio-project

# Install Python dependencies
pip install -r requirements.txt

# Run the application
python core/app.py
```

> Adjust the run command above to match the actual entry point inside `core/`.

## ⚙️ Configuration

If the project requires environment variables (e.g. database credentials, API keys, ports), document them here, for example:

```env
PORT=5000
DEBUG=True
```

## 🗺️ Features

- Responsive portfolio layout
- Sections for projects, skills, and contact information
- Dockerized for consistent, reproducible deployment

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add some feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 👤 Author

**NavaZaamari**
GitHub: [@NavaZaamari](https://github.com/NavaZaamari)
