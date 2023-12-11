import json

class JsonDB:

    def insert(self,name,email,dob,password):
        with open("db.json" ,'r') as rf:
            users = json.load(rf)

            if email in users:
                return 0
            else:
                users[email] = [name,dob,password]

        with open('db.json', 'w') as wf:
            json.dump(users,wf,indent=4)
            return 1

    def authenticate(self,email,password):

        with open('db.json','r') as rf:
            users = json.load(rf)

            if email in users:
                if users[email][2] == password:
                    return 1
                else:
                    return 0
            else:
                return 0