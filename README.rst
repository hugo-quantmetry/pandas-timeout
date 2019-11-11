=========
pdtimeout
=========


.. image:: https://img.shields.io/pypi/v/pdtimeout.svg
        :target: https://pypi.python.org/pypi/pdtimeout

.. image:: https://img.shields.io/travis/hugo-quantmetry/pdtimeout.svg
        :target: https://travis-ci.org/hugo-quantmetry/pdtimeout

.. image:: https://readthedocs.org/projects/pdtimeout/badge/?version=latest
        :target: https://pdtimeout.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Generate TimeOut errors with pandas.apply


* Free software: Apache Software License 2.0
* Documentation: https://pdtimeout.readthedocs.io.


Features
--------


* Define a pandas DataFrame

.. code-block:: python

    df = pd.DataFrame({'number': [1, 0.5, 0.2, 2, 0.3]})

+------------+------------+
|   Index    |   Number   |
+============+============+
| body row 1 | column 2   |
+------------+------------+
| body row 2 | Cells may  |
+------------+------------+



* TODO

.. code-block:: python

   @timeout(1.5)
    def sleep_and_triple(row):
        number_ = row['number']

        time.sleep(number_)

        return number_ * 3

Blah

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
