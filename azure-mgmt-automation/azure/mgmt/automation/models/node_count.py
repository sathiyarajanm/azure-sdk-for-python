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


class NodeCount(Model):
    """Number of nodes based on the Filter.

    :param name: Gets the name of a count type
    :type name: str
    :param properties:
    :type properties: ~azure.mgmt.automation.models.NodeCountProperties
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'NodeCountProperties'},
    }

    def __init__(self, name=None, properties=None):
        super(NodeCount, self).__init__()
        self.name = name
        self.properties = properties
