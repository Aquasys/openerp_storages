Feature: Leverage existing libraries for S3
	In order to build on a common framework
	I want to make all calls to AWS through boto

	Scenario: Establish connection to s3 using boto
		Given I fill the field "AWS_ACCESS_KEY_ID" with "<AWS_ACCESS_KEY_ID>"
		And I fill the field "AWS_SECRET_ACCESS_KEY" with "<AWS_SECRET_ACCESS_KEY>"
		Then I get s3 connection instance

	Scenario: Write file to bucket
		Given I upload the file "<filename>" in the field "attachment" with "<file>"
		Then I get file on AWS S3

	Scenario: Read file from bucket
		Given I click on "save" of the field "attachment"
		When Server reads a file from S3
		Then I get file

	Scenario: Delete file from bucket
		Given I click on "clear" of the field "attachment"
		When I click on "save"
		Then I get file deleted from the bucket "<bucket>"

	Scenario: Delete record from bucket
		Given I select record contains the field "attachmetn" in ERP
		When I click on "delete"
		Then I get file deleted from the bucket "<bucket>"
