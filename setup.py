from setuptools import setup

setup(
    name='pubsub-tools',
    version='1.0',
    packages=[''],
    install_requires=[
        'google-cloud-pubsub',
    ],
    entry_points={
        'console_scripts': [
            'consume = consume:main',
            'publish = publish:main',
        ],
    },
)

