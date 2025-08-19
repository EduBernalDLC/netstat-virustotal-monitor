#!/usr/bin/env python3
from setuptools import setup

setup(
    name='netstat-virustotal-monitor',
    version='0.1',
    py_modules=['virustotal', 'dnsbl'],
    install_requires=['gevent', 'IPy', 'greenlet', 'pygeoip', 'psutil'],
    url='https://github.com/PSJoshi/netstat-virustotal-monitor',
    author='Joshi Pradyumna',
    author_email='joshi.pradyumna@gmail.com',
    license='Apache',
    description='python based network connection monitoring tool',
    keywords='network connection monitoring',
    long_description=(
        'python-based script enhances netstat command output to include city, '
        'country and ASN information using Maxmind Geolite databases. '
        'In addition, it also checks whether the remote IP is malicious '
        'using Virustotal and DNS-based Blackhole List (DNSBL) databases.'
    ),
    python_requires='>=3.9',
    platforms=['Linux', 'Windows']
)
