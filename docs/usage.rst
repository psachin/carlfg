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

this will create an image(``myImage.png``) in working directory

for graphical frontend, open the terminal and type::

  clebg


cg
----

Calculate sum of all natural numbers from 1 to n using Carl Friedrich
Guass[1777-1855, Germany] algo

Typical usage::

  #!/usr/bin/env python
  
  from cg import german
  print german.sum(999)


Installation
------------

Install using PyPI::

  pip install carlfg

to uninstall::
  
  pip uninstall carlfg

source code at `github.com/psachin/carlfg
<https://github.com/psachin/carlfg>`_



