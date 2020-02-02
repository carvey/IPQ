# IPQ

## Setup
Setup the python environment
		
	python3 -m venv venv --system-site-packages
		
Setup the database schema
        
	flask init-db

This app currently accepts txt files in the form of

	[network id 1]/[prefix length 1]
	[network id 2]/[prefix length 2]
	[network id 3]/[prefix length 3]
	[network id 4]/[prefix length 4]
	...
	
Example:
	192.168.1.0/24
	10.1.1.0/24
	10.1.2.0/24

Use this command to load the address into the database. The same command is used to update the database as well.

	flask load-db path-to-txt-file


## Run
Finally, run the application from the top level directory (not within the ipq directory)
	
	flask run --host=0.0.0.0 --port=9150
