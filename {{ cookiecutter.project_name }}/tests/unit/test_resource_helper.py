import json

from source import resource_helper


def test_cfn_resource_helper():
    ret = resource_helper.cfn_resource_helper()

    assert ret