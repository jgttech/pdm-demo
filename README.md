# pdm-demo

This is a PDM (Python Dependency Manager) based solution that does NOT use Python virtual environments to install, develop, and deploy a single binary executable Python API service.

This is a basic example of how we could build a Python API without virtual environments that can be built into a single executable that can be embedded in whatever we want (like a Docker container, for example) and delivered to a client as a deliverable.

---

## Technologies

- [PDM](https://pdm-project.org/latest/)
- [Fast API](https://fastapi.tiangolo.com/)
- [PyInstaller](https://pyinstaller.org/en/stable/)

---

## Required Before Starting

- [PDM](https://pdm-project.org/latest/)
- Python 3.11 or greater

---

## Quick Start

| Order | Command | Description |
|:------|:--------|:------------|
| 1 | `pdm install`   | Installs all your dependencies.               |
| 2 | `pdm start`     | Starts the development server.                |

---

## Build/Preview Commands

| Command | Description |
|:--------|:------------|
| `pdm run build` | Builds the single-execution binary.           |
| `pdm preview`   | Starts a Docker Container running the binary. |

---

## API Documentation Links

1. [Redoc](http://127.0.0.1:8000/redoc)
   1. http://127.0.0.1:8000/redoc
2. [Swagger](http://127.0.0.1:8000/docs)
   1. http://127.0.0.1:8000/docs

---
