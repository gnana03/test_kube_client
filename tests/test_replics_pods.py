import os

import pytest
import yaml
from kubernetes import client, config
from api.pod_client import PodsClient
# from fixtures.all_fixtures import Fixtures

class TestPods:
    def test_pod_replicas_deployment(self,simple_deployment):
        print("simple deployment",simple_deployment)
        key_items = ["spec","replicas"]
        for key in simple_deployment.keys():
           ret = docs
           if(key == key_items[0]):
               print("printing value for given key",key_items[0])
               for key_item in key_items:
                   ret = ret[key_item]
                   print(ret)
               return(ret)

        response = PodsClient.get_pods_for_namespace(self,'default')
        replicas = 0
        for res in response:
            print(res.metadata.name)
            if res.metadata.name == "coredns":
                print(res.spec.replicas)
                replicas = res.spec.replicas
            return replicas
    
    
