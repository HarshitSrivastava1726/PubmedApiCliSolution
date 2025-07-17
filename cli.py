import typer
from medsearcher.api import fetch_pubmed_ids, fetch_pubmed_details
from medsearcher.parser import parse_pubmed_xml
from medsearcher.exporter import export_to_csv
from rich.console import Console

app = typer.Typer()
console = Console()

@app.command()
def get_papers_list(query: str, file: str = typer.Option(None, "--file", "-f"), debug: bool = typer.Option(False, "--debug", "-d")):
    if debug:
        console.log(f"Searching PubMed for query: {query}")
    ids = fetch_pubmed_ids(query)
    if debug:
        console.log(f"Found {len(ids)} papers")
    xml_data = fetch_pubmed_details(ids)
    papers = parse_pubmed_xml(xml_data)
    export_to_csv(papers, file)

if __name__ == "__main__":
    app()
