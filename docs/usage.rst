======
clarfg
======

clebg
-----
Calculate Clebsch–Gordan coefficients

Typical usage::

  #!/usr/bin/env python

  from cg import ClebschGordan
  ClebschGordan.execute('myImage.png',0.5,0.5,'Default','Default')

this should create an image with the name ``myImage.png`` in working directory

For graphical frontend, open the terminal and type::

  clebg


Additional modules
------------------

cg
~~~~
Calculate sum of all natural numbers from 1 to n using Carl Friedrich
Guass[1777-1855, Germany] algorithm.

Typical usage::

  #!/usr/bin/env python

  from cg import german
  print german.sum(999)


gcd
~~~
To find GCD/GCF of two numbers by Euclid’s GCD algorithm.

Typical usage::

  #!/usr/bin/env python

  from cg import german
  print german.gcd(999, 56)


Installation
------------

Install using PyPI::

  pip install carlfg

To uninstall::

  pip uninstall carlfg

Source code at `github.com/psachin/carlfg <https://github.com/psachin/carlfg>`_
