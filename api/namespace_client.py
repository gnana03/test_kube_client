from api.base import BaseClass
from kubernetes import client


class NameSpaceClient:

    def get_namespace(self):
        return client.CoreV1Api().list_namespace(watch=False)

    def get_namespaces_with_http_info(self):
        return client.CoreV1Api().list_namespace_with_http_info(watch=False)
    
    def get_namespaced_config_map(self,namespace):
        return client.CoreV1Api().list_namespaced_config_map(watch=False,namespace)
    
    def get_namespaced_pod(self,namespace):
        return client.CoreV1Api().list_namespaced_pod(watch=False,namespace)
    
    def get_namespaced_rc(self,namespace):
        return client.CoreV1Api().list_namespaced_replication_controller(watch=False,namespace)
       
