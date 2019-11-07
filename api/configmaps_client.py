from api.base import BaseClass
from kubernetes import client


class ConfigMaps_client:
    BaseClass()
    v1 = client.CoreV1Api()

    def __get__config_maps_for_all_namespaces__(self):
        return v1.list_config_map_for_all_namespaces(watch=False)

    def __get__config_maps_for_all_namespaces_with_http_info__(self, namepace):
        return v1.list_config_map_for_all_namespaces_with_http_info(watch=False)

    def __get__config_maps_for_namespace__(self, namepace):
        return v1.list_namespaced_config_map(namepace,watch=False)

    def _get___namespaced_config_map_with_http_info__(self, namespace):
        return v1.list_namespaced_config_map_with_http_info(namespace,watch=False)
