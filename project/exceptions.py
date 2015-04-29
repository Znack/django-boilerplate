# -*- coding: utf-8 -*-


class OpenCostBaseException(Exception):
    pass


class OpenCostBaseDirectoryVariableException(OpenCostBaseException):
    pass


class OpenCostLocalSettingsDoesNotExist(OpenCostBaseException):
    pass