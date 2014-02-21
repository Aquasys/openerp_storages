Feature: Import functionality
    In order to allow data owners to migrate non-tablular data into the database
    As a "system administrator"
    I want to be able to easily import existing non-tablular data from an external storage location.

    Scenario: Import attachments from S3
        Given I fill the field "storage type" with "S3"
        When I click on button "import"
        Then I can read attachments in ERP

    Scenario: Import attachments from ftp
        Given I fill the field "storage type" with "FTP"
        When I click on button "import"
        Then I can read attachments in ERP