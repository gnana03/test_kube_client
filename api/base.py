from kubernetes import config,client
import sys


class KubeApi:

    def __init__(self):
        """ Kube config file should be placed in /root/.kube folder with config as name for linux """
        self.configuration = client.Configuration()
        config.load_kube_config()
        print("Supported APIs (* is preferred version):")
        print("%-40s %s" %
          ("core", ",".join(client.CoreApi().get_api_versions().versions)))
        for api in client.ApisApi().get_api_versions().groups:
            versions = []
            for v in api.versions:
                name = ""
                if v.version == api.preferred_version.version and len(
                    api.versions) > 1:
                    name += "*"
                name += v.version
                versions.append(name)
            print("%-40s %s" % (api.name, ",".join(versions)))

    @property
    def coreV1Api(self):
        """  This returns the core v1 api object"""
        return client.CoreV1Api()

    @property
    def extension_v1beta1_api(self):
        """  This returns the Extension v1 beta Api object"""
        return client.ExtensionsV1beta1Api()
   
    @property
    def apps_v1_api(self):
        """ This returns the Apps V1 API object"""
        return client.AppsV1Api()
