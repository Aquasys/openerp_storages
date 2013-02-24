Feature: Pluggable architecture
	In order to provide a flexible solution that can support mulitple storage types and services
	I want to provide an abstract model upon which concrete implementation can be built.

	Scenario: Store AWS S3 information
		Given I fill AWS S3 information
		And I fill the field "store" with "s3"
		When I upload the file "<filename>" in the field "attachment" with "<file>"
		Then I get files on AWS S3

	Scenario: Store FTP information
		Given I fill ftp credentials
		And I fill the field "store" with "ftp"
		When I upload the file "<filename>" in the field "attachment" with "<file>"
		Then i get files on FTP
