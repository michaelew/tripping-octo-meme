users = [
    {
        'login': 'admin',
        'type': 'admin',
        'password': '5ac467'
    },
    {
        'login': 'freddy',
        'type': 'user',
        'password': '5a443c'
    },
    {
        'login': 'teddy',
        'type': 'user',
        'password': '5a4d3c'
    }
]

for user in users:
    print "{0} ({1})".format(user['login'], user['type'])
