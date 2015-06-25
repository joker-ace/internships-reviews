.PHONY: install create-environment install-packages 
.SILENT: install create-environment install-packages 

VERSION=2.7
ENV=env
PIP=$(ENV)/bin/pip
PYTHON=$(ENV)/bin/python$(VERSION)

install: create-environment install-packages

create-environment:
	if [ -d $(ENV) ]; then  \
	    chmod +w -R $(ENV); \
	    rm -fr $(ENV);      \
	fi; \
	PYTHON_EXE=/usr/local/bin/python$(VERSION); \
	if [ ! -x $$PYTHON_EXE ]; then \
		PYTHON_EXE=/usr/bin/python$(VERSION); \
	fi;\
	virtualenv --python=$$PYTHON_EXE $(ENV);

install-packages:
	$(PIP) install --requirement requirements.txt;
