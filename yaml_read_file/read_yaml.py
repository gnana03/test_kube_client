import yaml

class ReadYAML:

    def read_yaml(self, path, key_items):
        with open(path) as f:

#            docs = yaml.load_all(f,Loader=yaml.FullLoader)

            docs = yaml.safe_load(f)
#        print("**** keys for docs****",docs.keys())
#        print("#### values for docs ####",docs.values())
        for key in docs.keys():
            ret = docs
            if(key == key_items[0]):
                print("printing value for given key",key_items[0])
                for key_item in key_items:
                    ret = ret[key_item]
                    print(ret)
                return(ret)

