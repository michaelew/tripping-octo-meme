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
    for stuff in user.iteritems():
        if not "5" in stuff[1]:
            print stuff[1] + ' ' + '(' + stuff[0] + ')'
