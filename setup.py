from setuptools import setup, find_packages
from pkg_resources import parse_requirements

with open("requirements.txt", "r") as inst_reqs:
    install_requires = [str(req) for req in parse_requirements(inst_reqs)]

with open("requirements_test.txt", "r") as test_reqs:
    test_requires = [str(req) for req in parse_requirements(test_reqs)]

packages = find_packages(include=["simple_dir_watcher", "simple_dir_watcher.*"])


setup(
    name="simple_dir_watcher",
    version="0.1.0.dev0",
    license="LICENSE.TXT",
    author="Ettore Galli",
    description="Simple directory watcher",
    long_description=__doc__,
    packages=packages,
    install_requires=install_requires,
    test_requires=test_requires,
    python_requires=">=3.8",
    include_package_data=True
)