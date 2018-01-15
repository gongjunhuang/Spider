if not loginReq.json()['r']:
    print(s.cookies.get_dict())
    with open('cookiefile' 'wb') as f:
        json.dump(s.cookies.get_dict(), f)
else:
    print('login fail!!!')