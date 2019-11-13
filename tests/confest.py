import pytest
from kubernetes import client

class manifest_fixtures:
    

    @pytest.fixture()
    def manifest_dir():
        """Get the path to the test manifest directory."""
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
    
    @pytest.fixture()
    def simple_deployment(self, manifest_dir):
        """Test loading the simple deployment successfully."""
        obj = manifest.load_type(
            client.V1Deployment,
            os.path.join(manifest_dir, 'simple-deployment.yaml')
        )
        return obj

    @pytest.fixture()
    def read_dictionary(self,simple_deployment,key_items):
        for key in simple_deployment.keys():
           ret = docs
           if(key == key_items[0]):
               print("printing value for given key",key_items[0])
               for key_item in key_items:
                   ret = ret[key_item]
                   print(ret)
               return(ret)

