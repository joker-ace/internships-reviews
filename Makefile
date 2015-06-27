.PHONY: create-core-environment create-python-environment install-python-packages create_project_dirs_and_files
.SILENT: create-core-environment create-python-environment install-python-packages create_project_dirs_and_files

VERSION=2.7
ENV=env
PIP=$(ENV)/bin/pip
PYTHON=$(ENV)/bin/python$(VERSION)

install-postgresql:
	apt-get install postgresql;
	apt-get install postgresql-contrib;

create-core-environment: create-python-environment create_project_dirs_and_files install-python-packages

create_project_dirs_and_files:
	mkdir -p logs;
	mkdir -p run;
	mkdir -p media_content;
	touch logs/gunicorn_supervisor.log;
	chmod u+x bin/gunicorn_start.sh;


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