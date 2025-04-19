import os  # For file handling and checking file existence
from collections import Counter  # For efficient word frequency analysis
import matplotlib.pyplot as plt  # For plotting word frequency


# Read headlines from a file
def read_file(file_name):
    """
    Reads all headlines from a file and returns them as a list.
    
    Parameters:
        file_name (str): The name of the file to read.
    
    Returns:
        list: A list of headlines read from the file.
    """
    headlines = []  # Initialize an empty list to store headlines
    try:
        with open(file_name, "r") as file:  # Open the file in read mode
            for line in file:
                headlines.append(line.strip())  # Add each line (trimmed of whitespace) to the list
        if not headlines:  # Check if the file is empty
            print(f"\nError: The file '{file_name}' is empty.\n")
        else:
            print(f"\nFile '{file_name}' successfully loaded with {len(headlines)} headlines.\n")
    except FileNotFoundError:  # Handle the case where the file does not exist
        print(f"\nError: The file '{file_name}' could not be found.")
    return headlines

# Save analysis data to a file
def save_analysis_report(headlines, file_name="analysis_report.txt"):
    """
    Saves the analysis results (e.g., average characters, word frequency) to a file.
    
    Parameters:
        headlines (list): List of headlines to analyze.
        file_name (str): Name of the file to save the report (default is 'analysis_report.txt').
    """
    with open(file_name, 'w') as file:  # Open the file in write mode
        file.write(f"Total Headlines: {len(headlines)}\n")
        file.write(f"Average Characters: {average_characters(headlines):.2f}\n")
        file.write(f"Longest Headline: {find_longest_headline(headlines)}\n")
        file.write(f"Shortest Headline: {find_shortest_headline(headlines)}\n")
        file.write("\n--- Word Frequency ---\n")
        word_counts = word_frequency(headlines)  # Analyze word frequency
        for word, count in word_counts.most_common(10):  # Write the top 10 most common words
            file.write(f"{word}: {count} occurrences\n")
    print(f"\nAnalysis report saved to '{file_name}'.")

# === Analysis Functions ===

# Count occurrences of a word in headlines
def count_headlines_with_word(headlines, word):
    """
    Counts the number of headlines containing a specific word (case-insensitive).
    
    Parameters:
        headlines (list): List of headlines to search.
        word (str): The word to search for.
    
    Returns:
        int: The number of headlines containing the word.
    """
    count = sum(1 for headline in headlines if word.lower() in headline.lower())  # Count matching headlines
    print(f"\nThe word '{word}' appears in {count} headline(s).\n")
    return count

# Write headlines containing a specific word to a file
def write_matching_headlines(headlines, matching_word, output_file):
    """
    Writes all headlines containing a specific word to a new file.
    
    Parameters:
        headlines (list): List of headlines to search.
        matching_word (str): The word to search for.
        output_file (str): The name of the output file to save matching headlines.
    """
    with open(output_file, 'w') as file:  # Open the file in write mode
        for headline in headlines:
            if matching_word.lower() in headline.lower():  # Case-insensitive check
                file.write(headline + '\n')  # Write matching headlines to the file
    print(f"\nHeadlines containing '{matching_word}' have been written to '{output_file}'.")

# Calculate average headline length
def average_characters(headlines):
    """
    Calculates the average number of characters per headline.
    
    Parameters:
        headlines (list): List of headlines to analyze.
    
    Returns:
        float: The average number of characters per headline.
    """
    if not headlines:  # Handle the case where no headlines are provided
        return 0.0
    total_characters = sum(len(headline) for headline in headlines)  # Total characters across all headlines
    average = total_characters / len(headlines)  # Calculate the average
    print(f"\nThe average number of characters per headline is: {average:.2f}\n")
    return average

# Find the longest headline
def find_longest_headline(headlines):
    """
    Finds the longest headline in the list.
    
    Parameters:
        headlines (list): List of headlines.
    
    Returns:
        str: The longest headline.
    """
    return max(headlines, key=len)  # Use Python's built-in max() function

# Find the shortest headline
def find_shortest_headline(headlines):
    """
    Finds the shortest headline in the list.
    
    Parameters:
        headlines (list): List of headlines.
    
    Returns:
        str: The shortest headline.
    """
    return min(headlines, key=len)  # Use Python's built-in min() function

# Analyze word frequency
def word_frequency(headlines):
    """
    Analyzes the frequency of words across all headlines.
    
    Parameters:
        headlines (list): List of headlines to analyze.
    
    Returns:
        Counter: A Counter object containing word frequencies.
    """
    all_words = []  # Initialize a list to hold all words
    for headline in headlines:
        all_words.extend(headline.lower().split())  # Split each headline into words and add to the list
    word_counts = Counter(all_words)  # Count word frequencies
    print("\nMost common words:")
    for word, count in word_counts.most_common(10):  # Display the top 10 most common words
        print(f"{word}: {count} occurrences")
    return word_counts

