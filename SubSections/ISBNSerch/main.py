# Base Methodology unceremoniously lifted from https://gist.github.com/AO8/faa3f52d3d5eac63820cfa7ec2b24aa7

import urllib.request
import json
# import textwrap

# # I need to write the list of variables to a new file in CSV format, one per line, then check for remaining lines in
# read_ISBN file and continue until done. As a large part of that, need to decide where my loops are

# Open text file
f = open("C:\\Users\\trose\\Desktop\\Database Design\\BooK.K.Eeper\\personalBookcaseISBNs.txt", "r")
# print(f.read())

# Isolate 1 Line
# print(f.readline())

# Read and use first ISBN
current_ISBN = f.readline()

# For loop to parse through lines of read file 1 at a time
# for x in f:
#     current_ISBN = x
#     print(current_ISBN)

# Connect to API
base_api_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

# Insert extracted ISBN into API ping
with urllib.request.urlopen(base_api_link + current_ISBN) as f:
    text = f.read()

# Decode Search for Book into usable sections and output for one book (currently)
    decoded_text = text.decode("utf-8")
    obj = json.loads(decoded_text) # deserializes decoded_text to a Python object
    volume_info = obj["items"][0]
    # authors = obj["items"][0]["volumeInfo"]["authors"]

    # Extract Info We Give a Fuck About And Save Them As Variables
    current_authors = obj["items"][0]["volumeInfo"].get("authors", ["N/A"])
    current_title = volume_info["volumeInfo"]["title"]
    current_summary = volume_info["searchInfo"]["textSnippet"]

    # Check if commas are present in the fields and encapsulate in double quotes if necessary
    if ',' in current_title:
        current_title = '"' + current_title + '"'
    if any(',' in author for author in current_authors):
        current_authors = ['"' + author + '"' if ',' in author else author for author in current_authors]
    if ',' in current_summary:
        current_summary = '"' + current_summary + '"'

    # Print Top Label Line
    print('ISBN', ',', 'title', ',', 'authors', ',', 'summary', sep='')

    # Print Extracted Data With ISBN
    print(current_ISBN.strip(), ',', current_title, ',', ", ".join(current_authors), ',', current_summary, sep='')

    # Close File
    f.close()

    # displays title, summary, author, domain, page count and language
    # print("\nTitle:", volume_info["volumeInfo"]["title"])
    # print("\nSummary:\n")
    # print(textwrap.fill(volume_info["searchInfo"]["textSnippet"], width=65))
    # print("\nAuthor(s):", ",".join(authors))
    # print("\nPublic Domain:", volume_info["accessInfo"]["publicDomain"])
    # print("\nPage count:", volume_info["volumeInfo"]["pageCount"])
    # print("\nLanguage:", volume_info["volumeInfo"]["language"])
    # print("\n***")

# while True:
#
#     base_api_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
#     user_input = input("Enter ISBN: ").strip()
#
#     with urllib.request.urlopen(base_api_link + user_input) as f:
#         text = f.read()
#
#     decoded_text = text.decode("utf-8")
#     obj = json.loads(decoded_text) # deserializes decoded_text to a Python object
#     volume_info = obj["items"][0]
#     authors = obj["items"][0]["volumeInfo"]["authors"]
#
#     # displays title, summary, author, domain, page count and language
#     print("\nTitle:", volume_info["volumeInfo"]["title"])
#     print("\nSummary:\n")
#     print(textwrap.fill(volume_info["searchInfo"]["textSnippet"], width=65))
#     print("\nAuthor(s):", ",".join(authors))
#     print("\nPublic Domain:", volume_info["accessInfo"]["publicDomain"])
#     print("\nPage count:", volume_info["volumeInfo"]["pageCount"])
#     print("\nLanguage:", volume_info["volumeInfo"]["language"])
#     print("\n***")
#
#     status_update = input("\nEnter another ISBN? y or n: ").lower().strip()
#
#     if status_update == "n":
#         print("\nThank you! Have a nice day.")
#         break
