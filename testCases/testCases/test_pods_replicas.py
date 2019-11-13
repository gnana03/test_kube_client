import pytest
import os
# from yaml_read_file.yaml_read import ReadYAML
from fixtures.deployment_fixtures import deployments_fixtures


class Test_Pods_Replicas(deployments_fixtures):
    def test_get_pods_replicas(get_deployments_replicas_for_pod):
        replicas = get_deployments_replicas_for_pod
        print("replicas",replicas)
        assert replicas==10


