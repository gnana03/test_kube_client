from kubernetes import config,client
import sys


class KubeApi:

    def __init__(self):
        """ Kube config file should be placed in /root/.kube folder with config as name for linux """
        self.configuration = client.Configuration()
        config.load_kube_config()

    def coreV1Api(self):
        """  This returns the core v1 api object"""
        return client.CoreV1Api()

    def extension_v1beta1_api(self):
        """  This returns the Extension v1 beta Api object"""
        return client.ExtensionsV1beta1Api()
