import pymongo
import csv
import requests
import traceback

credentials = {
    "MONGOURI": "<Your-MongoDB-Service-URI>",
    "SSLCERTPATH": "<PATH-of-SSL-CERT>",
    "DATABASE": "<Mongodb-Database-Name>",
    "COLLECTION": "<Mongodb-Database-Collection>",
    "NOTESURL": "<DAS-Url-Notes-Database>",
    "NOTESSERVERID": "<Notes-Server-User-ID>",
    "NOTESSERVERPASSWORD": "<Notes-Server-Password>"
}

# Connect to MongoDB

client = pymongo.MongoClient(
    credentials.get("MONGOURI"),
    ssl=True,
    ssl_ca_certs=credentials.get("SSLCERTPATH"))

db = client[credentials.get("DATABASE")]
collection = db.nomination
print(f'Connected to MongoDB - Database: {db} - Collection: {collection} ')

documents = []

with open('<CSV File>', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='~')
    for row in csv_reader:
        notes_unid = row[0]
        documents.append(row[0])

print(f'Total Number of Documents to Migrate - {len(documents)}')

for count, document in enumerate(documents, start=1):
    notes_unid = document
    notesURL = credentials.get("NOTESURL") + notes_unid
    r = requests.get(notesURL, auth=(credentials.get("NOTESSERVERID"), credentials.get("NOTESSERVERPASSWORD")))
    r_json = r.json()
    try:
        for element in ['@href', '@authors', '@created', '@modified', '@form', '@noteid']:
            if element in r_json:
                r_json.pop(element)
        """
        ............
        Do you all json data cleaning/reformatting here. 
        Some common cleaning/reformatting are date fields, multivalued string to list, cleaning up some unwanted data etc. 
        Its best practice to clean up data before sending to MongoDB. The use cases varries with the data from nsf.
        ............
        
        """
        """
        This is how we send attachment data to MongoDB. Usually attachments are returned as Base64 from nsf. 
        In this example,"appssm" is a notes document field which has an inline image as attachment.
        
        """
        if 'appssm' in r_json:
            appssm = r_json['appssm']
            cont = appssm.get('content')
            for item in cont:
                if item.get('contentType') == 'image/jpeg':
                    image_data = item.get('data')
                    image = f'<p><img style="width: 539px;" src="data:image/png;base64,{image_data}" data-filename="image.png"><br></p>'
                    r_json['appssm'] = image
                elif item.get('contentType') == 'text/html; charset="US-ASCII"':
                    ssm_text_data = item.get('data')
                    r_json['appssm'] = ssm_text_data

        result = collection.insert_one(r_json)
        print(f'{count} - Notes document with UNID {notes_unid} is migrated to MongoDB')
    except:
        print(f'{count} - Notes document with UNID {notes_unid} is NOT migrated to MongoDB')
        traceback.print_exc()
        continue
