import pytest
import os

from fixtures.deployment_fixtures import deployments_fixtures


class Test_Pods_Replicas(deployments_fixtures):
    def test_get_pods_replicas(get_deployment_info):
        replicas = get_deployment_info
        print(replicas)

