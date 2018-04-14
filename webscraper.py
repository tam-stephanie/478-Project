import requests

# Grab link to page of reviews and make sure it is accessible
page = requests.get("https://myanimelist.net/anime/5114/Fullmetal_Alchemist__Brotherhood/reviews")

# Print error message, then exit if page is unaccessible
if page.status_code >= 400:
    print('Error {}: Unable to access page. Exiting program.'.format(page.status_code))
    exit(1)

#print(page.content)

# Notes on grabbing review text from page:
#   <div class="spaceit textReadability word-break pt8 mt8" ...>
#       <span style id="review#####"> to show full review text

#classification: span class="info pt8" --> ratings & stuff main page of the anime
