from api.base import KubeApi
from api.pod_client import PodsClient
import yaml

from yaml.read_yaml import ReadYAML


class TestPods(KubeApi):

    def get_pods_for_ns_in_yaml(self, namespace):
        print("started")
        ret = PodsClient().get_pods_for_all_namespaces()
        result_list = ret.items()
        with open(r'.\\test-output\pods.yml', 'w') as outfile:
            yaml.dump(result_list, outfile, default_flow_style=False)
        print("completed")

    def get_pods_replicas(self,namespace):
        ret = PodsClient().get_pods_for_namespace(namespace)
        result_list = ret.items()
        with open(r'.\\test-output\pods_details.yml', 'w') as outfile:
            yaml.dump(result_list, outfile, default_flow_style=False)
        print("completed")
        return ReadYAML().read_yaml('.\\test-output\pods_details.yml','Replicas')







