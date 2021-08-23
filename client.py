SERVER_IP = ''  

SERVER_PORT = 5555

import select
import threading
import sys
import random
import time
import socket
import termios

try: 


    def receiveMsg(s,killRequest):
        while not killRequest.isSet(): #waiting for user
            r, w, x = select.select([s], [], []) 
            data = r[0].recv(1024)
            print data
            if data:
                killRequest.set()

    def sendMsg(s, userid, killRequest, youBuzzed):
        while not killRequest.isSet(): 
            r, w, x = select.select([sys.stdin], [], [], 0.02)

            if r:
                s.send(str(userid))
                youBuzzed.set()
                time.sleep(0.01)
                break

    serverip = SERVER_IP
    serverport = SERVER_PORT
    clientport = random.randint(2000, 3000)


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', clientport))
    s.connect((serverip, serverport))
    userid = s.recv(1024)
    print "***We welcome you in the game.Good Luck.",
    print "You are player number-->",userid,
    print "***"
    win_score = s.recv(1024)
    print  "\nRules : \n 1)press buzzer first, answer correct and gain points.\n 2)1 point will be awarded for correct answer and 0.5 will be deducted for a wrong answer.\n 3)You have 10 sec to press the buzzer and answer the question.\n 4)Total number of points to win are:", win_score

    #game loop
    continue_next_round = 1 
    while continue_next_round:
        
        question = s.recv(1024)
        killRequest = threading.Event()
        youBuzzed = threading.Event()

        sendThread = threading.Thread(target = sendMsg, args = [s, userid, killRequest, youBuzzed]) 
        receiveThread = threading.Thread(target = receiveMsg, args = [s, killRequest]) 

        time.sleep(0.1)
        print "Your question is:", question
        print "Press the buzzer fast"
        
        s.setblocking(0)
        sendThread.start()
        receiveThread.start()
        receiveThread.join()
        sendThread.join()

        s.setblocking(1)
        termios.tcflush(sys.stdin, termios.TCIOFLUSH) 
        time.sleep(0.01)
        if youBuzzed.isSet():
            print "Answer the question"
            givenAnswer = raw_input()
            s.send(givenAnswer)
        else:
            givenAnswer = s.recv(1024)
            print "You answered-->:", givenAnswer
            
        is_correct_str = s.recv(1024)
        time.sleep(0.001)
        print is_correct_str
        trueAnswer = s.recv(1024)
        print "Correct answer is-->:",trueAnswer

        scoreboard = s.recv(1024) 
        scoreboard = scoreboard.split()

        print "Current Scoreboard scoreboard is"
        for i in range(len(scoreboard)):
            print i, scoreboard[i]
        continue_next_round = s.recv(1024)
        continue_next_round = int(continue_next_round)

    final_message = s.recv(1024) 
    print final_message
except Exception as e:
    print e 
finally: 
    s.close()
