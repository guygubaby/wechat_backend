from setuptools import setup,find_packages


setup(
    name='cxk flask app',
    version='1.0',
    long_description='''xixixi yingyingying''',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'beautifulsoup4==4.7.1',
        'Flask==1.0.2',
        'gevent==1.4.0',
        'gunicorn==19.9.0',
        'pymongo==3.8.0',
        'requests==2.21.0'
    ]
)