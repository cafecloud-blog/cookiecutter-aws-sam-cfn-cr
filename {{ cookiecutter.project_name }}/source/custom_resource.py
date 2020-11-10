from __future__ import print_function
from crhelper import CfnResource
import logging
import resource_helper

logger = logging.getLogger(__name__)
# Initialise the helper, all inputs are optional
helper = CfnResource(json_logging=False,
                     log_level='DEBUG',
                     boto_level='CRITICAL')

try:
    # Init code for the custom resource
    pass
except Exception as e:
    helper.init_failure(e)


@helper.create
def create(event, context):
    logger.info("Creating Custom::{{ cookiecutter.resource_type }}")
    # Optionally return an ID that will be used for the
    # resource PhysicalResourceId, if None is returned an ID
    # will be generated. If a poll_create function is defined
    # return value is placed into the poll event as:
    # event['CrHelperData']['PhysicalResourceId']
    #
    # To add response data update the helper.Data dict
    # If poll is enabled data is placed into poll event as
    # event['CrHelperData']
    helper.Data.update({"test": "testdata"})

    # use the custom resource_helper module to invoke any re-useable logic here
    resource_helper.cfn_resource_helper()

    # To return an error to cloudformation you raise an exception:
    if not helper.Data.get("test"):
        raise ValueError("this error will show in the cloudformation "
                         "events log and console.")

    return "MyResourceId"


@helper.update
def update(event, context):
    logger.info("Updating Custom::{{ cookiecutter.resource_type }}")
    # If the update resulted in a new resource being created,
    # return an id for the new resource.
    # CloudFormation will send a delete event with the old id
    # when stack update completes


@helper.delete
def delete(event, context):
    logger.info("Deleting Custom::{{ cookiecutter.resource_type }}")
    # Delete never returns anything.
    # Should not fail if the underlying resources are already deleted.


@helper.poll_create
def poll_create(event, context):
    logger.info("Polling during the creation of Custom::{{ cookiecutter.resource_type }}")
    # Return a resource id or True to indicate that creation is complete.
    # if True is returned an id will be generated
    return True

def lambda_handler(event, context):
    helper(event, context)