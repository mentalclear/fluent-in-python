# With decorator
def check_is_admin(f):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("This user is not allowed to get or put food")
        return f(*args, **kwargs)
    return wrapper


class Store(object):
    @check_is_admin
    def get_food(self, username, food):        
        return self.storage.get(food)

    @check_is_admin
    def put_food(self, username, food):        
        return self.storage.put(food)
        