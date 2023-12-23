# triathlon_analysis
Analysis of triathlon results with machine learning to find new information

The files in this repository are used to download, extract, and analyze the results of triathlon races, in the notebook the analysis uses machine learning. 
The passage to find all the information about race results is:
* create an account on the Triathlon API to have the API Key (https://apps.api.triathlon.org/register)
* Use the file 01_program_listing.py (insert the API key and the folder to save the file). All the 200.000 file is about 30 MB with a 48 hours of elaboration
* Use the 02_event_extract.py to extract the race result (insert the API key and the folder to upload and save the file). All the 200.000 file is about 500 MB with a 12 hours of elaboration
* Use the 03_.py to extract all data about triathlon races (excluding duathlon, winter triathlon, aquathlon, and para-triathlon race, etc.). Some files are corrupted or without data, you can choose to delete them or modify them to have the information.
