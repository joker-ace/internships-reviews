.PHONY: create-core-environment create-python-environment install-python-packages
.SILENT: create-core-environment create-python-environment install-python-packages

VERSION=2.7
ENV=env
PIP=$(ENV)/bin/pip
PYTHON=$(ENV)/bin/python$(VERSION)

install-postgresql:
	apt-get install postgresql;
	apt-get install postgresql-contrib;

create-core-environment: create-python-environment install-python-packages

create-python-environment:
	if [ -d $(ENV) ]; then  \
	    chmod +w -R $(ENV); \
	    rm -fr $(ENV);      \
	fi; \
	PYTHON_EXE=/usr/local/bin/python$(VERSION); \
	if [ ! -x $$PYTHON_EXE ]; then \
		PYTHON_EXE=/usr/bin/python$(VERSION); \
	fi;\
	virtualenv --python=$$PYTHON_EXE $(ENV);

install-python-packages:
	$(PIP) install --requirement requirements.txt;