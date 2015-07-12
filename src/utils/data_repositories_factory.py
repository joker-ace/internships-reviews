# -*- coding: utf-8 -*-

from common.repository import Repository as CommonDataRepository
from students.repository import Repository as UsersDataRepository


class DataRepositoriesFactory(object):
    @property
    def common(self):
        return CommonDataRepository()

    @property
    def users(self):
        return UsersDataRepository()
