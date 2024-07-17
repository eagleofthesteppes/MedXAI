py_file = extract_table.py

ifeq ($(OS),Windows_NT)
    interpreter = python
else
    interpreter = python3
endif

run:
    requirements extract

requirements:
    pip install -r requirements.txt

extract:
	$(interpreter) $(py_file)

