import os
from api.pod_client import PodsClient
import pytest

class PodFixtures:
    
    @pytest.fixture()
    def get_pod_replicas(self,simple_deployment):
        print("simple deployment",simple_deployment)
        response = PodsClient.get_pods_for_namespace(self,'default')
        replicas = 0
        for res in response:
            print(res.metadata.name)
            if res.metadata.name == "coredns":
                print(res.spec.replicas)
                replicas = res.spec.replicas
            return replicas

    def test_fixture(self,get_pod_replicas):
        res = get_pod_replicas
        print("fixture output is")


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

