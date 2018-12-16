from setuptools import setup, find_packages

setup(
    name="leaker",
    version="0.0.1",
    description="Detect memory leaks",
    url="https://github.com/lgvaz/reward",
    author="lgvaz",
    author_email="lgvaz@lishash.com",
    packages=[package for package in find_packages() if package.startswith("leaker")],
    zip_safe=False,
)