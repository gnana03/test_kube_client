"""
Creates, updates, and deletes a deployment using AppsV1Api.
"""
import os

import pytest
from kubernetes import client, config
from all_fixtures.deployment_fixtures import DeploymentFixtures
from api.deployment_client import DeploymentClient

class TestCases(DeploymentFixtures):

   # @pytest.mark.parametrize('crud_deployment',"nginx-deployment", indirect=True)
    def test_deployment_crud(self,crud_deployment):
        # Configs can be set in Configuration class directly or using helper
        # utility. If no argument provided, the config will be loaded from
        # default location.
#       config.load_kube_config()
#       apps_v1 = client.AppsV1Api()
        # Create a deployment object with client-python API. The deployment we
        # created is same as the `nginx-deployment.yaml` in the /examples folder.
#        deployment = simple_deployment
#
#        create_deployment deployment)

#        update_deployment(apps_v1, deployment)

        #delete_deployment("nginx-deployment")
        print("test starts now")
        DEPLOYMENT_NAME = "nginx-deployment"
        crud_deployment(self,DEPLOYMENT_NAME)

    def test_pod_replicas(self,pod_replicas):
        DEPLOYMENT_NAME = "nginx-deployment"
        replicas = pod_replicas(self,DEPLOYMENT_NAME,"default")
        print("**************verifying replicas****************")
        assert replicas==3


