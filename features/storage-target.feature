Feature: Define storage target
	In order to minimize database bloat
	As a "system administrator"
	I want to define a external location for non-tablular data

	Scenario: Store FTP connection information
		Given I fill the field "host" with "<host>"
		And I fill the field "port" with "<port>"
		And I the field "username" with "<username>"
		And I the field "password" with "<password">
		When I click on "save"
		Then I see that my information is save

	Scenario: Test success connection
		Given I access url "/"
		And I click on "test connection"
		When Server sends a 200 response
		Then I get the success message:"ftp connection successfull"

	Scenario: Test connection error
		Given I access url "/"
		And I click on "test connection"
		When Server sends a 404 response
		Then I get the error message:"ftp connection unsuccesfull"
