Feature: Import functionality
    In order to allow data owners to migrate non-tablular data into the database
    As a "system administrator"
    I want to be able to easily import existing non-tablular data from an external storage location.

    Scenario: Import attachments from S3
	Given I select import architecture type in the import "S3"
	When I click on import
	Then I get attachments in ERP 
	And I get one record for each file.
	
    Scenario: Import attachments from ftp
	Given I select import architecture type in the import "FTP"
	When I click on import
	Then I get attachments in ERP 
	And I get one record for each file.
