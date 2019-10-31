import pytest
import os

from fixtures.deployment_fixtures import deployments_fixtures


class Test_Pods_Replicas(deployments_fixtures):
    def test_get_pods_replicas(get_deployments_replicas_for_pod):
        replicas = get_deployments_replicas_for_pod
        assert replicas, 2


