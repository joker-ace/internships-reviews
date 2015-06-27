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

# project settings ==========================================
project_user = config.get('project', 'user')
project_user_group = config.get('project', 'group')
project_folder = config.get('project', 'folder')
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
    'python-dev',
    'make',
    'gcc',
    'libpq-dev',
    'python-virtualenv',
    'git',
    'postgresql',
    'postgresql-contrib',
    'nginx',
    'supervisor'
)


def install_system_packages():
    system_packages_list = ' '.join(system_packages)
    run('apt-get install {}'.format(system_packages_list))


def create_project_owner():
    run('groupadd --system {}'.format(project_user_group))
    run(
        'useradd --system --gid {} --shell /bin/bash --home {} {}'.format(
            project_user_group, project_folder, project_user
        )
    )


def create_project_folder_structure():
    run('mkdir -p {}'.format(project_folder))
    run('chown {} {}'.format(project_user, project_folder))


def create_project_database():
    sudo(
        'createuser --interactive -P',
        user='postgres'
    )
    sudo(
        'createdb --owner {} {}'.format(config.get('database', 'user'), config.get('database', 'name')),
        user='postgres'
    )


def get_project_from_github():
    with cd(project_folder):
        run('pwd')
        run('git clone {} .'.format(github_repository))


def change_project_files_owner():
    run('chown -R {}:{} {}'.format(project_user, project_user_group, project_folder))
    run('chmod -R g+w {}'.format(project_folder))


def build_project_environment():
    with cd(project_folder):
        run('chmod u+x Makefile')
        run('make create-core-environment')


def django_management_commands():
    with cd(project_folder):
        run('env/bin/python2.7 src/manage.py makemigrations')
        run('env/bin/python2.7 src/manage.py migrate')
        run('env/bin/python2.7 src/manage.py collectstatic --noinput')


def django_create_superuser():
    with cd(project_folder):
        run('env/bin/python2.7 src/manage.py createsuperuser --username {}'.format(django_superuser_username))


def install_supervisor_config():
    with cd(project_folder):
        run('cp config/supervisor/internships.conf /etc/supervisor/conf.d/internships.conf')
        run('supervisorctl reread')
        run('supervisorctl update')
        run('supervisorctl restart all')


def clean_deploy():
    install_system_packages()
    create_project_database()
    create_project_owner()
    create_project_folder_structure()
    get_project_from_github()
    build_project_environment()
    django_management_commands()
    django_create_superuser()
    change_project_files_owner()
    install_supervisor_config()