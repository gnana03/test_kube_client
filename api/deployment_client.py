from api.base import KubeApi
from kubernetes import client


class DeploymentClient(KubeApi):

    def get_deployments_for_all_namespaces(self, extension_v1beta1_api=None):
        return DeploymentClient().extension_v1beta1_api.list_deployment_for_all_namespaces(watch=False)

    def get_deployments_for_all_namespaces_with_http_info(self, extension_v1beta1_api=None):
        return extension_v1beta1_api.list_deployment_for_all_namespaces_with_http_info(watch=False)

    def get_deployments_for_namespace(self, namepace, extension_v1beta1_api=None):
#        print(dir(DeploymentClient().coreV1Api))
        return DeploymentClient().apps_v1_api.list_namespaced_deployment(namepace, watch=False)

    def get_namespaced_deployments_with_http_info(self, namespace, extension_v1beta1_api=None):
        return extension_v1beta1_api.list_namespaced_deployment_with_http_info(namespace, watch=False)

    def create_deployment(self, deployment):
        # Create deployement
        api_response = DeploymentClient().apps_v1_api.create_namespaced_deployment(
                       body=deployment,
                       namespace="default")
        print("Deployment created. status='%s'" % str(api_response.status))


    def update_deployment(self,deployment_name,deployment):
        # Update container image
        deployment.spec.template.spec.containers[0].image = "nginx:1.16.0"
        # Update the deployment
        api_response = DeploymentClient().apps_v1_api.patch_namespaced_deployment(
             name=deployment_name,
             namespace="default",
             body=deployment)
        print("Deployment updated. status='%s'" % str(api_response.status))


    def delete_deployment(self,deployment_name):
        # Delete deployment
        api_response = DeploymentClient().apps_v1_api.delete_namespaced_deployment(
            name=deployment_name,
            namespace="default",
            body=client.V1DeleteOptions(
                propagation_policy='Foreground',
                grace_period_seconds=5))
        print("Deployment deleted. status='%s'" % str(api_response.status))

