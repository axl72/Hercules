from setuptools import setup, find_packages

setup(
    name="hercules",
    version="0.1",
    packages=find_packages(
        include=["assets", "components", "config", "core", "services"]
    ),
    install_requires=[
        # Aquí puedes agregar dependencias adicionales si las tienes
    ],
    author_email="axell.bernabel72@gmail.com",
)
