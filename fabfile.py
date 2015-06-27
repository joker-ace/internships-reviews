# -*- coding: utf-8 -*-
from fabric.api import *
from ConfigParser import ConfigParser

CONFIG_FILE = 'deployment.ini'

config = ConfigParser()
config.read(CONFIG_FILE)

env.hosts = [
    config.get('production-server', 'host')
]

env.user = config.get('production-server', 'user')
env.password = config.get('production-server', 'password')

project_user = config.get('project', 'user')
project_user_group = config.get('project', 'group')
project_folder = config.get('project', 'folder')

env.prompts = {
    'Enter name of role to add: ': config.get('database', 'user'),
    'Enter password for new role: ': config.get('database', 'password'),
    'Enter it again: ': config.get('database', 'password'),
    'Shall the new role be a superuser? (y/n) ': 'n',
    'Shall the new role be allowed to create databases? (y/n) ': 'n',
    'Shall the new role be allowed to create more new roles? (y/n) ': 'n'
}

system_packages = (
    'python-dev',
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
    run('useradd --system --gid {} --shell /bin/bash --home {} {}'.format(
        project_user_group,
        project_folder,
        project_user))


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