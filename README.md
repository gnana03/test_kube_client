# Testing Kube Client API
    This uses Kube Client API to test Kubernetes resources

##  Installation
**From source :** 

git clone --recursive https://github.com/gnana03/test_kube_client.git

cd test_kube_client

python setup.py install

**From PyPi directly :**

pip install setup.py

## Key Features :
      This module tests the various kubernetes API resources such as Deployments, Pods, ConfigMaps, Secrets, namespaces, replicasets
    
## Pre-requisites

The framework requires
- [python 2.7+ / 3.6+](https://www.python.org/downloads/)
- [pip](pip )
- [pytest](https://docs.pytest.org/en/latest/getting-started.html) to be installed in the machine.
- kubernetes cluster or kube config file

## Running the tests

The sample tests for deploments are placed in **test_kube_client --> tests** folder. To run the sample tests, open command prompt/terminal, go to test_kube_client --> tests folder and run the following command:

`pytest {filename}.py -s` (-s indicates the standard output, please refer [here](https://docs.pytest.org/en/latest/contents.html) for a detailed understanding around pytest framework and its features/plugins/options etc.)
