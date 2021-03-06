from setuptools import setup

dependencies = [
    'natsort',
    'pyyaml',
    'swsssdk>=2.0.1',
]

high_performance_deps = [
    'swsssdk[high_perf]>=2.0.1',
]

setup(
    name='sonic-py-common',
    version='1.0',
    description='Common Python libraries for SONiC',
    license='Apache 2.0',
    author='SONiC Team',
    author_email='linuxnetdev@microsoft.com',
    url='https://github.com/Azure/SONiC',
    maintainer='Joe LeVeque',
    maintainer_email='jolevequ@microsoft.com',
    install_requires=dependencies,
    extras_require={
        'high_perf': high_performance_deps,
    },
    packages=[
        'sonic_py_common',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python',
    ],
    keywords='SONiC sonic PYTHON python COMMON common',
)

