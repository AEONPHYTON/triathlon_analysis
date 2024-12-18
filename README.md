# Triathlon Analysis Project
## Analysis of triathlon results with machine learning to find new information

The files in this repository are used to download, extract, and analyze the results of triathlon races, in the notebook the analysis uses machine learning. 
The passage to find all the information about race results is:
* create an account on the Triathlon API to have the API Key (https://apps.api.triathlon.org/register)
* Use the file `01_program_listing.py` (insert the API key and the folder to save the file). All the 200.000 file is about 30 MB with a 48 hours of elaboration
* Use the `02_event_extract.py` to extract the race result (insert the API key and the folder to upload and save the file). All the 200.000 file is about 500 MB with a 12 hours of elaboration
* Use the `03_race_extraction.py` to extract all data about triathlon races (excluding duathlon, winter triathlon, aquathlon, and para-triathlon race, etc.). Some files are corrupted or without data, you can choose to delete them or modify them to have the information****.
* Use the `header.csv` file to set the header of the race result
* `header_description.txt` file that describes the columns
* Use the `04_data_cleaning_triathlon_race.ipynb` for the first step of data cleaning
* Use the `04_1_cleaning_standard_race.ipynb` for the second step of data cleaning
* Use the `05_triathlon_analysis_statistic.ipynb` a notebook to perform traditional statistics
* Use the `06_triathlon_machine_learning_toop_3.ipynb` a notebook to perform machine learning analysis
* `db_standard_female.csv` standard distante database for female used for analysis
* `db_standard_male.csv` standard distante database for male used for analysis
* `PyThorch_best_model(Female).pth` best model with pythorch machine learning analysis for female
* `PyThorch_best_model(Male).pth` best model with pythorch machine learning analysis for male
* `Tensoflow_triathlon_prediction_(Male).h5` best model with Tensorflow machine learning analysis for male
* `Tensoflow_triathlon_prediction_(Female).h5` best model with Tensorflow machine learning analysis for female

In every notebook, there's a large description of the performed analysis.

**** Please note:
Some race files have data corrupted, during the extraction the number of the file indicates the file is corrupted. Open the file and search the problem manually. In the error message, there's an indication about the problem.
Usually, the error is in the time of the split, correct all the errors in the format: 00:00:00 or calculate to find the correct time values

* Error found: 1:00:00 set the zero in front of the hour value 
* Error found: 01::00:00 delete the double colon and set only one 
* Error found: 01;00;00 substitutes the semicolon with the colon 
* Error found: 01:00:00,5 delete the half-second 
* Error found: :: there's not a value between the colon 

It's boring work, but the data is not very clean (the problem, probably, was during time acquisition in the race).
To change the data in the JSON file don't use a spreadsheet like Excel because the first column is a big number and Excel converts it to an exponential number, I suggest using Notepad++ with a JSON plugin or other software