# Filter headlines by length
def filter_headlines_by_length(headlines, min_length=0, max_length=float('inf')):
    """
    Filters headlines by their character length.
    
    Parameters:
        headlines (list): List of headlines to filter.
        min_length (int): Minimum length of headlines to include.
        max_length (int): Maximum length of headlines to include.
    
    Returns:
        list: List of headlines matching the length criteria.
    """
    filtered = [headline for headline in headlines if min_length <= len(headline) <= max_length]
    print(f"\nHeadlines with length between {min_length} and {max_length}:")
    for headline in filtered:
        print(headline)
    return filtered

# Search for headlines with multiple words
def search_multiple_words(headlines, words, operator="AND"):
    """
    Searches for headlines containing multiple words using 'AND' or 'OR' logic.
    
    Parameters:
        headlines (list): List of headlines to search.
        words (list): List of words to search for.
        operator (str): The operator to use ('AND' or 'OR').
    
    Returns:
        list: List of matching headlines.
    """
    words = [word.lower() for word in words]  # Convert all words to lowercase for case-insensitive comparison
    matching_headlines = []
    for headline in headlines:
        headline_lower = headline.lower()
        if operator == "AND" and all(word in headline_lower for word in words):  # 'AND' logic
            matching_headlines.append(headline)
        elif operator == "OR" and any(word in headline_lower for word in words):  # 'OR' logic
            matching_headlines.append(headline)
    print(f"\nHeadlines matching '{operator}' operator for {words}:")
    for headline in matching_headlines:
        print(headline)
    return matching_headlines

# Plot word frequency
def plot_word_frequency(word_counts):
    """
    Plots the top 10 most common words as a bar chart.
    
    Parameters:
        word_counts (Counter): A Counter object containing word frequencies.
    """
    words, counts = zip(*word_counts.most_common(10))  # Extract the top 10 words and their counts
    plt.bar(words, counts, color='skyblue')  # Create a bar chart
    plt.title("Top 10 Most Common Words in Headlines")  # Chart title
    plt.xlabel("Words")  # X-axis label
    plt.ylabel("Frequency")  # Y-axis label
    plt.xticks(rotation=45)  # Rotate word labels for better readability
    plt.tight_layout()  # Adjust layout for display
    plt.show()

# === Main Program ===

def main():
    """
    Main function to control the program flow and display the menu.
    """
    print("=" * 60)
    print("Welcome to the Enhanced Headline Analyzer Program")
    print("=" * 60)

    # Prompt user for the filename to read
    file_name = input("\nWhat file do you want to read? ").strip()
    while not os.path.isfile(file_name):  # Validate file existence
        print("That file does not exist. Please try again.")
        file_name = input("\nWhat file do you want to read? ").strip()

    headlines = read_file(file_name)  # Load the file into a list

    while True:
        # Display Menu
        print("\n" + "-" * 60)
        print("Menu:")
        print("\t1. Count headlines containing a specific word")
        print("\t2. Write headlines containing a specific word to a new file")
        print("\t3. Calculate the average number of characters per headline")
        print("\t4. Output the longest and shortest headline")
        print("\t5. Analyze word frequency")
        print("\t6. Filter headlines by length")
        print("\t7. Search for headlines with multiple words")
        print("\t8. Save analysis report to a file")
        print("\t9. Plot word frequency")
        print("\t10. Load a new file to analyze")
        print("\t11. Quit")
        print("-" * 60)

        # Get user input
        choice = input("Enter your choice (1-11): ").strip()
        if not choice.isdigit() or not (1 <= int(choice) <= 11):  # Validate menu choice
            print("Invalid choice. Please enter a number between 1 and 11.")
            continue

        choice = int(choice)

        # Handle user choice
        if choice == 1:
            word = input("Enter the word you want to count: ").strip()
            count_headlines_with_word(headlines, word)
        elif choice == 2:
            word = input("Enter the word you want to match: ").strip()
            output_file = input("Enter the output file name: ").strip()
            write_matching_headlines(headlines, word, output_file)
        elif choice == 3:
            average_characters(headlines)
        elif choice == 4:
            print(f"Longest headline: {find_longest_headline(headlines)}")
            print(f"Shortest headline: {find_shortest_headline(headlines)}")
        elif choice == 5:
            word_frequency(headlines)
        elif choice == 6:
            min_len = int(input("Enter the minimum length: "))
            max_len = int(input("Enter the maximum length: "))
            filter_headlines_by_length(headlines, min_len, max_len)
        elif choice == 7:
            words = input("Enter the words to search (comma-separated): ").strip().split(',')
            operator = input("Enter the operator (AND/OR): ").strip().upper()
            search_multiple_words(headlines, words, operator)
        elif choice == 8:
            save_analysis_report(headlines)
        elif choice == 9:
            word_counts = word_frequency(headlines)
            plot_word_frequency(word_counts)
        elif choice == 10:
            file_name = input("\nWhat file do you want to read? ").strip()
            while not os.path.isfile(file_name):  # Validate file existence
                print("That file does not exist. Please try again.")
                file_name = input("\nWhat file do you want to read? ").strip()
            headlines = read_file(file_name)
        elif choice == 11:
            print("\nThank you for using the Headline Analyzer! Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    main()
