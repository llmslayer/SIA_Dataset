import os
import json

# Specify the directory containing the files
directory = "./Question_Dataset_without_AQ_Updated_auxilary_information_First_Refinement"

# Loop through all files in the directory
for filename in os.listdir(directory):

    print(f"Processing file: {filename}")
    if filename.endswith(".json") or filename.endswith(".js"):
        filepath = os.path.join(directory, filename)

        # Read the JSON file
        with open(filepath, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                print(f"Skipping file {filename}: not a valid JSON file.")
                continue

        # Process scenarios and remove specified keys
        for scenario in data.get('scenarios', []):
            if 'public_info' in scenario and 'questions' in scenario['public_info']:
                for question in scenario['public_info']['questions']:
                    question.pop('auxilary_information', None)
                    question.pop('Task_category', None)
                    question.pop('complexity', None)

        # Write the updated JSON back to the file
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)

        print(f"Processed and updated file: {filename}")
