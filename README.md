<h1>An ICONic Project</h1>

<h2>Configure an virtual environment</h2>

Create an virtual environment and install pipenv
```bash
python -m venv .venv
pip install pipenv
````

Activate the virtual environment
```bash
source .venv/bin/activate # macOS or Linux
.venv\Scripts\activate # Windows
.venv\Scripts\activate.ps1 # Windows Powershell
```

Install the dependencies (this will install the dependencies from the Pipfile)
```bash
pipenv install
```

<h2>Configure access to Google Console</h2>

1. From Google Console, create a project and enable the Google Sheets API
2. Create a service account and download the json key file (rename it to `credentials.json`)
3. Share access to the email on the json to the spreadsheets you are accessing
4. Put the `credentials.json` file in the root of the project

<h2>Run the project</h2>
```bash
python main.py
# or
pipenv run python main.py
```