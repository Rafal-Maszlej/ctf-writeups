import socket

HOST = '54.175.35.248'
PORT = 8001

f = open('log.txt', 'w')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        data = s.recv(1024)
        data = str(data, encoding='utf-8').strip()
        print(data)
        f.write(data)

        if data.startswith('To receive the first pair'):
            answer = data[-3:-1]
        elif 'Stage' in data:
            p = data.find('01')
            q = data.find('02')
            sample1 = data[p+4:].partition(' ')[0]
            sample2 = data[q+4:].partition(' ')[0]

            answer = str(sum(1 for i, j in zip(sample1, sample2) if i!=j))
        else:
            answer = ''

        if answer:
            print(answer)
            f.write(answer+'\n')
            s.sendall(bytes(answer+'\n', encoding='utf-8'))
