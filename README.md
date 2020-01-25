## Menu Scraper

A simple way to get relevant data from the following menu:
https://menupages.com/asian-cajun-too/1322-chicago-ave-evanston

I used python the fetch the appropriate response. I then filtered this reponse through 3 functions: make_restaurant, get_category, and make_entry.

In the first function make_entry(), I make an entry for the restaurant and pass in the get_category() function for each category in esponse_json[menu_category_list]. In the get_category() function, I then pass in the make_entry() function to add entries with the appropriate name, description, and price.
