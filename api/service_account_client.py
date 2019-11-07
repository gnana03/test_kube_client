from api.base import BaseClass
from kubernetes import client


class ServiceAccountClient:

    def get_sa_for_all_namespaces(self):
        return client.CoreV1Api().list_service_account_for_all_namespaces(watch=False)

    def get_sa_for_all_namespaces_with_http_info(self):
        return client.CoreV1Api().list_service_account_for_all_namespaces_with_http_info(watch=False)
