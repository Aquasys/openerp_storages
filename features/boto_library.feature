Feature: Leverage existing libraries for S3
    In order to build on a common framework
    I want to make all calls to AWS through boto

    Scenario: Establish connection to s3 using boto
        Given I fill the field "AWS_ACCESS_KEY_ID" with "<AWS_ACCESS_KEY_ID>" in configuration
        And I fill the field "AWS_SECRET_ACCESS_KEY" with "<AWS_SECRET_ACCESS_KEY>" in configuration
        Then I get s3 connection instance

    Scenario: Write file to bucket
        Given I upload the file "<filename>" in the field "attachment" with "<file>"
        Then I can read file on AWS S3

    Scenario: Read file from bucket
        Given I click on link of the field "attachment"
        When Server reads a file from S3
        Then I can read file

    Scenario: Delete file from bucket
        Given I click on button "Clear" of the field "attachment"
        When I click on button "Save"
        Then I get file deleted from the bucket "<bucket>"

    Scenario: Delete record from bucket
        Given I select record contains the field "attachment" in ERP
        When I click on button "Delete"
        Then I get file deleted from the bucket "<bucket>"