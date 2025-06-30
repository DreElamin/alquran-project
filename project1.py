import requests
import pandas as pd
import sqlalchemy as db

url = "http://api.alquran.cloud/v1/ayah/262/en.asad"
response = requests.get(url)

data = response.json()


if data["status"] == "OK":
  ayah = data["data"]
  print("Surah:", ayah["surah"]["englishName"])
  print("Ayah Number:", ayah["numberInSurah"])
  print("Text:", ayah["text"])
else:
  print("Error:", data["status"])


if data["status"] == "OK":
    ayah = data["data"]
    ayah_dict = {
        "surah": [ayah["surah"]["englishName"]],
        "ayah_number": [ayah["numberInSurah"]],
        "text": [ayah["text"]],
        "translator": [ayah["edition"]["englishName"]]
    }

    df = pd.DataFrame(ayah_dict)
    print(df)
else:
    print("Error:", data["status"])

engine = db.create_engine('sqlite:///quran.db')

df.to_sql('ayahs', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM ayahs;")).fetchall()
   print(pd.DataFrame(query_result))