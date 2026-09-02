.PHONY: check manifest tree
check:
	python scripts/00_setup/repo_check.py
manifest:
	python scripts/00_setup/refresh_manifest.py
tree:
	python scripts/00_setup/build_tree.py
