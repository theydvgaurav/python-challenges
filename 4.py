
import requests

placeholder = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
q = 12345

while True:
    url = placeholder + str(q)
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)
    try:
        txt = response.text
        q = txt.split("and the next nothing is ")[-1]
    except Exception:
        print("Unexpected result", response.text) # Unexpected result Yes. Divide by two and keep going.
        break

# Next One -> peak.html
