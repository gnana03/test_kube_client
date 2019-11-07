from api.base import BaseClass
from kubernetes import client


class SecretsClient:

    def get_secret_for_all_namespaces(self):
        return client.CoreV1Api().list_secret_for_all_namespaces(watch=False)

    def get_secret_for_all_namespaces_with_http_info(self):
        BaseClass().load_config()
        return client.CoreV1Api().list_secret_for_all_namespaces_with_http_info(watch=False)
