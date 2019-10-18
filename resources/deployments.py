from api.deployment_client import DeploymentClient

class Deployments:


    def get_deployments_for_ns_in_yaml(self):
        ret = DeploymentClient().get_pods_for_namespace()
