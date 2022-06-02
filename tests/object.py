# basic object (MAIN)

class Identify(object):
  def __init__(self, user) -> None:
    print("You have created a new object!")
    self.user = user
    
  def show(self):
    print(f"The username is {self.user['username']}, and the ID is {self.user['id']}")
    
UserObject = Identify({
  "username": "AWeirdDev#1744",
  "id": 123456789
})
UserObject.show()
