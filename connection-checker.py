import csv

import requests 


status_dict = {"Website": "Status"} # Call the main function


def main():
    with open("websites.txt", "r") as fr: # Open the file
        for line in fr: # For each line in the file
            website = line.strip() # Strip the line
            status = requests.get(website).status_code 
            status_dict[website] = "working" if status == 200 \
                else "not working" # Add the status to the dictionary
 
    # print(status_dict)
    with open("website_status.csv", "w", newline="") as fw: # Open the file
        csv_writers = csv.writer(fw) # Create a csv writer
        for key in status_dict.keys(): # For each key in the dictionary
            csv_writers.writerow([key, status_dict[key]]) # Write the key and value to the file


if __name__ == "__main__": # If this file is run as a script
    main() # Run the main function