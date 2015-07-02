# -*- coding: utf-8 -*-

# imports ===============================
from fabric.api import *
from ConfigParser import ConfigParser
# =======================================

# create configuration reader ===========
CONFIG_FILE = 'deployment.ini'
config = ConfigParser()
config.read(CONFIG_FILE)
# =======================================

# environment configuration =================================
env.hosts = [config.get('production-server', 'host')]
env.user = config.get('production-server', 'user')
env.password = config.get('production-server', 'password')
env.prompts = {}
# ===========================================================

# application settings ======================================
project_user = config.get('application', 'user')
project_user_group = config.get('application', 'group')
project_folder = config.get('application', 'folder')
# ===========================================================

# database settings =========================================
database_user = config.get('database', 'user')
database_password = config.get('database', 'password')

database_prompts = {
    'Enter name of role to add: ': database_user,
    'Enter password for new role: ': database_password,
    'Enter it again: ': database_password,
    'Shall the new role be a superuser? (y/n) ': 'n',
    'Shall the new role be allowed to create databases? (y/n) ': 'n',
    'Shall the new role be allowed to create more new roles? (y/n) ': 'n'
}
env.prompts.update(database_prompts)
# ===========================================================

# github settings ===========================================
github_repository = config.get('github', 'repository')
# ===========================================================

# django settings ===========================================
django_superuser_username = config.get('django-superuser', 'username')
django_superuser_password = config.get('django-superuser', 'password')
django_superuser_prompts = {
    'Email address: ': '',
    'Password: ': django_superuser_password,
    'Password (again): ': django_superuser_password
}
env.prompts.update(django_superuser_prompts)
# ===========================================================

system_packages = (
    'gcc',
    'make',
    'python-dev',
    'libpq-dev',
    'python-virtualenv',
    'postgresql',
    'postgresql-contrib',
    'nginx',
    'supervisor',
    'git',
)


def install_system_packages():
    system_packages_list = ' '.join(system_packages)
    run('apt-get install {}'.format(system_packages_list))


def create_system_user_for_application():
    run('groupadd --system {}'.format(project_user_group))
    run(
        'useradd --system --gid {} --shell /bin/bash --home {} {}'.format(
            project_user_group, project_folder, project_user
        )
    )
    run('mkdir -p {}'.format(project_folder))
    run('chown {} {}'.format(project_user, project_folder))


def create_application_folders_structure():
    with cd(project_folder):
        run('mkdir -p logs')
        run('mkdir -p run')
        run('mkdir -p media_content')
        run('touch logs/gunicorn_supervisor.log')
        run('chmod u+x bin/gunicorn_start.sh')


def create_application_database():
    sudo(
        'createdb --owner {} {}'.format(config.get('database', 'user'), config.get('database', 'name')),
        user='postgres'
    )


def create_application_database_user():
    sudo(
        'createuser --interactive -P',
        user='postgres'
    )


def clone_application_from_repository():
    with cd(project_folder):
        run('git clone {} .'.format(github_repository))


def change_application_files_owner():
    run('chown -R {}:{} {}'.format(project_user, project_user_group, project_folder))
    run('chmod -R g+w {}'.format(project_folder))


def create_application_environment():
    with cd(project_folder):
        run('rm -rf env')
        run('virtualenv env')


def install_application_packages():
    with cd(project_folder):
        run('env/bin/pip install --requirement requirements.txt')


def process_application_migrations():
    with cd(project_folder):
        run('env/bin/python2.7 src/manage.py makemigrations')
        run('env/bin/python2.7 src/manage.py migrate')


def process_application_static_files():
    with cd(project_folder):
        run('env/bin/python2.7 src/manage.py collectstatic --noinput')


def create_application_superuser():
    with cd(project_folder):
        run('env/bin/python2.7 src/manage.py createsuperuser --username {}'.format(django_superuser_username))


def install_supervisor_config():
    with cd(project_folder):
        run('cp --update config/supervisor/internships.conf /etc/supervisor/conf.d/internships.conf')
        run('supervisorctl reread')
        run('supervisorctl update')
        run('supervisorctl restart all')


def restart_supervisor():
    run('supervisorctl restart all')


def install_nginx_config():
    with cd(project_folder):
        run('cp --update config/nginx/internships.conf /etc/nginx/sites-available/internships.conf')
        run('ln -s -f /etc/nginx/sites-available/internships.conf /etc/nginx/sites-enabled/internships.conf')


def restart_nginx():
    run('service nginx restart')


def get_last_application_version():
    with cd(project_folder):
        run('git checkout -- .')
        run('git pull origin master')


def load_application_initial_data():
    with cd(project_folder):
        run('env/bin/python2.7 src/manage.py loaddata --ignorenonexistent provinces.json')


def update():
    get_last_application_version()
    create_application_folders_structure()
    change_application_files_owner()
    process_application_migrations()
    process_application_static_files()
    restart_supervisor()
    restart_nginx()


def clear_install():
    install_system_packages()
    create_application_database_user()
    create_application_database()
    create_system_user_for_application()
    create_application_folders_structure()
    clone_application_from_repository()
    create_application_environment()
    install_application_packages()
    process_application_migrations()
    load_application_initial_data()
    process_application_static_files()
    create_application_superuser()
    change_application_files_owner()
    install_supervisor_config()
    restart_supervisor()
    change_application_files_owner()
    install_nginx_config()
    restart_nginx()