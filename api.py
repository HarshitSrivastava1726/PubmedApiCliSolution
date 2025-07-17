import requests
from typing import List

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def fetch_pubmed_ids(query: str, retmax: int = 50) -> List[str]:
    """Search PubMed and return list of IDs."""
    url = f"{BASE_URL}esearch.fcgi"
    params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": retmax}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json().get("esearchresult", {}).get("idlist", [])

def fetch_pubmed_details(ids: List[str]) -> str:
    """Fetch paper details as XML."""
    url = f"{BASE_URL}efetch.fcgi"
    params = {"db": "pubmed", "id": ",".join(ids), "retmode": "xml"}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text
