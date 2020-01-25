import requests

def get_auth_response():
    headers = {
        'authority': 'api-gtm.grubhub.com',
        'origin': 'https://menupages.com',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'content-type': 'application/json',
        'accept': '*/*',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'referer': 'https://menupages.com/proxy/proxy.html',
        'accept-encoding': 'identity',
        'accept-language': 'en-US,en;q=0.9',
    }

    data = {
        "brand":"GRUBHUB",
        "client_id":"mp_yFU6flWhiKRdlgSMrwC43FF2",
        "scope":"anonymous",
        "device_id":1927446407
    }

    auth_response = requests.post('https://api-gtm.grubhub.com/auth', headers=headers, json=data)
    auth_response.raise_for_status()
    return auth_response

def get_menu_response(access_token):
    headers = {
        'authority': 'api-gtm.grubhub.com',
        'accept': 'application/json',
        'origin': 'https://menupages.com',
        'authorization': 'Bearer ' + access_token,
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'content-type': 'application/json',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'referer': 'https://menupages.com/proxy/proxy.html',
        'accept-encoding': 'identity',
        'accept-language': 'en-US,en;q=0.9',
    }

    params = (
        ('hideUnavailableMenuItems', 'true'),
        ('showMenuItemCoupons', 'false'),
        ('includePromos', 'true'),
        ('bust', '1579987408995'),
    )

    menu_response = requests.get('https://api-gtm.grubhub.com/restaurants/337669', headers=headers, params=params)
    menu_response.raise_for_status()
    return menu_response

auth_response = get_auth_response()
menu_response = get_menu_response(auth_response.json()["session_handle"]["access_token"])

def make_entry(menu_item):
    return {
        "name": menu_item["name"],
        "description": menu_item["description"],
        "price": round(menu_item["price"]["amount"] / 100, 2)
    }

def get_category(category):
    return {
        "name": category["name"],
        "items": [make_entry(item) for item in category["menu_item_list"]]
    }

def make_restaurant(response_json):
    return {
        "restaurant": response_json["name"],
        "categories": [get_category(category) for category in response_json["menu_category_list"]]
    }

print(menu_response)
print(make_restaurant(menu_response.json()['restaurant']))