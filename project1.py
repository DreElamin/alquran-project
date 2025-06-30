import requests

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