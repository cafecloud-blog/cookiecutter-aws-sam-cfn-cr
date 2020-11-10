import logging

logger = logging.getLogger(__name__)


def cfn_resource_helper():
    """ A helper method for the custom cloudformation resource """

    # Custom logic goes here. This might include side effects or
    # Producing a a return value used elsewhere in your code.
    logger.info("cfn_resource_helper logic")
    return True
