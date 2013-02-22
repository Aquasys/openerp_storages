Feature: Pluggable architecture
    In order to provide a flexible solution that can support mulitple storage types and services
    I want to provide an abstract model upon which concrete implementation can be built.

    Scenario: Store AWS S3 information
	Given I fill S3 information
	And I fill store type in the store "s3"
	When I upload file to ERP
	Then I get files on AWS S3

    Scenario: Store FTP information
	Given I fill ftp credentials
	And I fill store type in the store "ftp"
	When I upload file to ERP
	Then i get files on FTP 
