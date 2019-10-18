import pytest

from fixtures.deployment_fixtures import deployments_fixtures


class Test_Pods_Replicas(deployments_fixtures):


    def test_get_pods_replicas(self,get_deployments_replicas_for_pod):
        response = get_deployments_replicas_for_pod
        replicas = 0
        assert replicas, 2


