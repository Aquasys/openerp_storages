================
OpenERP Storages
================


doc
---

.. code-block:: console

    $ cd doc/
    $ mkvirtualenv -p python2.7 openerp_storages-sphinx
    (openerp_storages-sphinx)$ pip install -r requirements.txt
    (openerp_storages-sphinx)$ make html
    (openerp_storages-sphinx)$ xdg-open _build/html/index.html
