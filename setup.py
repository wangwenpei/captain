from setuptools import find_packages, setup

version = '0.1.0-alpha.1'

deps = {
    'captain': [
        'click'
    ],

    'test': [
        'pytest'
    ],
    'dev': []
}

deps['dev'] = (
        deps['dev'] +
        deps['test'] +
        deps['captain']
)

install_requires = deps['captain']

setup(
    name='captain-py',
    version=version,
    packages=find_packages(exclude=["tests"]),
    url='https://github.com/wangwenpei/captain',
    download_url='https://github.com/wangwenpei/captain/tarball/master',
    license='MIT',
    author='WANG WENPEI',
    install_requires=install_requires,
    extras_require=deps,
    zip_safe=False,
    test_suite="tests",
    author_email='stormxx@1024.engineer',
    description='A modern deploy tool',
    keywords='captain,kubernetes,k8s',
    entry_points={
        'console_scripts': [
            'cap = captain.main:main'
        ]
    },
)
