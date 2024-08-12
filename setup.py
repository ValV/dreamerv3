import pathlib
import setuptools

from os import path as osp, sep
from setuptools import find_namespace_packages


def read_requirements(path_package):
    path_requirements = osp.join(path_package, 'requirements.txt')
    if osp.isfile(path_requirements):
        with open(path_requirements) as f:
            return f.read().splitlines()
    return []

def collect_requirements(packages):
    requirements_all = set()
    for path_package in packages:
        requirements_all.update(read_requirements(path_package))
    return list(requirements_all)

# Find all packages
package_names = find_namespace_packages(exclude=['scores', 'example.py'])

# Convert package names to directory paths
package_paths = [package.replace('.', sep) for package in packages]

setuptools.setup(
    name='dreamerv3',
    version='1.5.0',
    description='Mastering Diverse Domains through World Models',
    author='Danijar Hafner',
    url='http://github.com/danijar/dreamerv3',
    long_description=pathlib.Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    packages=package_names,
    include_package_data=True,
    install_requires=collect_requirements(package_paths),
    dependency_links = [
        'https://storage.googleapis.com/jax-releases/jax_cuda_releases.html',
        'https://pypi.org/simple'
    ],
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)
