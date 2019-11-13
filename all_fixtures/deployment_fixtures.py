import pytest
from api.pod_client import PodsClient
from api.deployment_client import DeploymentClient
# from pytest_cases import param_fixture
from pprint import pprint

# create a single parameter fixture
class DeploymentFixtures:
 
    @pytest.fixture()    
    def crud_deployment(self,simple_deployment):
        def get_deployment_name(self,deployment_name="coredns"):
            print("crud fixture")
            deployment = simple_deployment

            DeploymentClient.create_deployment(self,deployment)

            DeploymentClient.update_deployment(self, deployment_name,deployment)
#            DeploymentClient.delete_deployment(self,deployment_name)
            return deployment_name
        return get_deployment_name

    @pytest.fixture()
    def pod_replicas(self,simple_deployment):
        def get_deployment_info(self,dep_name,namespace):
            response = DeploymentClient.get_deployments_for_namespace(self,namespace)
            pprint(response)
            #    print(model.items[0].metadata.name)
            replicas = 0
            for res in response.items:
                print(res.metadata.name)
                if res.metadata.name == dep_name:
                   print(res.spec.replicas)
                   replicas = res.spec.replicas
            return replicas
        return get_deployment_info

        
   

