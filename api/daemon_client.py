from api.base import BaseClass
from kubernetes import client


class DaemonClient:

    def get_daemons_for_all_namespaces(self):
        return client.CoreV1Api().list_daemon_set_for_all_namespaceswatch=False)

    def get_pods_for_all_namespaces_with_http_info(self):
        return client.CoreV1Api().list_daemon_set_for_all_namespaces_with_http_info(watch=False)
