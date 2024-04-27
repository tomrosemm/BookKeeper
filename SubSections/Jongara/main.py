# Read a txt file of ISBNs that are one to a line and use Google Books API to find and extract title, author, and
# Summary properly formatted into a CSV file
# Base Methodology unceremoniously lifted from https://gist.github.com/AO8/faa3f52d3d5eac63820cfa7ec2b24aa7

import urllib.request
import json
import csv
import time

def process95(input_filepath, loopNum, output_filepath="books.csv", initial_delay=2, max_retries=5):
    count = 0
    delay = initial_delay

    print("Jongara - Start")

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
                            print(f"Too many requests error. Retrying in {delay} seconds...")
                            time.sleep(delay)
                            delay *= 2  # Exponential backoff
                        else:
                            print("Unhandled HTTP error:", e)
                            break
                    except Exception as e:
                        print("Error:", e)
                        break

                count += 1
                print("Book", loopNum, ".", count, " complete.")

                # Reset delay for next iteration
                delay = initial_delay

    print("Extraction and writing of ", count, " books and details to 'books.csv' this loop.")
    return count  # Move the return statement outside the loop


def __main__():
    totalCount = process95(r"C:\Users\trose\Desktop\Database Design\BooK.K.Eeper\list_of_isbn1.txt", 1)
    totalCount += process95(r"C:\Users\trose\Desktop\Database Design\BooK.K.Eeper\list_of_isbn2.txt", 2)

    print("Extraction and writing of ", totalCount, " books and details to 'books.csv' total.")


__main__()
