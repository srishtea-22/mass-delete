## mass-delete

A command line tool to mass delete emails with a keyword, from a sender or both.

Arguments - 
- --sender - delete all emails from this sender
- --keyword - delete all emails containing this keyword (case insensitive), pass in quotes for a pattern with more than one word
- when --sender and --keyword used together - delete all emails from this sender containing the provided keyword

Usage -
```bash
# Delete all emails from a specific sender
python mass-delete.py --sender "example@gmail.com"

# Delete all emails containing a keyword
python mass-delete.py --keyword "newsletter"

# Delete all emails from a sender containing a keyword
python mass-delete.py --sender "example@gmail.com" --keyword "newsletter"
```