Feature: Define storage target
    In order to minimize database bloat
    As a "system administrator"
    I want to define a external location for non-tablular data

    Scenario: Store FTP connection information
        Given I fill the field "host" with "<host>"
        And I fill the field "port" with "<port>"
        And I the field "username" with "<username>"
        And I the field "password" with "<password">
        When I click on button "save"
        Then I can read "my information is save"

    Scenario: Test success connection
        Given I access url "/"
        And I click on button "test connection"
        When Server sends a 200 response
        Then I can read "ftp connection successfull"

    Scenario: Test connection error
        Given I access url "/"
        And I click on button "test connection"
        When Server sends a 404 response
        Then I can read "ftp connection unsuccesfull"