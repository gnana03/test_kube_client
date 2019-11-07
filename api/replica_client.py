from api.base import BaseClass
from kubernetes import client


class ReplicaClient:

    def get_rc_for_all_namespaces(self):
        return client.CoreV1Api().list_replication_controller_for_all_namespaces(watch=False)

    def get_rc_for_all_namespaces_with_http_info(self):
        return client.CoreV1Api().ist_replication_controller_for_all_namespaces_with_http_info(watch=False)
