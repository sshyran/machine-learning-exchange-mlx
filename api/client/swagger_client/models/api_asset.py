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

"""
    MLX API

    MLX API Extension for Kubeflow Pipelines  # noqa: E501

    OpenAPI spec version: 0.1.25-related-assets
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ApiAsset(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'created_at': 'datetime',
        'name': 'str',
        'description': 'str',
        'featured': 'bool',
        'publish_approved': 'bool',
        'related_assets': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'name': 'name',
        'description': 'description',
        'featured': 'featured',
        'publish_approved': 'publish_approved',
        'related_assets': 'related_assets'
    }

    def __init__(self, id=None, created_at=None, name=None, description=None, featured=None, publish_approved=None, related_assets=None):  # noqa: E501
        """ApiAsset - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._created_at = None
        self._name = None
        self._description = None
        self._featured = None
        self._publish_approved = None
        self._related_assets = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        self.name = name
        self.description = description
        if featured is not None:
            self.featured = featured
        if publish_approved is not None:
            self.publish_approved = publish_approved
        if related_assets is not None:
            self.related_assets = related_assets

    @property
    def id(self):
        """Gets the id of this ApiAsset.  # noqa: E501


        :return: The id of this ApiAsset.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiAsset.


        :param id: The id of this ApiAsset.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this ApiAsset.  # noqa: E501


        :return: The created_at of this ApiAsset.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ApiAsset.


        :param created_at: The created_at of this ApiAsset.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def name(self):
        """Gets the name of this ApiAsset.  # noqa: E501


        :return: The name of this ApiAsset.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiAsset.


        :param name: The name of this ApiAsset.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this ApiAsset.  # noqa: E501


        :return: The description of this ApiAsset.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiAsset.


        :param description: The description of this ApiAsset.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def featured(self):
        """Gets the featured of this ApiAsset.  # noqa: E501


        :return: The featured of this ApiAsset.  # noqa: E501
        :rtype: bool
        """
        return self._featured

    @featured.setter
    def featured(self, featured):
        """Sets the featured of this ApiAsset.


        :param featured: The featured of this ApiAsset.  # noqa: E501
        :type: bool
        """

        self._featured = featured

    @property
    def publish_approved(self):
        """Gets the publish_approved of this ApiAsset.  # noqa: E501


        :return: The publish_approved of this ApiAsset.  # noqa: E501
        :rtype: bool
        """
        return self._publish_approved

    @publish_approved.setter
    def publish_approved(self, publish_approved):
        """Sets the publish_approved of this ApiAsset.


        :param publish_approved: The publish_approved of this ApiAsset.  # noqa: E501
        :type: bool
        """

        self._publish_approved = publish_approved

    @property
    def related_assets(self):
        """Gets the related_assets of this ApiAsset.  # noqa: E501


        :return: The related_assets of this ApiAsset.  # noqa: E501
        :rtype: list[str]
        """
        return self._related_assets

    @related_assets.setter
    def related_assets(self, related_assets):
        """Sets the related_assets of this ApiAsset.


        :param related_assets: The related_assets of this ApiAsset.  # noqa: E501
        :type: list[str]
        """

        self._related_assets = related_assets

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ApiAsset, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiAsset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
