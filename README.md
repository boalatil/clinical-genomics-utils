```
  ____              _       _   _ _ 
 | __ )  ___   __ _| | __ _| |_(_) |
 |  _ \ / _ \ / _` | |/ _` | __| | |
 | |_) | (_) | (_| | | (_| | |_| | |
 |____/ \___/ \__,_|_|\__,_|\__|_|_|
```

# Clinical Genomics Utils
This repository contains small, self-contained scripts and notebooks for educational and practical tasks in clinical genomics data analysis, with a focus on **gene symbol handling**, **HGNC validation**, and **reproducible exploratory workflows**.

## Repository structure

```text
clinical-genomics-utils/
├── scripts/
│   └── __init__.py
│   └── gene_symbols/
│       └── validate_hgnc_symbols.py
|       └── gene_lists.py
|       └── __init__.py
├── README.md
└── LICENSE

```
```
scripts/
```
Reusable Python code that implements core logic.
Core functions are implemented in:

`scripts/gene_symbols/validate_hgnc_symbols.py`

## HGNC validation

Gene symbol validation is performed using the official HGNC REST API (HUGO Gene Nomenclature Committee).
The workflow: Merge gene lists while removing duplicates, Check whether each symbol is an approved HGNC symbol, If not approved, search for: previous (deprecated) symbols, known aliases. Report: approved symbols,
renamed symbols, symbols not found in HGNC.

An active internet connection is required for validation.

## Requirements

Python ≥ 3.8
Jupyter Notebook or JupyterLab
requests
nbformat (for notebook validation)

## Usage
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

### License

This project is licensed under the MIT License.

### Disclaimer

This repository focuses on gene symbol handling, not variant interpretation.
HGNC results depend on the current state of the HGNC database.
The code is intended for educational and research purposes, not for direct clinical decision-making or diagnostic use.
