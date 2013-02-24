Feature: Detect broken links and orphans
	In order to maintain relative referential integrity
	As a "system administrator"
	I want to be able to generate a report of broken references and orphaned files.

	Scenario: Report of broken pipe files.
		Given I click "generate report"
		When Server sends files which are not find on external storage
		Then I get status in the field "status" with "broken pipe"

	Scenario: Report of orphaned files
		Given I click "generate report"
		When Server sends files which are not related to ERP attachment
		Then I get status in the field "status" with "orphan"

	Examples:
		| filename   | bucket        | sha1                                     | Status      |
		| README.pdf | test_bucket   | f3a19af4e89ca0994571191ed4a0550a087ca8d2 | broken pipe |
		| test.png   | test_bucket   | 3b6c7861e55c86cf077db883704017482e5f1fcb | orphan      |
