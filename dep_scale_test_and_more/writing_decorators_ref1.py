def check_is_admin(username):
    if username != 'admin':
        raise Exception("This user is not allowed to get or put food")

class Store(object):
    def get_food(self, username, food):
        check_is_admin(username)
        return self.storage.get(food)

    def put_food(self, username, food):
        check_is_admin(username)
        return self.storage.put(food)
        