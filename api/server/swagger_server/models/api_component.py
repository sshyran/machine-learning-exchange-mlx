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
from swagger_server.models.api_metadata import ApiMetadata  # noqa: F401,E501
from swagger_server.models.api_parameter import ApiParameter  # noqa: F401,E501
from swagger_server import util


class ApiComponent(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, created_at: datetime=None, name: str=None, description: str=None, featured: bool=None, publish_approved: bool=None, related_assets: List[str]=None, metadata: ApiMetadata=None, parameters: List[ApiParameter]=None):  # noqa: E501
        """ApiComponent - a model defined in Swagger

        :param id: The id of this ApiComponent.  # noqa: E501
        :type id: str
        :param created_at: The created_at of this ApiComponent.  # noqa: E501
        :type created_at: datetime
        :param name: The name of this ApiComponent.  # noqa: E501
        :type name: str
        :param description: The description of this ApiComponent.  # noqa: E501
        :type description: str
        :param featured: The featured of this ApiComponent.  # noqa: E501
        :type featured: bool
        :param publish_approved: The publish_approved of this ApiComponent.  # noqa: E501
        :type publish_approved: bool
        :param related_assets: The related_assets of this ApiComponent.  # noqa: E501
        :type related_assets: List[str]
        :param metadata: The metadata of this ApiComponent.  # noqa: E501
        :type metadata: ApiMetadata
        :param parameters: The parameters of this ApiComponent.  # noqa: E501
        :type parameters: List[ApiParameter]
        """
        self.swagger_types = {
            'id': str,
            'created_at': datetime,
            'name': str,
            'description': str,
            'featured': bool,
            'publish_approved': bool,
            'related_assets': List[str],
            'metadata': ApiMetadata,
            'parameters': List[ApiParameter]
        }

        self.attribute_map = {
            'id': 'id',
            'created_at': 'created_at',
            'name': 'name',
            'description': 'description',
            'featured': 'featured',
            'publish_approved': 'publish_approved',
            'related_assets': 'related_assets',
            'metadata': 'metadata',
            'parameters': 'parameters'
        }

        self._id = id
        self._created_at = created_at
        self._name = name
        self._description = description
        self._featured = featured
        self._publish_approved = publish_approved
        self._related_assets = related_assets
        self._metadata = metadata
        self._parameters = parameters

    @classmethod
    def from_dict(cls, dikt) -> 'ApiComponent':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The apiComponent of this ApiComponent.  # noqa: E501
        :rtype: ApiComponent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this ApiComponent.


        :return: The id of this ApiComponent.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this ApiComponent.


        :param id: The id of this ApiComponent.
        :type id: str
        """

        self._id = id

    @property
    def created_at(self) -> datetime:
        """Gets the created_at of this ApiComponent.


        :return: The created_at of this ApiComponent.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: datetime):
        """Sets the created_at of this ApiComponent.


        :param created_at: The created_at of this ApiComponent.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def name(self) -> str:
        """Gets the name of this ApiComponent.


        :return: The name of this ApiComponent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ApiComponent.


        :param name: The name of this ApiComponent.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self) -> str:
        """Gets the description of this ApiComponent.


        :return: The description of this ApiComponent.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this ApiComponent.


        :param description: The description of this ApiComponent.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def featured(self) -> bool:
        """Gets the featured of this ApiComponent.


        :return: The featured of this ApiComponent.
        :rtype: bool
        """
        return self._featured

    @featured.setter
    def featured(self, featured: bool):
        """Sets the featured of this ApiComponent.


        :param featured: The featured of this ApiComponent.
        :type featured: bool
        """

        self._featured = featured

    @property
    def publish_approved(self) -> bool:
        """Gets the publish_approved of this ApiComponent.


        :return: The publish_approved of this ApiComponent.
        :rtype: bool
        """
        return self._publish_approved

    @publish_approved.setter
    def publish_approved(self, publish_approved: bool):
        """Sets the publish_approved of this ApiComponent.


        :param publish_approved: The publish_approved of this ApiComponent.
        :type publish_approved: bool
        """

        self._publish_approved = publish_approved

    @property
    def related_assets(self) -> List[str]:
        """Gets the related_assets of this ApiComponent.


        :return: The related_assets of this ApiComponent.
        :rtype: List[str]
        """
        return self._related_assets

    @related_assets.setter
    def related_assets(self, related_assets: List[str]):
        """Sets the related_assets of this ApiComponent.


        :param related_assets: The related_assets of this ApiComponent.
        :type related_assets: List[str]
        """

        self._related_assets = related_assets

    @property
    def metadata(self) -> ApiMetadata:
        """Gets the metadata of this ApiComponent.


        :return: The metadata of this ApiComponent.
        :rtype: ApiMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: ApiMetadata):
        """Sets the metadata of this ApiComponent.


        :param metadata: The metadata of this ApiComponent.
        :type metadata: ApiMetadata
        """

        self._metadata = metadata

    @property
    def parameters(self) -> List[ApiParameter]:
        """Gets the parameters of this ApiComponent.


        :return: The parameters of this ApiComponent.
        :rtype: List[ApiParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters: List[ApiParameter]):
        """Sets the parameters of this ApiComponent.


        :param parameters: The parameters of this ApiComponent.
        :type parameters: List[ApiParameter]
        """

        self._parameters = parameters
