Feature: Leverage existing libraries for S3
    In order to build on a common framework
    I want to make all calls to AWS through boto

    Scenario: Establish connection to s3 using boto
	Given I fill the AWS_ACCESS_KEY_ID in the AWS_ACCESS_KEY_ID "<AWS_ACCESS_KEY_ID>"
	And I fill the AWS_SECRET_ACCESS_KEY in the AWS_SECRET_ACCESS_KEY "<AWS_SECRET_ACCESS_KEY>"
	Then I get s3 connection instance

    Scenario: Get bucket
	Given I fill the bucket in the bucket "<bucket>"
	Then I get bucket instance

    Scenario: Write file to bucket
	Given I upload file to file "<filename>" ERP
	Then I get file on AWS S3

    Scenario: Read file from bucket
	Given the file "<filename>" exists in the bucket "<bucket>"
	And referance of file "<filename>" in ERP
	When I open file "<filename>" in ERP
	Then I get file from the bucket "<bucket>"

    Scenario: Delete file from bucket
	Given I delete file "<filename>" in  ERP
	When I save changes
	Then I get file deleted from the bucket "<bucket>"

    Scenario: Delete record from bucket
	Given I delete record contains file "<filename>" in ERP
	Then I get file deleted from the bucket "<bucket>"
