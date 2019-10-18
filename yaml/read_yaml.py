import yaml

class ReadYAML:


    def read_yaml(self,path,key_item):
        with open(path) as f:
            docs = yaml.load_all(f, Loader=yaml.FullLoader)
        for doc in docs:
            for key, value in doc.items():
                if(key == key_item):
                    return value