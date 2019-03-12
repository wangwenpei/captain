from setuptools import find_packages, setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

version = '0.1.1'

deps = {
    'kaptain': [
        'click',
    ],
    # 'deploy': [
    #     'ansible',
    # ],
    'test': [
        'pytest',
        'flake8',
        'pytest-flake8'
    ],
    'dev': []
}

deps['dev'] = (
        deps['dev'] +
        deps['test'] +
        deps['kaptain']
)

install_requires = deps['kaptain']

setup(
    name='kaptain',
    version=version,
    packages=find_packages(exclude=["tests"]),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/wangwenpei/kaptain',
    download_url='https://github.com/wangwenpei/kaptain/tarball/master',
    license='MIT',
    author='WANG WENPEI',
    install_requires=install_requires,
    extras_require=deps,
    zip_safe=False,
    test_suite="tests",
    author_email='stormxx@1024.engineer',
    description='A modern SRE tool',
    keywords='captain,kubernetes,k8s',
    entry_points={
        'console_scripts': [
            'kap = kaptain.main:cli'
        ]
    },
)
