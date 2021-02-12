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
We wanted to show readers the correlations between the polititcal party type and Income group or ethnicity to see voting patterns between income groups and ethnicities. To most effectively show the connections between these two variables, the data had to be re-formatted various ways to accomodate for each income group or ethnicity to relate their perspective political parties. We used matplotlib.pyplot to plot our bar graphs. We made a total of 2 graphs where the x-axis was Income Groups and Ethnicities, and the y-axis was count for each political party. Each x-axis componenet had 8 individual bars representing the count of the votes for each party. The graphs are in the 'Income_Parties.pdf' and the 'Ethnicity_Parties.pdf' files. This code shows the relationship for Alaska but can be used for any other states multiple states combined if you simple merge the demographics files of each state and change the filepath. 
scrpit:
python3 datathon.py



## Our Code
* We edited the jupyter notebook provided to us by NYU Libraries to better fit our needs: [l2_political_general_subsetting_guide.ipynb](l2_political_general_subsetting_guide.ipynb). Instead of taking a one percent sample, we took a two percent sample. Parts V and VI were added on to edit Voter IDs and birthdays.
* We created a python program that finds our newfound data that has just been anonymized (it has to be in the same directory as the code and the filename has to be replaced in the actual code to the correct file name : state_demographic = pd.read_csv('PUT FILENAME HERE', usecols=selected_variables)). The python program takes the incoming csv file and reorganizes the data into a dictionary that is nestes in another dictionary. The first index would either be the income group or ethnicity and the indexes within these index would be the seperate political parties for each perspective income or ethnicity. The value for each of the political parties was a count keeping track of the amount of people who voted for that party in that income group or ethnicity. Than the data had to be reorganized into array formats so that it could be taken as parameters in the df2 = pd.DataFrame() funciton which is what all the if clauses are doing. 
* our code can work for any of the states Demographic files post cleaning. 
