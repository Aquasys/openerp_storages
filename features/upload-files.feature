Feature: Capture uploaded files and email attachments
    In order to automate external storage on non-tabular data
    As an "end user"
    I want the system to automatically upload all files and email attachments to a defined S3 bucket.

    Scenario: Upload attachment files by "end user"
	Given I upload attachment to ERP as "end user"
	When I save data
	Then I get attachment files to S3
	And upload to S3 as a "system administrator"

    Scenario: Upload email attachment by "end user"
	Given I upload attachment to ERP Email as "end user"
	When I save data
	Then I get attachment files to S3
	And upload to S3 as a "system administrator"
