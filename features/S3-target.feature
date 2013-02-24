Feature: Define an AWS S3 storage target
	In order to store non-tabluar data in Amazon S3
	As a "system administrator"
	I want to define a bucket and credentials to use in the OpenERP admin interface

	Scenario: Store connection information to external storage s3
		Given I fill the field "url" with "<url>"
		And I fill the field "bucket" with "<bucket>"
		And I fill the field "AWS_ACCESS_KEY_ID" with "<AWS_ACCESS_KEY_ID>"
		And I fill the field "AWS_SECRET_ACCESS_KEY" with "<AWS_SECRET_ACCESS_KEY>"
		When I click on "save"
		Then I see that my information is save
   
	Scenario: Test connection success 
		Given I access url "/"
		And I click on "test connection"
		When Server sends a 200 response
		Then I get the success message: "connection successfull to bucket"
 
	Scenario: Test connection fail
		Given I access url "/"
		And I click on "test connection"
		When Server sends a 404 response
		Then I get the error message: "connection unsuccesfull, credentil are invalid"
