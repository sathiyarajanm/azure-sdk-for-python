# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ServiceConfiguration(Model):
    """The service configuration.

    :param version: The version of the sync service.
    :type version: str
    :param service_type: The service type of the server.
    :type service_type: int
    :param service_account: The service account.
    :type service_account: str
    :param sql_server: The SQL server information.
    :type sql_server: str
    :param sql_version: The SQL version.
    :type sql_version: str
    :param sql_edition: The SQL edition
    :type sql_edition: str
    :param sql_instance: The SQL instance details.
    :type sql_instance: str
    :param sql_database_name: The SQL database.
    :type sql_database_name: str
    :param sql_database_size: The SQL database size.
    :type sql_database_size: int
    """

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'},
        'service_type': {'key': 'serviceType', 'type': 'int'},
        'service_account': {'key': 'serviceAccount', 'type': 'str'},
        'sql_server': {'key': 'sqlServer', 'type': 'str'},
        'sql_version': {'key': 'sqlVersion', 'type': 'str'},
        'sql_edition': {'key': 'sqlEdition', 'type': 'str'},
        'sql_instance': {'key': 'sqlInstance', 'type': 'str'},
        'sql_database_name': {'key': 'sqlDatabaseName', 'type': 'str'},
        'sql_database_size': {'key': 'sqlDatabaseSize', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(ServiceConfiguration, self).__init__(**kwargs)
        self.version = kwargs.get('version', None)
        self.service_type = kwargs.get('service_type', None)
        self.service_account = kwargs.get('service_account', None)
        self.sql_server = kwargs.get('sql_server', None)
        self.sql_version = kwargs.get('sql_version', None)
        self.sql_edition = kwargs.get('sql_edition', None)
        self.sql_instance = kwargs.get('sql_instance', None)
        self.sql_database_name = kwargs.get('sql_database_name', None)
        self.sql_database_size = kwargs.get('sql_database_size', None)
