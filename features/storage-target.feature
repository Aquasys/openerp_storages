Feature: Define storage target
    In order to minimize database bloat
    As a "system administrator"
    I want to define a external location for non-tablular data.

    Scenario: Store FTP connection information
	Given I fill the host in the host "<host>"
	And I fill the port in the port "<port>"
	And I fill username in the username "<username>"
	And I fill password in the password "<password">
	When I save the data
	Then I see that my information is saved
	    | Field    | Value        |
	    | host     | "<host>"     |
	    | port     | "<port>"     |
	    | username | "<username>" |
	    | password | ************ |

    Scenario: Test success connection
	Given I have the test ftp connection button
	When I click the test ftp connection
	Then I get the success message: "ftp connection successfull"
  
    Scenario: Test connection error
	Given I have the test ftp connection button
	When I click the test ftp connection
	Then I get the error: "ftp connection unsuccesfull"	
