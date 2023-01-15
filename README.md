# dropbox_app

1. Register new app in Dropbox developer console - https://www.dropbox.com/developers/apps/create
2. Get the Access Token and paste it in .env file (notion: Access Token expires very fast)
3. Create venv and pip install -r requirements.txt
4. Run "uvicorn app.main:app"
5. Test GET and PUT routs on http://127.0.0.1:8000/docs
