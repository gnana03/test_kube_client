from setuptools import setup, find_packages  # noqa
from os import path

this_directory = path.abspath(path.dirname(__file__))
long_description = None
try:
    with open(path.join(this_directory, 'README.md'), 'rb') as f:
        long_description = f.read().decode('utf-8')
except IOError:
    long_description = 'Unified Automation Testing Framework'

setup(
    name='test_kube_client',
    version='0.0.1',
    description='Test Automation Framework',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/',
    platforms=["Windows", "Linux", "Unix", "Mac OS-X"],
    author='Gnana',
    author_email='gnana.kilambhi@gmail.com',
    maintainer='Gnana',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Internet",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Testing :: Acceptance",
        "Topic :: Utilities",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=[
        'pip',
        'setuptools',
        'scikit-image',
        'selenium',
        'nose',
        'flake8',
        'jsondiff',
        'pandas',
        'pytest>=3.8.2',
        'pytest-html>=1.19.0',
        'requests>=2.19.1',
        'pytest>=4.0.2',
        'pytest-html<1.21.0',
        'kubernetes',
        'kubetest'
    ], )
print("\n*** Kube client Package Installation Complete! ***\n")
