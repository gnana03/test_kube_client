import yaml

from api.pod_client import PodsClient


def test_get_pods_for_ns_in_yaml(self, namespace):
    print("started")
    ret = PodsClient().get_pods_for_all_namespaces()
    result_list = ret.items()
    with open(r'.\\test-output\pods.yml', 'w') as outfile:
        yaml.dump(result_list, outfile, default_flow_style=False)
    print("completed")
