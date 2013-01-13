from setuptools import setup

setup(name='carlfg',
      version='0.2',
      description='find CG coefficients,find the sum of all natural numbers from 1 to n',
      url='https://github.com/psachin/carlfg',
      author='sachin',
      author_email='isachin@iitb.ac.in',
      license='LICENSE.rst',
      packages=['cg'],
      scripts=['bin/cg','bin/clebg'],
      long_description=open('README').read(),
#      install_requires=["python >= 2.7.3",
#                        ],
      zip_safe=False)
