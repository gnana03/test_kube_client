import pytest
import os

from api.pod_client import PodsClient


class deployments_fixtures:


    @pytest.fixture()
    def get_deployments_replicas_for_pod(self):
        response = PodsClient.list_namespaced_deployment(namespace="kube-system")
        #    print(model.items[0].metadata.name)
        replicas = 0
        for res in response:
            print(res.metadata.name)
            if res.metadata.name == "coredns":
                print(res.spec.replicas)
                replicas = res.spec.replicas
        return replicas

    def test_deployment_fixture(self,get_deployments_replicas_for_pod):
        print("testing started")

