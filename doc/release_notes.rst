Release Notes
=============


v0.3.1
------
:Date: 2013/10/07

* Add sub-directories feature for s3 storage.


v0.3
----
:Date: 2013/09/13

* Create logic for unique filename in 'lookup' object of openerp,
  use same file name to store in AWS S3 bucket.
* Added functionality for deleting files; if attached files are deleted
  from openerp 'lookup' object then respective file with same name
  will be deleted from AWS S3 bucket 


v0.2
----
:Date: 2013/08/21

* When installing openerp_storages module it was giving error
  for credentials: Fixed a bug
* Fixed patch for openerp_storages in aoe repository


v0.1
----
:Date: 2013/08/07

* Create sphinx documentation
* Write initial features, scenarios and steps
