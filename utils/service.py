import logging
from abc import ABC, abstractmethod
from typing import Type, Union

from utils.unitofwork import IUnitOfWork


class BaseService:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
