from setuptools import setup

setup (
    name='snapshotalyzer-30000',
    version='0.1',
    author='Vitalij',
    author_email='vmostowoj@gmail.com',
    summary='Tool to manage AWS EC2 snapshots',
    license='GPLv3+',
    packages=['shotty'],
    url='https://github.com/vmostowoj/snapshotalyzer-30000',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
