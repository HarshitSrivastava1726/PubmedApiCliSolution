# Pubmed Api  and CliSolution
✅ Features
Fetch research papers from PubMed by query

Filter authors affiliated with non-academic institutions

Export results to CSV

CLI with options for:

Debug logs

Output file saving

📂 Project Structure
python
Copy
Edit
medsearcher/
│
├── medsearcher/             # Main package
│   ├── __init__.py
│   ├── api.py               # PubMed API calls
│   ├── parser.py            # XML parsing logic
│   ├── filter.py            # Affiliation filtering
│   ├── exporter.py          # CSV export logic
│   └── cli.py               # CLI entry point
│
├── tests/                   # Unit tests (optional)
│   └── test_api.py
│
├── pyproject.toml           # Poetry config
└── README.md
🔧 Setup
1. Install Poetry
bash
Copy
Edit
pip install poetry
2. Install Project Dependencies
bash
Copy
Edit
poetry install
▶ Usage
Run CLI command with Poetry:

bash
Copy
Edit
poetry run get-papers-list "covid vaccine" -f results.csv --debug
Options:

query → Search term for PubMed

-f → Output CSV file (optional)

--debug → Enable debug logs

✅ Example Output
text
Copy
Edit
PubmedID | Title | Publication Date | Non-academic Author(s) | Company Affiliation(s) | Corresponding Author Email
12345    | Sample Research | 2023 | John Doe | ABC Pharma | john@abcpharma.com
✅ Tech Stack
Python 3.9+

Typer (CLI)

Pandas (Data handling)

Requests (API)

Rich (Pretty logs)

Poetry (Dependency management)

