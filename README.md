# gve_devnet_intersight_workflow_runner
sample code for running custom workflow in Intersight Cloud Orchestrator and retrieving the output. 


## Contacts
* Kevin Chen

## Solution Components
* Intersight

## Related Sandbox Environment
This uses a workflow originally from dCloud demo of Intersight, Getting started with Intersight orchestration V2, the SDK is using the default SaaS platform therefore the workflow is exported from the dCloud demo and re-imported to Intersight. 


## Installation/Configuration

1. Set up a Python virtual environment. Make sure Python 3 is installed in your environment, and if not, you may download Python [here](https://www.python.org/downloads/). Once Python 3 is installed in your environment, you can activate the virtual environment with the instructions found [here](https://docs.python.org/3/tutorial/venv.html).

2. Install the requirements with `pip3 install -r requirements.txt`

3. Generate Intersight API KEY ID and secret on the Intersight dashboard. Follow the latest instructions here on the [Intersight API Documentation](https://intersight.com/apidocs/introduction/security/) 

4. Set up the environment file as per .env example file. The .env file contains credentials used for the code to authenticate with Intersight. 

```
INTERSIGHT_API_KEY_ID = [insert your API KEY ID generated]
INTERSIGHT_API_PRIVATE_KEY = [path to the secret key text file downloaded from Intersight]
Organization_MoId = [The organization ID for your specific Organization on Intersight]
```

5. You can run sampleCode/get_workflows.py to see the history of workflows that has been executed. 

```
$ python sampleCode/get_workflows.py
```

This will generate an output that lists workflow information such as workflow definition MoId, inputs used, status, etc. The information here can be used for step 6.

6. Customise sampleCode/run_workflow.py to run your workflows. 

Currently the function refer to a workflow corresponding to my specific demo instance, therefore workflow definition MoId should be modified according to the information collected in step 5. 

``` python
    workflow_definition=WorkflowWorkflowDefinitionRelationship(
        class_id="mo.MoRef",
        moid="660b69c7696f6e3201f1dc71",
        object_type="workflow.WorkflowDefinition"
    )
```

## Usage

7. Run the modified python script

```
$ python sampleCode/run_workflow.py
```

# Screenshots

![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.