import json

# reading the input file and all of its lines
with open('input.txt', 'r') as file:
    data = file.readlines()

# setting right side of colon values to none for later
dme_id = dme_name = drug_id = drug_name = reference_name = reference_url = None

# all lines are split based on tab and put into list
for line in data:
    parts = line.strip().split("\t")
    
    # takes all parts of input file below sets of colons for data
    if len(parts) < 3:
        continue
    
    # ex. in ['DE4LYSA', 'DI', 'DMIKQH5'] <-- key is DI and Value is DMIKQH5
    key = parts[1]
    value = parts[2]
    
    # assigning variable names based on categorical info specified in colons section
    if key == "EI":
        dme_id = value
    elif key == "EN":
        dme_name = value
    elif key == "DI":
        drug_id = value
    elif key == "DN":
        drug_name = value
    elif key == "RN":
        reference_name = value
    elif key == "RU":
        reference_url = value

# splitting reference url into 2 parts(before and after "term") and taking last value for id
pmid = reference_url.split("term=")[-1]

# creating the JSON object
json_obj = {
    "_id": f"{dme_id}-METABOLIZES-{drug_id}",
    "_version": 1,
    "object": {
        "name": drug_name,
        "id": drug_id
    },
    "predicate": "metabolizes",
    "predication": [
        {
            "pmid": pmid
        }
    ],
    "subject": {
        "name": dme_name,
        "id": dme_id
    }
}

# outputting the JSON object
print(json.dumps(json_obj, indent=2))
