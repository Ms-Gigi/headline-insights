# ubiquitous-succotash
Projects with Python

Headline Analyzer Program

Overview
The Headline Analyzer Program is a Python tool that analyzes text data, specifically headlines. It provides various functionalities such as counting specific words, calculating average headline length, finding the longest and shortest headlines, analyzing word frequency, filtering headlines by length, and exporting results. This program is ideal for journalists, data analysts, or anyone working with headline datasets.

Features
Count Headlines Containing a Word: Count how many headlines contain a specific word.
Write Matching Headlines to File: Save headlines containing a specific word to a new file.
Calculate Average Headline Length: Get the average number of characters in the headlines.
Find Longest and Shortest Headlines: Identify the longest and shortest headlines in the dataset.
Word Frequency Analysis: Analyze and display the most common words and their frequencies.
Filter Headlines by Length: Filter headlines based on a specified minimum and maximum length.
Search for Multiple Words: Search for headlines containing multiple words, using "AND" or "OR" logic.
Save Analysis Report: Save the analysis results (e.g., word frequency, average length) to a file.
Plot Word Frequency: Visualize the top 10 most common words in the dataset as a bar chart.
Load a New File: Switch to analyzing a different dataset without restarting the program.

Requirements
Python 3.7 or later
Required Python libraries:
os (standard library for file handling)
collections (standard library for word counting)
matplotlib (for plotting word frequency)

Installation
Clone or Download the Repository:
Clone the repository using:
bash

Copy
git clone https://github.com/your-repo/headline-analyzer.git
Or download the ZIP file from the repository and extract it.
Install Required Libraries:
If you don't have matplotlib installed, run:
bash

Copy
pip install matplotlib
Prepare Your Dataset:
Prepare a text file containing one headline per line. Make sure the file is in the same directory as the program or provide the full path.
Run the Program:
Open a terminal or command prompt and run:
bash

Copy
python headline_analyzer.py
Usage
When you run the program, you will be prompted to enter the name of the file you want to analyze.
After loading the file, the program displays a menu with the following options:
livecodeserver

Copy
Menu:
    1. Count headlines containing a specific word
    2. Write headlines containing a specific word to a new file
    3. Calculate the average number of characters per headline
    4. Output the longest and shortest headline
    5. Analyze word frequency
    6. Filter headlines by length
    7. Search for headlines with multiple words
    8. Save analysis report to a file
    9. Plot word frequency
    10. Load a new file to analyze
    11. Quit
Enter the number corresponding to the desired action, and follow the prompts to perform the analysis.
Example
Here’s an example of how the program works:

Input File:

Copy
Breaking: Massive Storm Hits the Coast
Sports Update: Local Team Wins Championship
Economy: Stock Market Reaches New Highs
Entertainment: Celebrity Announces New Movie
Menu Options:
If you select "1" and search for the word "storm", the program will output:

Copy
The word 'storm' appears in 1 headline(s).
If you select "4", the program will output:

Copy
Longest headline: Breaking: Massive Storm Hits the Coast
Shortest headline: Entertainment: Celebrity Announces New Movie
If you select "5", the program will display the most common words and their frequencies:

Copy
Most common words:
the: 4 occurrences
new: 2 occurrences
massive: 1 occurrences
...
File Requirements
The input file should be a plain text file (.txt) where each line represents one headline.
Example:

Copy
Headline 1
Headline 2
Headline 3
Output Files
The program generates output files for specific features:
Matching Headlines: A new file containing the filtered headlines (e.g., output.txt).
Analysis Report: A detailed report file (default: analysis_report.txt).
Common Errors
File Not Found:
If the program cannot find the file, it shows:
subunit

Copy
Error: The file '<file_name>' could not be found.
Solution: Ensure the file exists in the directory and you provide the correct name or path.
Empty File:
If the file is empty, the program shows:
subunit

Copy
Error: The file '<file_name>' is empty.
Invalid Input:
For menu choices, ensure you enter a number between 1 and 11.
Customization
You can customize the program as needed:
File Name: Change the default file name for saving analysis reports in the save_analysis_report function.
Word Frequency: Modify the number of most common words displayed by changing the .most_common(10) parameter in word_frequency.
Future Improvements
Add support for multilingual headline analysis.
Include sentiment analysis for headlines.
Support for non-text file formats (e.g., CSV files).
License
This program is open-source and free to use under the MIT License.

