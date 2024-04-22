""" Copyright (c) 2024 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
           https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied. 
"""


import intersight.api.workflow_api
import credentials

wf_name = "test workflow"


def get_workflows(apiClient):
    api_instance = intersight.api.workflow_api.WorkflowApi(apiClient)
    workflows = api_instance.get_workflow_workflow_info_list()
    for i in workflows.results:
        # if i.name == wf_name:
        print("Name: " + i.name)
        print("Workflow Info MoId: " + i.moid)
        print("Status: " + i.status)
        print("Workflow Definition MoId: " + i.workflow_definition['moid'])
        get_workflow_inputs(apiClient, i.workflow_definition['moid'])


def get_workflow_inputs(apiClient, moId):
    api_instance = intersight.api.workflow_api.WorkflowApi(apiClient)
    workflows = api_instance.get_workflow_workflow_definition_by_moid(moId)
    for k in workflows.permission_resources:
        print("Organization MoId: " + k.moid)
    for i in workflows.input_definition:
        print("Input name: " + i.name)
        print("Input type: " + i.properties['type'])


def main():
    apiClient = credentials.config_credentials()
    try:
        get_workflows(apiClient)
    except intersight.OpenApiException as e:
        print(e)


if __name__ == "__main__":
    main()
