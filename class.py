class User:
    def __init__(self, user_id, username):
        self.user_id=user_id
        self.username=username
        self.followers=12
        self.following=0
    def follow(self,user):
        user.followers+=1
        self.following+=1
    
user1=User("001","Abhirup")
user2=User("002","Babai")
print(user1.user_id,user1.username)
print(user2.user_id,user2.username)
user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)