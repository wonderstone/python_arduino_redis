import redis,time

config = dict(host='127.0.0.1', port=6379, db=0)
r = redis.StrictRedis(**config)

if __name__ == '__main__':
    while True:
        print(r.get('I0T').decode())
        time.sleep(1)