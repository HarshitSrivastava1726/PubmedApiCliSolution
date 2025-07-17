from lxml import etree
from typing import Dict, List
from medsearcher.filter import is_non_academic

def parse_pubmed_xml(xml_data: str) -> List[Dict]:
    root = etree.fromstring(xml_data.encode('utf-8'))
    papers = []

    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle")
        pub_date = article.findtext(".//PubDate/Year") or "Unknown"

        authors, companies, email = [], [], None
        for author in article.findall(".//Author"):
            last = author.findtext("LastName") or ""
            fore = author.findtext("ForeName") or ""
            aff = author.findtext(".//Affiliation") or ""
            full_name = f"{fore} {last}".strip()

            if is_non_academic(aff):
                authors.append(full_name)
                companies.append(aff)
            if "@" in aff:
                email = aff.split()[-1]

        if authors:
            papers.append({
                "PubmedID": pmid,
                "Title": title,
                "Publication Date": pub_date,
                "Non-academic Author(s)": "; ".join(authors),
                "Company Affiliation(s)": "; ".join(companies),
                "Corresponding Author Email": email or ""
            })

    return papers
