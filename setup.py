from setuptools import find_packages, setup

version = '0.1.0-alpha.4'

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
    url='https://github.com/wangwenpei/kaptain',
    download_url='https://github.com/wangwenpei/kaptain/tarball/master',
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
            'kap = kaptain.main:cli'
        ]
    },
)
