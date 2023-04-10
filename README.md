# CayoAnalysis
Program that parses through screenshots of the Cayo Perico heist completion screen from Grand Theft Auto Online, and extracts the data into CSV format.
# Instructions
1. Place all images you want to extract data from in the Images folder
1. Change settings if wanted in settings.csb
    + `rewrite` is whether or not the output file should be overwritten to added on to
    + `onlyCompletes` is if the data from images that not all data could be extracted from should be used in the final output file
1. Run main.py
<br /> <br />
The output file is finalOutput.csv. If the file does not exist (you will not have it when cloning/downloading this repository) it will be created.
<br /> <br />
Also, there is an example output file with sample data in the Examples folder.