from api.base import BaseClass
from kubernetes import client


class ServiceClient:

    def get_service_for_all_namespaces(self):
        return client.CoreV1Api().list_service_for_all_namespaces(watch=False)

    def get_service_for_all_namespaces_with_http_info(self):
        return client.CoreV1Api().list_service_for_all_namespaces_with_http_info(watch=False)
