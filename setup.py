from setuptools import find_packages, setup


setup(
    name="miniwob",
    license="Apache 2.0",
    packages=find_packages(where="python", exclude=["test"]),
    package_dir={"": "python"},
    version="0.0.1",
    install_requires=["Pillow>=4.0", "selenium>=3.4.3"],
)
