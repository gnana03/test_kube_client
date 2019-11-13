import pytest
import os

from yaml_read_file.read_yaml import ReadYAML
from api.pod_client import PodsClient
from api.deployment_client import DeploymentClient

class deployments_fixtures():


    @pytest.fixture()
    def get_deployments_replicas_for_pod(self):
        response = PodsClient.list_namespaced_deployment(namespace="kube-system")
        print(model.items[0].metadata.name)
        replicas = 0
        for res in response:
            print(res.metadata.name)
            if res.metadata.name == "coredns":
                print(res.spec.replicas)
                replicas = res.spec.replicas
        return replicas

    @pytest.fixture()
    def get_deployment_info(self):
        print("reading yaml file")
        inputfile = "/root/kube_client/testdata/input.yaml"
        kind = ReadYAML.read_yaml(self,inputfile,["kind"])
        name = ReadYAML.read_yaml(self,inputfile,["metadata","name"])
        namespace1 = ReadYAML.read_yaml(self,inputfile,["metadata","namespace"])
        print("printing all returned values",kind,name,namespace1)
        response = PodsClient.list_namespaced_deployment(namespace=namespace1)
        response = PodsClient.list_namespaced_deployment(namespace="kube-system")
#        response = PodsClient.get_deployments_for_namespace(namespace1)
        return(response.items)

#    def test_deployment_fix(self,get_deployment_info):
#       print("testing deployment")

