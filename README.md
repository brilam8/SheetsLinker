# SheetsLinker

Welcome to SheetsLinker! A tool that links a Tkinter GUI with a Google Sheets page, allowing you to fill in each row one by one.
Built to allow me to easily keep track of internships that I apply to.

## Getting Started
1. Clone this repo to your local machine.
2. Run `pip install -r requirements.txt`
3. Go to [Google Cloud Platform](https://console.cloud.google.com/) and create a project.
4. Enable Google Drive and Google Sheets API for that project.
5. Create a service account and move your `client_secret.json` file in the config folder.
6. Add the service account as an editor on your Sheets page.
7. Run `pyinstaller --onefile --hidden-import babel.numbers main.py` to generate an executable. (and copy your config folder over to the `dist` folder)
8. Open the app in the `dist` folder, it should now be linked to your Google Sheets!

## Features
* Automatically keeps track of the current row that you're at after each session.
* Auto-completion for positions that are most commonly used.
* Automatically fills in your Google Sheets based on what you input.