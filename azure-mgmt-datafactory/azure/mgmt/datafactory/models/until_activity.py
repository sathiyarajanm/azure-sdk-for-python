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

from .control_activity import ControlActivity


class UntilActivity(ControlActivity):
    """This activity executes inner activities until the specified boolean
    expression results to true or timeout is reached, whichever is earlier.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param name: Required. Activity name.
    :type name: str
    :param description: Activity description.
    :type description: str
    :param depends_on: Activity depends on condition.
    :type depends_on: list[~azure.mgmt.datafactory.models.ActivityDependency]
    :param user_properties: Activity user properties.
    :type user_properties: dict[str, str]
    :param type: Required. Constant filled by server.
    :type type: str
    :param expression: Required. An expression that would evaluate to Boolean.
     The loop will continue until this expression evaluates to true
    :type expression: ~azure.mgmt.datafactory.models.Expression
    :param timeout: Specifies the timeout for the activity to run. If there is
     no value specified, it takes the value of TimeSpan.FromDays(7) which is 1
     week as default. Type: string (or Expression with resultType string),
     pattern: ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])). Type:
     string (or Expression with resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type timeout: object
    :param activities: Required. List of activities to execute.
    :type activities: list[~azure.mgmt.datafactory.models.Activity]
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
        'expression': {'required': True},
        'activities': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'depends_on': {'key': 'dependsOn', 'type': '[ActivityDependency]'},
        'user_properties': {'key': 'userProperties', 'type': '{str}'},
        'type': {'key': 'type', 'type': 'str'},
        'expression': {'key': 'typeProperties.expression', 'type': 'Expression'},
        'timeout': {'key': 'typeProperties.timeout', 'type': 'object'},
        'activities': {'key': 'typeProperties.activities', 'type': '[Activity]'},
    }

    def __init__(self, **kwargs):
        super(UntilActivity, self).__init__(**kwargs)
        self.expression = kwargs.get('expression', None)
        self.timeout = kwargs.get('timeout', None)
        self.activities = kwargs.get('activities', None)
        self.type = 'Until'
