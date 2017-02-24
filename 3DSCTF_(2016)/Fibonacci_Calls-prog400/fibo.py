import socket
import functools

HOST = '54.175.35.248'
PORT = 8000

f = open('log.txt', 'w')


@functools.lru_cache()
def fibo_count(n):
    if n < 2:
        return 1
    return fibo_count(n-2) + fibo_count(n-1)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        data = s.recv(1024)
        data = str(data, encoding='utf-8').strip()
        print(data)
        f.write(data)

        if 'To start the challenge' in data:
            answer = data[-3:-1]
        elif 'Stage' in data:
            p = data.find('N = ')
            n = data[p+4:data.find('The answer')].strip()

            answer = str(fibo_count(int(n))*2-2)

            if len(answer) > 3:
                answer = str(int(answer[-3:]))
        else:
            answer = ''

        if answer:
            print(answer)
            f.write(answer+'\n')
            s.sendall(bytes(answer+'\n', encoding='utf-8'))
