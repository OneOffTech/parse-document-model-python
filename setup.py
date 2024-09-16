from codecs import open
from os import path

from setuptools import setup

ROOT = path.abspath(path.dirname(__file__))

with open(path.join(ROOT, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='document-model-python',
    version='0.1.0',
    description='Define the pydantic models for a text document.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='OneOffTech',
    author_email='info@oneofftech.de',
    license='MIT',
    url='https://github.com/OneOffTech/document-model-python',
    project_urls={
        'Source': 'https://github.com/OneOffTech/document-model-python',
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Operating System :: OS Independent'
    ],
    packages=['document_model_python'],
    include_package_data=True,
    install_requires=['pydantic']
)
