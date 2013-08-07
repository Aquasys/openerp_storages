Feature: Export functionality
    Given I'm located in "Attachments"
    In order to allow data owners to migrate non-tabular data out of the database
    As a "System Administrator"
    I want to be able to easily export existing non-tabular data to an external storage location.

    Scenario: Export attachments with remaining file in database
        When I click on link "Export to S3"
        Then I can read "attachments in AWS S3"
        And I can read attachments in databse

    Examples:
        | model         | attachment      |
        | purchase      | PO0056.pdf      |
        | warehouse     | OUT/0058.pdf    |
        | purchase      | DT-00673.doc    |
