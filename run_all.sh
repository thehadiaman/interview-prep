gnome-terminal --tab -- bash -c "cd backend;python3 -m venv .venv;source .venv/bin/activate;pip install -r requirements.txt;python3 server.py";
gnome-terminal --tab -- bash -c "cd fe && python3 -m http.server 3000;";
