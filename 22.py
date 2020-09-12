from twitchobserver import Observer

newf = open("new.txt", 'w')
good_accounts = []
channel = 'in3c'


def parse(usr):
    m = usr.split(':')
    user = m[0]
    return user


def parse_oau(usr):
    m = usr.split(':')
    oauth = 'oauth:' + m[2]
    return oauth


f = open("text.txt", 'r+')
for i in f.readlines():
    user, oauth = parse(i), parse_oau(i)
    try:
        with Observer(user, oauth) as observer:
            observer.join_channel(channel)
            print(f'[+] {i} ')
            good_accounts.append(i)
    except RuntimeError:

        continue

newf = open("new.txt", 'w')
newf.writelines(good_accounts)
newf.close()
