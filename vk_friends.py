import requests
import json

OAUTH_URL = "https://oauth.vk.com/authorize"
TOKEN = "10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c"

class User:
    def __init__(self, id) -> None:
        self.id = id

    def list_of_friends(self) -> int:
        response = requests.get(
            "https://api.vk.com/method/friends.get",
            params={
                "access_token": TOKEN,
                "v": 5.21,
                "user_id": self.id,
                "order": "random",
                "scope": "friends",
            }
        )
        data_json = response.json()
        return data_json["response"]["items"]

    def __str__(self):
        link = "https://vk.com/id" + str(self.id)
        return link

    def __and__(self, other):
        user1_friends = self.list_of_friends()
        user2_friends = other.list_of_friends()
        mutual_friends = set(user1_friends) & set(user2_friends)
        return mutual_friends

user1 = User(id = 26485931)
user2 = User(id = 56053916)


print("Ссылка на юзера №1", user1)
print("================================")
print("Ссылка на юзера №2", user2)
print("Cписок друзей user1", user1.list_of_friends())
print("================================")
print("Список друзей user 2", user2.list_of_friends())
print("================================")
friends = user1 & user2
for friend in friends:
    new_user = User(friend)
    print("Общий друг user1 и user2", (new_user))
