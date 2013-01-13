from setuptools import setup

setup(name='cfg',
      version='0.1',
      description='find the sum of all natural numbers from 1 to n',
      url='https://gitlab.com/cfg',
      author='sachin',
      author_email='isachin@iitb.ac.in',
      license='LICENSE.rst',
      packages=['cg'],
      scripts=['bin/cg'],
      long_description=open('README.rst').read(),
#      install_requires=["python >= 2.7.3",
#                        ],
      zip_safe=False)
