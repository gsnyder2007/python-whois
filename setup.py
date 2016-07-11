from setuptools import setup

setup(name='pythonwhois',
      version='2.5.0',
      description='Module for retrieving and parsing the WHOIS data for a domain. Supports most domains. Modified from Sven Slootwegs versionto support use of a proxy and whois server cache',
      author='Sven Slootweg',
      author_email='gsnyder@opsecsecurity.com',
      url='http://cryto.net/pythonwhois',
      packages=['pythonwhois'],
      package_dir={"pythonwhois":"pythonwhois"},
      package_data={"pythonwhois":["*.dat"]},
      install_requires=['argparse'],
      provides=['pythonwhois'],
      scripts=["pwhois"],
      license="WTFPL"
     )
