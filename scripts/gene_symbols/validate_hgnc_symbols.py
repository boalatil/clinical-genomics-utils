"""
HGNC gene symbol validation utilities.

This module provides helper functions to validate and normalize
human gene symbols using the HGNC REST API.

Source:
- https://www.genenames.org/
"""
import requests
import sys
import re
HGNC_FETCH_SYMBOL_ENDPOINT = "https://rest.genenames.org/fetch/symbol/"
HGNC_SEARCH_ENDPOINT = "https://rest.genenames.org/search/"

####FUNCTIONS

def merge_gene_lists(*gene_lists):
    def clean_gene(gen):
        gen = gen.strip()
        gen = gen.strip('.,;:!?_()[]{}"\'/\\')
        return gen.upper()
    all_genes=set()
    for gene_list in gene_lists:
      genes = set(cleaned for gen in re.split(r'[,;\s]+', gene_list) if (cleaned := clean_gene(gen)))
      all_genes.update(genes)

    return sorted(all_genes)

def validate_gene_list(gene_symbols):
    approved_genes = []
    renamed_genes = []
    not_found_genes = []

    headers = {"Accept": "application/json"}

    for original_symbol in gene_symbols:
        if not original_symbol or not original_symbol.strip():
            continue

        symbol = original_symbol.strip().upper().replace(" ", "")

        fetch_url = HGNC_FETCH_SYMBOL_ENDPOINT + symbol

        try:
            fetch_response = requests.get(fetch_url, headers=headers, timeout=10)

            if fetch_response.status_code == 200:
                fetch_data = fetch_response.json()
                num_encontrados = fetch_data["response"]["numFound"]

                if num_encontrados > 0:
                    approved_genes.append(symbol)
                    continue
        except:
            pass

        search_url = HGNC_SEARCH_ENDPOINT + symbol

        try:
            search_response = requests.get(search_url, headers=headers, timeout=10)

            if search_response.status_code != 200:
                not_found_genes.append(original_symbol.strip())
                continue

            search_data = search_response.json()
            docs = search_data["response"]["docs"]

            if not docs:
                not_found_genes.append(original_symbol.strip())
                continue

            gene_found = False
            current_symbol = docs[0].get("symbol")

            if current_symbol:
                detail_url = HGNC_FETCH_SYMBOL_ENDPOINT + current_symbol

                try:
                    detail_response = requests.get(detail_url, headers=headers, timeout=10)

                    if detail_response.status_code == 200:
                        detail_data = detail_response.json()
                        detail_docs = detail_data["response"]["docs"]

                        if detail_docs:
                            detail_doc = detail_docs[0]

                            prev_symbols = detail_doc.get("prev_symbol", [])
                            if symbol in prev_symbols:
                                approved_genes.append(current_symbol)
                                renamed_genes.append([original_symbol.strip(), current_symbol])
                                gene_found = True

                            if not gene_found:
                                alias_symbols = detail_doc.get("alias_symbol", [])
                                if symbol in alias_symbols:
                                    approved_genes.append(current_symbol)
                                    renamed_genes.append([original_symbol.strip(), current_symbol])
                                    gene_found = True

                except:
                    pass

            if not gene_found:
                not_found_genes.append(original_symbol.strip())

        except:
            not_found_genes.append(original_symbol.strip())

    return approved_genes, renamed_genes, not_found_genes
