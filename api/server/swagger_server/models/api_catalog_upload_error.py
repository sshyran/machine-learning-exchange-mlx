# Copyright 2021 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ApiCatalogUploadError(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, url: str=None, error_message: str=None, status_code: int=None):  # noqa: E501
        """ApiCatalogUploadError - a model defined in Swagger

        :param name: The name of this ApiCatalogUploadError.  # noqa: E501
        :type name: str
        :param url: The url of this ApiCatalogUploadError.  # noqa: E501
        :type url: str
        :param error_message: The error_message of this ApiCatalogUploadError.  # noqa: E501
        :type error_message: str
        :param status_code: The status_code of this ApiCatalogUploadError.  # noqa: E501
        :type status_code: int
        """
        self.swagger_types = {
            'name': str,
            'url': str,
            'error_message': str,
            'status_code': int
        }

        self.attribute_map = {
            'name': 'name',
            'url': 'url',
            'error_message': 'error_message',
            'status_code': 'status_code'
        }

        self._name = name
        self._url = url
        self._error_message = error_message
        self._status_code = status_code

    @classmethod
    def from_dict(cls, dikt) -> 'ApiCatalogUploadError':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The apiCatalogUploadError of this ApiCatalogUploadError.  # noqa: E501
        :rtype: ApiCatalogUploadError
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this ApiCatalogUploadError.


        :return: The name of this ApiCatalogUploadError.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ApiCatalogUploadError.


        :param name: The name of this ApiCatalogUploadError.
        :type name: str
        """

        self._name = name

    @property
    def url(self) -> str:
        """Gets the url of this ApiCatalogUploadError.

        The URL to the YAML metadata file, i.e. on GitHub.com  # noqa: E501

        :return: The url of this ApiCatalogUploadError.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this ApiCatalogUploadError.

        The URL to the YAML metadata file, i.e. on GitHub.com  # noqa: E501

        :param url: The url of this ApiCatalogUploadError.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def error_message(self) -> str:
        """Gets the error_message of this ApiCatalogUploadError.


        :return: The error_message of this ApiCatalogUploadError.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message: str):
        """Sets the error_message of this ApiCatalogUploadError.


        :param error_message: The error_message of this ApiCatalogUploadError.
        :type error_message: str
        """

        self._error_message = error_message

    @property
    def status_code(self) -> int:
        """Gets the status_code of this ApiCatalogUploadError.


        :return: The status_code of this ApiCatalogUploadError.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code: int):
        """Sets the status_code of this ApiCatalogUploadError.


        :param status_code: The status_code of this ApiCatalogUploadError.
        :type status_code: int
        """

        self._status_code = status_code
