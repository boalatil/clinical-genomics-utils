import requests
import re

from scripts.gene_symbols.validate_hgnc_symbols import (
    merge_gene_lists,
    validate_gene_list
)

def main():
  print(r"""
  ____              _       _   _ _ 
 | __ )  ___   __ _| | __ _| |_(_) |
 |  _ \ / _ \ / _` | |/ _` | __| | |
 | |_) | (_) | (_| | | (_| | |_| | |
 |____/ \___/ \__,_|_|\__,_|\__|_|_|
 """)
  print("="*37)
  print("HGNC GENE LIST MERGER AND VALIDATOR")
  print("(C) 2026 Laura Giron")
  print("https://github.com/boalatil/")
  print("="*37)
  print()
  try:
    num_lists= int(input("How many gene lists do you want to merge? "))
  except ValueError:
    print("Please enter a valid integer number.")
    return

  gene_lists= []

  for i in range(num_lists):
      genes = input(f"Please enter gene list #{i+1}: ")
      gene_lists.append(genes)

#* "unpacks" the list
  merged_genes = merge_gene_lists(*gene_lists)
  totalnumber=sum(len([g for g in re.split(r'[,;\s]+', gl.strip()) if g]) for gl in gene_lists)
  print(f"\nTotal number of gene entries provided (including duplicates): {totalnumber}.")
  print(f"\nAfter eliminating duplicates, your total number of UNIQUE gene symbols is: {len(merged_genes)}.\n\nNow proceeding with validation of the gene names in HGNC database. \nThis may take a few minutes to complete, depending on the number\nof genes on your lists.")
  approved_genes, renamed_genes, not_found_genes = validate_gene_list(merged_genes)
  print("\nYour new list of ", len(approved_genes), "genes is:")
  print("\n#########################################################################")
  print(", ".join(approved_genes))
  print("\n#########################################################################")
  if renamed_genes:
    print("\n\nIMPORTANT: The following gene symbols were updated according to HGNC:")
    for old, new in renamed_genes:
          print(f"{old} -> {new}")

  nogenes=", ".join(not_found_genes)
  if not_found_genes:
      print(f"\n\nIMPORTANT: The following gene symbols were not found in the HGNC\ndatabase or are invalid: {nogenes}")

if __name__ == "__main__":
    main()
