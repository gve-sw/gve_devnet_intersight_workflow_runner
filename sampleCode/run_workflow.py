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

#!/usr/bin/env python
import intersight
import intersight.api.workflow_api
import credentials
from intersight.api.workflow_api import WorkflowApi
from intersight.model.workflow_workflow_info import WorkflowWorkflowInfo
from intersight.model.mo_base_mo_relationship import MoBaseMoRelationship
from intersight.model.workflow_initiator_context import WorkflowInitiatorContext
from intersight.model.workflow_workflow_definition_relationship import WorkflowWorkflowDefinitionRelationship
from pprint import pprint
import time
import os

# User Input
Organization_MoId = os.getenv("Organization_MoId")
city = "brisbane"
country = "AUS"
units = "metric"

# Workflow info is used to define a new run of an existing workflow (dCloud Get Current Weather)
mo = WorkflowWorkflowInfo(
    action="Start",
    input={
        "city": city,
        "country": country,
        "units": units},
    name="Temp Demo",
    workflow_definition=WorkflowWorkflowDefinitionRelationship(
        class_id="mo.MoRef",
        moid="660b69c7696f6e3201f1dc71",
        object_type="workflow.WorkflowDefinition"
    )
)


def create_workflow_workflow_info(apiClient, mo):
    print("city: "+mo.input['city'])
    api_instance = intersight.api.workflow_api.WorkflowApi(apiClient)
    workflow = api_instance.create_workflow_workflow_info(mo)
    # print(workflow)
    return workflow


def get_workflow_output(apiClient, moid):
    api_instance = intersight.api.workflow_api.WorkflowApi(apiClient)
    output = api_instance.get_workflow_workflow_info_by_moid(moid)
    print(output.output)
    return output


def main():
    apiClient = credentials.config_credentials()
    try:
        workflow_attempt = create_workflow_workflow_info(apiClient, mo)
    except intersight.OpenApiException as e:
        print(e)

    while True:
        try:
            output = get_workflow_output(apiClient, workflow_attempt.moid)
        except intersight.OpenApiException as e:
            print(e)
        if output.workflow_status == "Completed":
            break
        print("Waiting for workflow to compelete. status: " +
              output.workflow_status)
        time.sleep(2)


if __name__ == "__main__":
    main()
