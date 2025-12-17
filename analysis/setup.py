from setuptools import setup, find_packages

setup(
    name="ktu_rocket_analysis",
    version="1.0.0",
    description="KTU Gokcen Rocket Team Engineering Analysis Tools",
    author="KTU Gokcen Rocket Team",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
        "pandas",
    ],
)
