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
        print("test starts now")
        DEPLOYMENT_NAME = "nginx-deployment"
        crud_deployment(self,DEPLOYMENT_NAME)

    def test_pod_replicas(self,pod_replicas):
        DEPLOYMENT_NAME = "nginx-deployment"
        replicas = pod_replicas(self,DEPLOYMENT_NAME,"default")
        print("**************verifying replicas****************")
        assert replicas==3


