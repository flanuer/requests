import requests
r = requests.get("https://www.whoi.edu/website/redtide/research/publications-reports/national/")
print(r.text)
