# coding: utf-8

"""
    LocationIQ

    LocationIQ provides flexible enterprise-grade location based solutions. We work with developers, startups and enterprises worldwide serving billions of requests everyday. This page provides an overview of the technical aspects of our API and will help you get started.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Address(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'house_number': 'str',
        'road': 'str',
        'residential': 'str',
        'village': 'str',
        'county': 'str',
        'state': 'str',
        'postcode': 'str',
        'country': 'str',
        'country_code': 'str',
        'city': 'str'
    }

    attribute_map = {
        'house_number': 'house_number',
        'road': 'road',
        'residential': 'residential',
        'village': 'village',
        'county': 'county',
        'state': 'state',
        'postcode': 'postcode',
        'country': 'country',
        'country_code': 'country_code',
        'city': 'city'
    }

    def __init__(self, house_number=None, road=None, residential=None, village=None, county=None, state=None, postcode=None, country=None, country_code=None, city=None):  # noqa: E501
        """Address - a model defined in OpenAPI"""  # noqa: E501

        self._house_number = None
        self._road = None
        self._residential = None
        self._village = None
        self._county = None
        self._state = None
        self._postcode = None
        self._country = None
        self._country_code = None
        self._city = None
        self.discriminator = None

        if house_number is not None:
            self.house_number = house_number
        if road is not None:
            self.road = road
        if residential is not None:
            self.residential = residential
        if village is not None:
            self.village = village
        if county is not None:
            self.county = county
        if state is not None:
            self.state = state
        if postcode is not None:
            self.postcode = postcode
        if country is not None:
            self.country = country
        if country_code is not None:
            self.country_code = country_code
        if city is not None:
            self.city = city

    @property
    def house_number(self):
        """Gets the house_number of this Address.  # noqa: E501


        :return: The house_number of this Address.  # noqa: E501
        :rtype: str
        """
        return self._house_number

    @house_number.setter
    def house_number(self, house_number):
        """Sets the house_number of this Address.


        :param house_number: The house_number of this Address.  # noqa: E501
        :type: str
        """

        self._house_number = house_number

    @property
    def road(self):
        """Gets the road of this Address.  # noqa: E501


        :return: The road of this Address.  # noqa: E501
        :rtype: str
        """
        return self._road

    @road.setter
    def road(self, road):
        """Sets the road of this Address.


        :param road: The road of this Address.  # noqa: E501
        :type: str
        """

        self._road = road

    @property
    def residential(self):
        """Gets the residential of this Address.  # noqa: E501


        :return: The residential of this Address.  # noqa: E501
        :rtype: str
        """
        return self._residential

    @residential.setter
    def residential(self, residential):
        """Sets the residential of this Address.


        :param residential: The residential of this Address.  # noqa: E501
        :type: str
        """

        self._residential = residential

    @property
    def village(self):
        """Gets the village of this Address.  # noqa: E501


        :return: The village of this Address.  # noqa: E501
        :rtype: str
        """
        return self._village

    @village.setter
    def village(self, village):
        """Sets the village of this Address.


        :param village: The village of this Address.  # noqa: E501
        :type: str
        """

        self._village = village

    @property
    def county(self):
        """Gets the county of this Address.  # noqa: E501


        :return: The county of this Address.  # noqa: E501
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """Sets the county of this Address.


        :param county: The county of this Address.  # noqa: E501
        :type: str
        """

        self._county = county

    @property
    def state(self):
        """Gets the state of this Address.  # noqa: E501


        :return: The state of this Address.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Address.


        :param state: The state of this Address.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def postcode(self):
        """Gets the postcode of this Address.  # noqa: E501


        :return: The postcode of this Address.  # noqa: E501
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this Address.


        :param postcode: The postcode of this Address.  # noqa: E501
        :type: str
        """

        self._postcode = postcode

    @property
    def country(self):
        """Gets the country of this Address.  # noqa: E501


        :return: The country of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Address.


        :param country: The country of this Address.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def country_code(self):
        """Gets the country_code of this Address.  # noqa: E501


        :return: The country_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Address.


        :param country_code: The country_code of this Address.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def city(self):
        """Gets the city of this Address.  # noqa: E501


        :return: The city of this Address.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Address.


        :param city: The city of this Address.  # noqa: E501
        :type: str
        """

        self._city = city

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Address):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
