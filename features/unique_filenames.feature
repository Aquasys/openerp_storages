Feature: Unique file names
	In order to eliminate file name collisions
	I want the system to rename all new files to the hash value of the file

	Scenario: Uploaded file get renamed to its hash value
		Given I upload the file "<filename>" in the bucket "<bucket>"
		Then the remote file has been renamed to "<sha512>"

	Scenario: Existing file in the bucket is not uploaded again
		Given the file "<filename>" exists in the bucket "<bucket>"
		When I upload the file "<filename" in the bucket "<bucket>"
		Then I get an error "This file already exists, not uploading"

	Examples:
		| filename   | bucket        | sha1                                     |
		| README.pdf | test_bucket   | f3a19af4e89ca0994571191ed4a0550a087ca8d2 |
		| test.png   | test_bucket   | 3b6c7861e55c86cf077db883704017482e5f1fcb |
