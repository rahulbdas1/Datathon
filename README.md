# Datathon: Track 2
Rahul Das and Forzana Rime

## Background
For this track, we were given the task to filter through L2 Political Data and deidentify it for appropriate public use. We were also asked to expand usability of the data. Although we were unable to process all the files provided, we have included the script needed to process the files and a sample file of processed data: [alaska-twopercent-sample.csv](alaska-twopercent-sample.csv). 

## Our Idea
* To anonymize the data, we want to keep certain fields we feel are important while deleting unnecessary information.
  - The fields we decided to keep as is: voter participation in the past three general elections (2008, 2012, 2016), residence zipcode, voter age, party affiliation, 
change in party affiliation, ethnicity, ethnic group, religion, marital status, county, education level, household income (both range and estimated exact figures), and gun ownership.
  - We jittered longitude and latitude.
  - We changed birthdays from MM/DD/YYYY to just MM/YYYY
  - We also encrypted Voter IDs using a simple Caesar Cipher, however if necessary, we can get rid of that field in the data altogether.

## Data Visualization
RAHUL DESCRIBE WHAT YOU DID HERE

## Our Code
* We edited the jupiter notebook provided to us by NYU Libraries to better fit our needs: [l2-political-general-subsetting-guide.ipynb](l2-political-general-subsetting-guide.ipynb).
* RAHUL INCLUDE BRIEF DESCRIPTION OF YOUR CODE HERE
