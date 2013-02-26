Feature: Capture uploaded files and email attachments
    In order to automate external storage on non-tabular data
    As an "end user"
    I want the system to automatically upload all files and email attachments to a defined S3 bucket

    Scenario: Upload attachment files by "end user"
        Given I upload the file "<filename>" in the field "attachment" with "<file>" as "end user"
        When I click on button "Save"
        Then I can read attachment files to S3 as "system administrator"