class SocialNetwork():
    def __init__(self):
        self.friend_list = []

    def add_friend(self, name):
        self.friend_list.append(name)
        print(self.friend_list)

    def publish_message(self, message):
        print(f'{message} was published')

    def post_comment(self, comment):
        print(f'You commented into a post: {comment}')

    def search_user(self, user_searched):
        for friend in self.friend_list:
            if friend == user_searched:
                print('User found')
            else:
                print('User not found')

social_network = SocialNetwork()

social_network.add_friend('Rafael')

social_network.publish_message('Oi')

social_network.post_comment('Olá')

social_network.search_user('Rafael')