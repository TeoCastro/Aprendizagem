#!/bin/sh
set -e

# Start virtual framebuffer (1280x720, 24-bit color)
Xvfb :1 -screen 0 1280x720x24 &
sleep 1

# Start window manager
DISPLAY=:1 fluxbox &
sleep 1

# Start VNC server (no password, listens on port 5901)
x11vnc -display :1 -forever -nopw -quiet -rfbport 5901 &
sleep 1

# Start noVNC web client on port 3000, proxying to VNC on 5901
websockify --web /usr/share/novnc/ 3000 localhost:5901 &

# Run the Tkinter app from the Treinamento directory
# (so relative paths to Logo.jpg and Banco_Clientes.db resolve correctly)
cd /app/Treinamento
DISPLAY=:1 exec python3 Treinando.py
