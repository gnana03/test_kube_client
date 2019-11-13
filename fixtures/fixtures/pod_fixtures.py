import pytest
import os

from api.pod_client import PodsClient


class pods_fixtures(PodsClient):


    @pytest.fixture()
    def get_namespaces_pods_info(self,namespace):
        model = PodsClient.get_pods_for_namespace(namespace)
        #    print(model.items[0].metadata.name)
        return model.items
