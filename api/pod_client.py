from api.base import KubeApi
from kubernetes import client


class PodsClient(KubeApi):

    def get_pods_for_all_namespaces(self):
        return PodsClient().coreV1Api.list_pod_for_all_namespaces(watch=False)

    def get_pods_for_all_namespaces_with_http_info(self):
        return PodsClient().coreV1Api.list_pod_for_all_namespaces_with_http_info(watch=False)

    def get_pods_for_namespace(self, namepace):
        return PodsClient().coreV1Api.list_namespaced_pod(namepace, watch=False)

    def get_namespaced_pods_with_http_info(self, namespace):
        return PodsClient().coreV1Api.list_namespaced_pod_with_http_info(namespace, watch=False)
