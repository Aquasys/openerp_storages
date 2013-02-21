Feature: Export functionality
    In order to allow data owners to migrate non-tablular data out of the database
    As a "system administrator"
    I want to be able to easily export existing non-tablular data to an external storage location.

    Scenario: Export attachments with remain file in database
		Given I select attachments from list
		And I check checkbox "<Store in Databse>"
		When I click on export
		Then I get attachments in AWS S3
		And I get attachments in databse

    Scenario: Export attachments
		Given I select attachments from list
		And I uncheck checkbox "<Store in Databse>"
		When I click on export
		Then I get attachments in AWS S3
		And I get attachments are deleted from databse

  	Examples:
    	| model         | attachment      | Store in Databse | 
    	| purchase      | PO0056.pdf      | F                |
    	| warehouse     | OUT/0058.pdf    | T                |
    	| purchase      | DT-00673.doc    | F                |
