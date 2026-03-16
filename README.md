## mass-delete
A command line tool to mass delete emails with a keyword, from a sender or both.

Arguments -
- `--sender` - delete all emails from this sender
- `--keyword` - delete all emails containing this keyword (case insensitive), pass in quotes for a pattern with more than one word
- when `--sender` and `--keyword` used together - delete all emails from this sender containing the provided keyword

This was a personal project that I built for deleting repetitive emails in my college email ID.


## Steps to use it for yourself

### 1. Clone the repo
```bash
git clone https://github.com/srishtea-22/mass-delete.git
cd mass-delete
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up a Google Cloud Project
1. Create a [Google Cloud Project](https://developers.google.com/workspace/guides/create-project)
2. Navigate to **APIs & Services > Library** and enable the **Gmail API**

### 4. [Configure the OAuth consent screen](https://developers.google.com/workspace/gmail/api/quickstart/python#configure_the_oauth_consent_screen)

### 5. [Authorize credentials for a desktop application](https://developers.google.com/workspace/gmail/api/quickstart/python#authorize_credentials_for_a_desktop_application)

### 6. Save the downloaded JSON file as `credentials.json`, and move the file to the root of the directory.

### 7. Run the script

```bash
# First run will open a browser window asking you to authorize the app

# Delete all emails from a specific sender
python mass-delete.py --sender "example@gmail.com"

# Delete all emails containing a keyword
python mass-delete.py --keyword "newsletter"

# Delete all emails from a sender containing a keyword
python mass-delete.py --sender "example@gmail.com" --keyword "newsletter"
```