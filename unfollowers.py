import time
import os.path
import getpass
from instagrapi import Client
from random import randint
from discord_webhook import DiscordWebhook
from datetime import datetime

cached = {}
cl = Client()


def main():
    global cached
    global cl

    webhook_url = input('Webhook url: ')
    username = input('Username: ')
    password = getpass.getpass('Password: ')
    verification_code = input('Verification code: ')

    if os.path.exists('session.json'):
        cl.load_settings('session.json')
    cl.login(username, password, verification_code=verification_code)
    cl.dump_settings('session.json')

    account_info = cl.account_info().dict()
    print(account_info)

    while True:
        followers = cl.user_followers(account_info['pk'])

        if len(cached) == 0:
            cached = followers

        for follower in cached.keys():
            contains = False

            for cache in followers.keys():
                if follower == cache:
                    contains = True

            if not contains:
                print('[' + str(datetime.now()) + '] https://instagram.com/' + cl.username_from_user_id_gql(follower) + ' unfollowed your account!')
                try:
                    webhook = DiscordWebhook(url=webhook_url)

                    webhook.set_content('https://instagram.com/' + cl.username_from_user_id_gql(follower) + ' unfollowed your account!')
                    webhook.execute(remove_embeds=True)
                except:
                    print('Error sending webhook')

        print('[' + str(datetime.now()) + '] Cached ' + str(len(followers)) + ' followers.')
        cached = followers

        time.sleep(randint(3600, 7200))


if __name__ == '__main__':
    main()