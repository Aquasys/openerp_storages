Feature: Define an AWS S3 storage target
    In order to store non-tabluar data in Amazon S3
    As a "system administrator"
    I want to define a bucket and credentials to use in the OpenERP admin interface

    Scenario: Store connection information to external storage s3
	Given I fill the url in the url "<url>"
	And I fill the bucket in the bucket "<bucket>"
	And I fill the AWS_ACCESS_KEY_ID in the AWS_ACCESS_KEY_ID "<AWS_ACCESS_KEY_ID>"
	And I fill the AWS_SECRET_ACCESS_KEY in the AWS_SECRET_ACCESS_KEY "<AWS_SECRET_ACCESS_KEY>"
	When I save the data
	Then I see that my information is saved
	    | Field | Value |
	    | url | "<url>" |
	    | bucket | "<bucket>" |
	    | AWS_ACCESS_KEY_ID | "<AWS_ACCESS_KEY_ID>" |
	    | AWS_SECRET_ACCESS_KEY | ************ |
    
    Scenario: Test success connection
	Given I have the test connection button
	When I click the test connection
	Then I get the success message: "connection successfull to bucket"
  
    Scenario: Test connection error
	Given I have the test connection button
	When I click the test connection
	Then I get the error: "connection unsuccesfull, credentil are invalid"
