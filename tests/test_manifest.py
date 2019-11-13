"""Unit tests for the kubetest.manifest package."""

import os

import pytest
import yaml
from kubernetes import client

from kubetest import manifest


class TestCastValue:
    """Tests for kubetest.manifest.cast_value"""

    @pytest.mark.parametrize(
        'value,t,expected', [
            # builtin types
            (11, 'int', int(11)),
            ('11', 'int', int(11)),
            (11.0, 'int', int(11)),
            (11, 'float', float(11)),
            (11, 'str', '11'),

            # casting to object should result in no change
            (11, 'object', 11),
            ('11', 'object', '11'),

            # kubernetes types
            (
                {'apiVersion': 'apps/v1', 'kind': 'Namespace'},
                'V1Namespace',
                client.V1Namespace(kind='Namespace', api_version='apps/v1')),
            (
                {'fieldRef': {'apiVersion': 'apps/v1beta1', 'fieldPath': 'foobar'}},
                'V1EnvVarSource',
                client.V1EnvVarSource(field_ref=client.V1ObjectFieldSelector(
                    api_version='apps/v1beta1', field_path='foobar'
                ))),
            (
                {'finalizers': ['a', 'b', 'c']},
                'V1ObjectMeta',
                client.V1ObjectMeta(finalizers=['a', 'b', 'c'])),
        ]
    )
    def test_ok(self, value, t, expected):
        """Test casting values to the specified type successfully."""

        actual = manifest.cast_value(value, t)
        assert type(actual) == type(expected)
        assert actual == expected

class TestLoadType:
    """Tests for kubetest.manifest.load_type"""

    def test_simple_deployment_ok(self, manifest_dir, simple_deployment):
        """Test loading the simple deployment successfully."""
        obj = manifest.load_type(
            client.V1Deployment,
            os.path.join(manifest_dir, 'simple-deployment.yaml')
        )
        assert obj == simple_deployment

