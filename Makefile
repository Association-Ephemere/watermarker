FILES = $(shell find tests -name "*.py")

install:
	pip install -r requirements/requirements.txt

save_dependencies:
	pipreqs src --savepath requirements/app.txt
	pipreqs tests --savepath requirements/tests.txt

run: install
	python src/main.py

test: install 
	@pytest 


.PHONY: install save_dependencies run