from api.base import KubeApi
from kubernetes import client


class DeploymentClient(KubeApi):

    def get_deployments_for_all_namespaces(self, extension_v1beta1_api=None):
        return extension_v1beta1_api.list_deployment_for_all_namespaces(watch=False)

    def get_deployments_for_all_namespaces_with_http_info(self, extension_v1beta1_api=None):
        return extension_v1beta1_api.list_deployment_for_all_namespaces_with_http_info(watch=False)

    def get_deployments_for_namespace(self, namepace, extension_v1beta1_api=None):
        return extension_v1beta1_api.list_namespaced_deployment(namepace, watch=False)

    def get_namespaced_deployments_with_http_info(self, namespace, extension_v1beta1_api=None):
        return extension_v1beta1_api.list_namespaced_deployment_with_http_info(namespace, watch=False)
