# Base44 Dev Environment

## Project Overview
Python learning project ("Aprendizagem") containing Tkinter desktop GUI applications for clinic/client management with SQLite databases. All text is in Portuguese.

## Architecture
- **Language**: Python 3 (Tkinter desktop GUI — not a web app)
- **Database**: SQLite (`Banco_Clientes.db`)
- **GUI Framework**: Tkinter (creates desktop windows)
- **Browser Preview**: Xvfb virtual framebuffer + x11vnc + noVNC/websockify streams the desktop to port 3000

## Running the App
```bash
docker compose -f docker-compose.base44.yml up -d --build
```
The Tkinter GUI is streamed to the browser via noVNC on port 3000. The VNC server runs without a password and noVNC auto-connects.

## Main Application
- `Treinamento/Treinando.py` — Full client management app with login (password: "sua"), CRUD operations, and logo image. This is the app that runs in the preview.
- `Tkinter/Segunda.py` — Client registration GUI with SQLite (class-based)
- `Tkinter/Primeiro.py` — Simpler procedural version of the client management GUI
- `Tkinter/PrimeiroPandas.py` — Pandas + Tkinter demo (has hardcoded Windows Excel path, won't work without the file)

## Notes
- The hardcoded Windows image path in `Treinamento/Treinando.py` was fixed to use a relative path (`Logo.jpg`) so the app runs on Linux.
- The app runs from the `Treinamento/` directory so relative paths to `Logo.jpg` and `Banco_Clientes.db` resolve correctly.
- The login password for `Treinando.py` is "sua".
- noVNC serves on port 3000 and auto-connects to the VNC server.
