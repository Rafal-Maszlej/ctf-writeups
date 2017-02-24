import socket

HOST = '209.190.1.131'
PORT = 9002

f = open('log.txt', 'w')

def take_data():
    data = s.recv(1024)
    print(data)
    f.write(str(data, encoding='utf-8'))
    return data

def compare():
    results = set()

    n = len(sample1)

    while n:
        l = [sample1[i:i+n] for i in range(len(sample1)-n+1)]

        for elem in l:
            if elem in sample2:
                results.add(elem)

        n -= 1

    if results:
        return str(len(sorted(results, key=len)[-1]))
    else:
        return '0'


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    for _ in range(2):
        data = take_data()

    answer = data[-4:-2]
    print(answer)
    f.write(str(answer, encoding='utf-8')+'\n')
    s.sendall(answer+b'\n')

    while True:
        data = take_data()

        g = open('temp.txt', 'wb')
        g.write(data)
        g.close()

        temp = []
        for line in open('temp.txt', 'rb'):
            temp.append(line)

        p = temp[2].find(b'Sample 01')
        q = temp[2].find(b'Sample 02')
        sample1 = temp[2][p+11:temp[2].find(b' - Sample 02')]
        sample2 = temp[2][q+11:].strip()
        
        if len(temp) < 4:
            data = take_data()
            sample2 += data[q+11:data.find(b'The answer')-6].strip()

        sample1, sample2 = ((sample1, sample2), (sample2, sample1))[sample1 < sample2]


        answer = compare()

        s.send(answer.encode('utf-8'))
        s.send(b'\n')

        print(answer)
        f.write(answer+'\n')

