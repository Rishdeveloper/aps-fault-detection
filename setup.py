from setuptools import find_packages,setup


setup(
    name="sensor",
    version="0.0.2",
    author="ineuron",
    author_email="urishabh6@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),
)

