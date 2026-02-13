"""
HGNC gene symbol validation utilities.

This module provides helper functions to validate and normalize
human gene symbols using the HGNC REST API.

Source:
- https://www.genenames.org/
"""
import requests
# =========================
# Configuration / constants
# =========================
HGNC_FETCH_SYMBOL_ENDPOINT = "https://rest.genenames.org/fetch/symbol/"
HGNC_SEARCH_ENDPOINT = "https://rest.genenames.org/search/"
DEFAULT_TIMEOUT = 10


# =========================
# Public functions
# =========================
def merge_gene_lists(list_a: str, list_b: str, delimiter=", ") -> list[str]:
    """
    Merge two gene lists, remove duplicates, and sort alphabetically.
    """
    genes_a = {g.strip() for g in list_a.split(delimiter)}
    genes_b = {g.strip() for g in list_b.split(delimiter)}
    return sorted(genes_a.union(genes_b))


def resolve_hgnc_symbol(symbol: str) -> dict:
    """
    Resolve a human gene symbol using HGNC.

    Returns a dictionary with:
    - status: approved | previous | alias | not_found | error
    - approved_symbol: current HGNC symbol or None
    """
    headers = {"Accept": "application/json"}

    # 1) Strict check: approved symbol
    fetch_response = requests.get(
        HGNC_FETCH_SYMBOL_ENDPOINT + symbol,
        headers=headers,
        timeout=DEFAULT_TIMEOUT
    )

    if fetch_response.status_code == 200:
        data = fetch_response.json()
        if data["response"]["numFound"] > 0:
            return {"status": "approved", "approved_symbol": symbol}

    # 2) Fallback: previous symbols or aliases
    search_response = requests.get(
        HGNC_SEARCH_ENDPOINT + symbol,
        headers=headers,
        timeout=DEFAULT_TIMEOUT
    )

    if search_response.status_code != 200:
        return {"status": "error", "approved_symbol": None}

    docs = search_response.json()["response"]["docs"]

    for doc in docs:
        if symbol in doc.get("prev_symbol", []):
            return {"status": "previous", "approved_symbol": doc["symbol"]}
        if symbol in doc.get("alias_symbol", []):
            return {"status": "alias", "approved_symbol": doc["symbol"]}

    return {"status": "not_found", "approved_symbol": None}


# =========================
# Module test (optional)
# =========================
if __name__ == "__main__":
    # Minimal sanity check, not a demo
    print(resolve_hgnc_symbol("TP53"))
