# setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='esp_config_diff',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'esp-config-diff=diff.cli:main',
        ],
    },
    description='A tool for comparing esp idf sdkconfigs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='shubhamdp',
    url='https://github.com/shubhamdp/esp-config-diff',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
