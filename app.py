import requests

cookies = {
    '_ga': 'GA1.2.1697804321.1652268137',
    '_gid': 'GA1.2.1671280518.1652268137',
    '_yatri_session': 'V0Y4SjlaMUZCb2U1K0dqR3RtYkhsN3NmTVNkZHNsVkRFcFZxRzJDeTZ0QUE2UnVXQTVBVTNjQmsvUFNRcFJZNU5KcURBWjRQR2NkZFhDcXpRRnMxODRreGhRbmhlU0JmbzZpNytHdy9yUy9yS0U5R1hkTW5YOXJyaVZMUXFINHNHbkRNSFRZUG5ncXIvOGNra0pVQ1NLSmVselVhUzhiWXVSYjVJSE1xZmZ4eTF1eUZrTThwQkRvV0ZLcWpFSFhNcTNOV3FOcUxNZ2lmVkNpY3dDY0NsWU02Y1JGeEZtYzByR2x5RjEwYjh3R0tISFhnR1lxbC83NUUxWVptTjZNQlB6ZXVaWTN4bGF6a3ViY05jaDFXUjRMKzdCQWZtMzVpL1doVmNaU2xlMHhYZ0IwVVBiUUc2Y01iSVR5Y0ZWckFJb0pPVnJxc20yQld6bUltY0tUUVhzdUMvSUtoSXpvbWhmWklFYjNBa1Z5UklZVDl3bHpkWVdVVVZWTERwM1FCYVRnTXhnMXEvMGJZMjBCTWVhbE9aQzF6M2xKRzZHWWtZc3Y2ckFwUDhQQm12Z3NKSGtWdmlEeHI1SHkyZXl3azgzTlM2RGZ5STRadlBRczhTeGVNVHg2T0lYV0ZTTGYxRWFpU3FkWVprdjN0RjlvTzJJMUF3Q0dZRGM3RU0zbmMxZ2x0dEpGK28yVjdLU1hFRlJ6SFNPUSs1VlNUNmFZQjd5OTB6RjNsd3ZvPS0tdHd5L1RjejBCd29sa0w3WXMrN3ZlUT09--119af872fb3da5cd8a542727e4ea4b94d4ce85dd',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-CSRF-Token': 'eiDaUWITHb3PQ5EWnYmHwB86t5qvAt/3LhKBICtLb2MvNvb4Ph4ry2d1Mi5vL0dJMr/nCVUSyE2JM2wV4ca97A==',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-platform': '"Linux"',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://ais.usvisa-info.com/es-ar/niv/schedule/38923059/appointment',
    'Accept-Language': 'en-US,en;q=0.9,es-AR;q=0.8,es;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_ga=GA1.2.1697804321.1652268137; _gid=GA1.2.1671280518.1652268137; _yatri_session=VmtZZE01VUtieDBDUXJRN2lBbHdLbW5XdllhdytlMmVDbUNFRUhmVC9KL1NZclpCelR1Vkl0N2tlN2lNa0RaMDhFbUxqWXZWMXRlQ1FCVHd5WkVJaU1yZEVIVXZ1RGZqbndaZlZKUUxjMmV1eE5rWjdvNjFUeHY4Smo1aUtDQ254RnJGNHN4WGY2cURCenM2SkdSQXFoNVZ5TXhDaytWaDdxWlZRUnRuVnJxcXpldGM5dU9pQUdKV0ZGWjF2aTRsODlRU1RjNU9sLzlsM1Y2Y2xkcUFYUzdlSGtvOWYxRVR2VURURzNERG50RHZjWWs0QTMwSjZndmFVNTZlWXBuYW4yM1FqcDh3VHNGa3pQZGpqM0hsUnVvY2h0amxqYTdqZGU4OG5wNm1NNE9SMGV2eDU0NU51MHIrSTg2QXloMTZVTXExR1MreHlBWkhsVmRtTlpVSGVCdzM0MGJkbFlXSFVFaWNicHAveVJaYnFRV0NKVWlaTDFZYUtPZWo3N01KNHdpYVpkeldHVUxQS2VUd1ZOQ3JOSnNFa1BReHV3aDV4ZGFvRVlGNnhpdHJwd2krNFg4VWxicDdKb2g1T1Z2S0ZQaHAxbGFCSU5SREFxNDcyRjlzdDZwR2x2b01udUxGMVB6KzlWSC9EMHpoR1VRY29RYjVrMldsRit0S2dCbnpWZmwrb2VVeHhNRDJEeldwcE5NbTF4ZVZQUlVRa3dYUTNvM3NxVFRWVlVVPS0tZ0hmUnpvaHJ3SmJnVXZvYlJzUllWZz09--be6a049bf2b7e8854835ce99b6e563f2cde45709',
}

response = requests.get('https://ais.usvisa-info.com/es-ar/niv/schedule/38923059/appointment/days/28.json?appointments\\[expedite\\]=false', cookies=cookies, headers=headers)
print(response.json())