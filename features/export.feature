Feature: Export functionality
    In order to allow data owners to migrate non-tablular data out of the database
    As a "system administrator"
    I want to be able to easily export existing non-tablular data to an external storage location.

    Scenario: Export attachments with remain file in database
        Given I select attachments from list
        And I check the field "Store in Databse" with "T"
        When I click on button "export"
        Then I can read attachments in AWS S3
        And I can read attachments in databse

    Scenario: Export attachments
        Given I select attachments from list
        And I uncheck the field "Store in Databse" with "F"
        When I click on button "export"
        Then I can read attachments in AWS S3
        And I can read no attachments in databse

    Examples:
        | model         | attachment      | Store in Databse |
        | purchase      | PO0056.pdf      | F                |
        | warehouse     | OUT/0058.pdf    | T                |
        | purchase      | DT-00673.doc    | F                |