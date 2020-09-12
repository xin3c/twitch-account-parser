from twitchobserver import Observer

rfile = input('Print the filename of yor accounts list.\n')

channel = 'nasa'


def parse(usr):
    m = usr.split(':')
    user = m[0]
    return user


def parse_oau(usr):
    m = usr.split(':')
    oauth = 'oauth:' + m[2]
    return oauth


try:
    f = open(rfile, 'r+')
except FileNotFoundError:
    print('Wrong filename')
    exit()
for i in f.readlines():
    user, oauth = parse(i), parse_oau(i)
    try:
        with Observer(user, oauth) as observer: 
            observer.join_channel(channel)
            newf = open("output.txt", 'a+')
            print(f'[+] {i}')
            newf.write(i)
            newf.close()

    except RuntimeError:
        print('[-]' + i)
        continue
