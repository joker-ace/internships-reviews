# -*- coding: utf-8 -*-

from common.repositories.common_data_repository import CommonDataRepository
from students.repositories.users_data_repository import UsersDataRepository
from companies.repositories.companies_data_repository import CompaniesDataRepository

class DataRepositoriesFactory(object):
    @property
    def common(self):
        return CommonDataRepository()

    @property
    def users(self):
        return UsersDataRepository()

    @property
    def companies_data(self):
        return CompaniesDataRepository()