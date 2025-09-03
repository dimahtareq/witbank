class Users:
    
    user = [   #A list of dictionary as our database.
    {
        "name": "Noor",
        "credit": 50000
    },
    {
        "name": "Dimah",
        "credit": 55000
    }
    ,{
        "name": "Athraa",
        "credit": 100000
    }
    ]

    def returnUser(name):
        for i in Users.user:
            if i["name"] == name:
                return i["name"], i["credit"]
        return "There is no such name"
    
    

