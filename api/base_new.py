import os
import unittest
import urllib3

from kubernetes.client.configuration import Configuration
from kubernetes.config import kube_config

DEFAULT_E2E_HOST = '127.0.0.1'


def get_e2e_configuration():
    config = Configuration()
    config.host = '172.16.50.14'
    if os.path.exists(
            os.path.expanduser(kube_config.KUBE_CONFIG_DEFAULT_LOCATION)):
        kube_config.load_kube_config(client_configuration=config)
    else:
        print('Unable to load config from %s' %
              kube_config.KUBE_CONFIG_DEFAULT_LOCATION)
        for url in ['https://%s:8443' % DEFAULT_E2E_HOST,
                    'http://%s:8080' % DEFAULT_E2E_HOST]:
            try:
                urllib3.PoolManager().request('GET', url)
                config.host = url
                config.verify_ssl = False
                urllib3.disable_warnings()
                break
            except urllib3.exceptions.HTTPError:
                pass
    if config.host is None:
        raise unittest.SkipTest('Unable to find a running Kubernetes instance')
    print('Running test against : %s' % config.host)
    config.assert_hostname = False
    return config

if __name__ == '__main__':
    get_e2e_configuration()