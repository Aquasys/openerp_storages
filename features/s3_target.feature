Feature: Define an AWS S3 storage target
    Given I'm located in "external storage"
    In order to store non-tabular data in Amazon S3
    As a "system administrator"
    I want to define a bucket and credentials to use in the OpenERP admin interface

    Scenario: add s3 configuration
        Given I fill the field "bucket" with "openerp-storage-test"
        And I fill the field "AWS_ACCESS_KEY_ID" with "<key_id>"
        And I fill the field "AWS_SECRET_ACCESS_KEY" with "<secret_key>"
        When I click on link "Save"
        Then I can read "Your configuration has been saved"

    Scenario: Test connection success
        Given I complete scenario "add s3 configuration"
        When I click on link "Test Connection"
        Then I can read "Connection Successful to bucket"

    Scenario: Test connection fail
        Given I complete scenario "add s3 configuration"
        When I click on lnk "Test Connection"
        Then I can read "Connection unsuccessful, Credential are invalid"

    Examples:
        | key_id               | secret_key                               |
        | AKIAJRZJLHNEGIQI6QNQ | xaGmFLK7SCq5+M6VvcXOuh3qtF40bz0av2G/fnuJ |
        | bad_key_id           | bad_secret_key                           |
