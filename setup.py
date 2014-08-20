from setuptools import setup

setup(name='carlfg',
      version='0.32',
      description='Find Clebsch-Gordan coefficients',
      url='https://github.com/psachin/carlfg',
      author='Sachin',
      author_email='isachin@iitb.ac.in',
      license=open('LICENSE.rst').read(),
      packages=['cg'],
      scripts=['bin/cg','bin/clebg'],
      long_description=open('README.rst').read(),
      keywords=['cg','clebg','pypi','coefficients','clebsch gordan','gcd'],
      install_requires=["wx",
                        ],
      zip_safe=False)
