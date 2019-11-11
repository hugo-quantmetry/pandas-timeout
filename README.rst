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


Basic usage : Raise a TimeOut Error
-----------------------------------

* Define a pandas DataFrame

.. code-block:: python

    df = pd.DataFrame({'number': [1, 0.5, 0.2, 2, 0.3]}, index=[0, 2, 4, 6, 8])

+-------+--------+
| Index | Number |
+=======+========+
|   0   |    1   |
+-------+--------+
|   2   |   0.5  |
+-------+--------+
|   4   |  0.2   |
+-------+--------+
|   6   |    2   |
+-------+--------+
|   8   |   0.3  |
+-------+--------+

* Define a function to apply on the DataFrame and set the timeout value

.. code-block:: python

   @timeout(4)
    def sleep_and_triple(row):
        number_ = row['number']

        time.sleep(number_)

        return number_ * 3

This function first sleeps for ``number`` seconds and then returns the triple of the input value.
Since the highest number is 2, a timeout value of 4 should not trigger a TimeOut error.

* Apply function on DataFrame


.. code-block:: python

    df['result'] = df.apply(sleep_and_halve, axis=1)
    print(df)


+-------+--------+--------+
| Index | Number | Result |
+=======+========+========+
|   0   |    1   |    3   |
+-------+--------+--------+
|   2   |   0.5  |   1.5  |
+-------+--------+--------+
|   4   |  0.2   |  0.6   |
+-------+--------+--------+
|   6   |    2   |    6   |
+-------+--------+--------+
|   8   |   0.3  |   0.9  |
+-------+--------+--------+

* Change the timeout value to 1.7 seconds and re-apply function on DataFrame

.. code-block:: python

    @timeout(1.7)
    def sleep_and_triple(row):
        number_ = row['number']

        time.sleep(number_)

        return number_ * 3

    df['result'] = df.apply(sleep_and_halve, axis=1)
    print(df)

The following TimeOut error is triggered:

>>> "TimeoutError: ('Time expired', 'occurred at index 6')"

The row index (pandes ``.loc``) of the row triggering the TimeOut error is given in the error message.




Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
