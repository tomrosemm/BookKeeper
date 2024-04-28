# Read a txt file of ISBNs that are one to a line and use Google Books API to find and extract title, author, and
# Summary properly formatted into a CSV file
# Base Methodology unceremoniously lifted from https://gist.github.com/AO8/faa3f52d3d5eac63820cfa7ec2b24aa7

import urllib.request
import json
import csv
import time
import config



def jongara(input_filepath, output_filepath=config.default_books_file, initial_delay=2, max_retries=7):
    delay = initial_delay

    # Open text file of ISBNs to read
    with open(input_filepath, "r") as f_in:

        # Open a CSV file to store finished data
        with open(output_filepath, "a", encoding="utf-8", newline='') as f_out:

            # Create a CSV writer object
            writer = csv.writer(f_out)

            # If the output file is empty, write the header
            if f_out.tell() == 0:
                writer.writerow(['ISBN', 'title', 'authors', 'summary'])

            # Loop through each ISBN in the input file
            for current_ISBN in f_in:
                retries = 0
                success = False

                while not success and retries < max_retries:
                    # Connect to Google Books API
                    base_api_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
                    try:
                        with urllib.request.urlopen(base_api_link + current_ISBN.strip()) as response:
                            text = response.read()
                            decoded_text = text.decode("utf-8")
                            obj = json.loads(decoded_text)

                            # Check if book data is available
                            if "items" in obj and len(obj["items"]) > 0:

                                # Extract relevant information
                                volume_info = obj["items"][0]["volumeInfo"]
                                current_title = volume_info.get("title", "N/A")
                                current_authors = volume_info.get("authors", ["N/A"])
                                current_summary = volume_info.get("description", "N/A")

                                # Ensure proper CSV formatting
                                current_title = current_title.replace('"', '""')
                                current_summary = current_summary.replace('"', '""')

                                # Write extracted data to CSV file
                                writer.writerow([current_ISBN.strip(), current_title, ', '.join(current_authors), current_summary])
                                success = True

                            else:
                                # If no book found for the ISBN, write a placeholder to the CSV file
                                writer.writerow([current_ISBN.strip(), "N/A", "N/A", "N/A"])
                                success = True

                    except urllib.error.HTTPError as e:
                        # Handle HTTP errors (e.g., too many requests)
                        if e.code == 429:
                            retries += 1
                            time.sleep(delay)
                            delay *= 2  # Exponential backoff
                        else:
                            break
                    except Exception as e:
                        break

                print("Processed ISBN:", current_ISBN.strip())

                # Reset delay for next iteration
                delay = initial_delay

    print("Processing complete.")


'''
# Example usage:
input_filepath = "input_ISBNs.txt"  # Replace with the path to your input file
output_filepath = "output_books.csv"  # Replace with the desired output file path
process95(input_filepath, output_filepath)
'''
input_filepath = "list_of_isbn_mine.txt"
output_filepath = "books1.csv"
jongara(input_filepath, output_filepath)
