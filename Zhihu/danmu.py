import multiprocessing
import socket
import time
import re
import signal
import pandas as pd
import csv

# 构造socket链接
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname("openbarrage.douyutv.com")
port = 8601
client.connect((host, port))

# 弹幕查询正则表达式
danmu_re = re.compile(b'txt@(.*?)/cid@')
username_re = re.compile(b'nn@=(.*?)/txt@')

def send_req_msg(msgstr):
    '''构造并发送符合斗鱼api的请求消息'''
    msg = msgstr.encode('utf-8')
    data_length = len(msg) + 8
    code = 689
    #构造协议头
    msgHead = int.to_bytes(data_length, 4, 'little') + \
        int.to_bytes(data_length, 4, 'little') + \
        int.to_bytes(code, 4, 'little')
    client.send(msgHead)
    sent = 0
    while sent < len(msg):
        tn = client.send(msg[sent:])
        sent = sent + tn

def DM_start(roomid):
    msg = "type@=loginreq/roomid@={}/\0".format(roomid)
    send_req_msg(msg)
    msg_more =  'type@=joingroup/rid@={}/gid@=-9999/\0'.format(roomid)
    send_req_msg(msg_more)

    while True:
        with open('E:/BaiduNetdiskDownload/0205project/danmu.csv', 'a', newline='') as f:
            data = client.recv(1024)
            danmu_username = username_re.findall(data)
            danmu_content = danmu_re.findall(data)

            if not data:
                break
            else:
                for i in range(0, len(danmu_content)):
                    try:
                        # print('[{}]:{}'.format(danmu_username[0].decode('utf8'), danmu_content[0].decode(encoding='utf8')))

                        writer = csv.writer(f)

                        if danmu_username and danmu_content:
                            print('========')

                            data = [danmu_username[0].decode('utf-8'), danmu_content[0][1:].decode('utf-8')]
                            writer.writerow(data)
                            #dataFrame = pd.DataFrame({'username':danmu_username[0], 'content':danmu_content[0][1:]})
                            #dataFrame.to_csv("E:/BaiduNetdiskDownload/0205project/danmu.csv", index=False, mode='a+')
                    except:
                        continue

def keepAlive():
    while True:
        msg = 'type@=keeplive/tick@=' + str(int(time.time())) + '/\0'
        send_req_msg(msg)
        print('发送心跳包')
        time.sleep(15)

def logout():
    msg = 'type@=logout/'
    send_req_msg(msg)
    print('已经退出服务器')

if __name__ == '__main__':
    room_id = 606118

    p1 = multiprocessing.Process(target=DM_start, args=(room_id,))
    p2 = multiprocessing.Process(target=keepAlive)
    p1.start()
    p2.start()
