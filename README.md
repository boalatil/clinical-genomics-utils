## Clinical Genomics Utils
This repository contains small, self-contained scripts and notebooks for educational and practical tasks in clinical genomics data analysis, with a focus on **gene symbol handling**, **HGNC validation**, and **reproducible exploratory workflows**.

## Repository structure

```text
clinical-genomics-utils/
├── scripts/
│   └── gene_symbols/
│       └── validate_hgnc_symbols.py
│
├── notebooks/
│   └── gene_lists/
│       └── a_gene_list_hgnc.ipynb
│
├── README.md
└── LICENSE

```
```
scripts/
```
Reusable Python code that implements core logic. Scripts are not notebook-specific and are meant to be imported by notebooks or other tools.
```
scripts/gene_symbols/validate_hgnc_symbols.py
```
merge gene lists, validate human gene symbols using the official HGNC REST API, detect deprecated symbols and aliases.
```
notebooks/
```
Jupyter notebooks intended for explanation, reproducible examples, exploratory and educational use.
```
notebooks/gene_lists/a_gene_list_hgnc.ipynb
```
Demonstrates how to merge gene lists and validate symbols by importing functions from the scripts/ module.

# HGNC validation

Gene symbol validation is performed using the official HGNC REST API (HUGO Gene Nomenclature Committee).
The workflow: Merge gene lists while removing duplicates, Check whether each symbol is an approved HGNC symbol, If not approved, search for: previous (deprecated) symbols, known aliases. Report: approved symbols,
renamed symbols, symbols not found in HGNC.

An active internet connection is required for validation.

# Requirements

Python ≥ 3.8
Jupyter Notebook or JupyterLab
requests
nbformat (for notebook validation)

# Usage
Clone the repository:
```bash
git clone https://github.com/boalatil/clinical-genomics-utils.git
cd clinical-genomics-utils
```
Open the notebook:
```
jupyter notebook notebooks/gene_lists/a_gene_list_hgnc.ipynb
```
The notebook imports functionality directly from the scripts/ directory; no code duplication is required.

## License

This project is licensed under the MIT License.

## Disclaimer

This repository focuses on gene symbol handling, not variant interpretation.
HGNC results depend on the current state of the HGNC database.
The code is intended for educational and research purposes, not for direct clinical decision-making or diagnostic use.
