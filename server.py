NUMBER_OF_CLIENTS = 3
WINNING_SCORE = 5
SERVER_PORT = 5555

import select
import socket
import time
import random

questions = [" The term *Googly* is associated with?\n a.Cricket b.Volleyball c.Tennis d.Hockey",
    " In 1924 the first winter Olympics was held in?\n a.France b.Italy c.India d.None",
    " Shivam dube is associated with which sports? \n a.Football b.Cricet c.Badminton d.Foosball",
    " How many gold medals won by India in 2010 Commonwealth Games ? \n a.30 b.32 c.36 d.38",
    " Ronaldo is associated with ? \n a.Football b.Cricet c.Badminton d.Foosball",
    " The term *Smasher* is associated with? \n a.Cricket b.Volleyball c.Tennis d.Hockey",
    " Gelid synonym? \n a.talkitive b.hard headed c.extremely cold d.mad",
    " How many states are there in India? \n a.24 b.29 c.30 d.31",
    " What are the different types of real data type in C ? \n a. float b. long float c.short int d. long long float",
    " National Income estimates in India are prepared by? \n a. Planning Commission b. Reserve Bank of India c.Central statistical d.Indian statistical Institute",
    " What is 1+2 ? \n a.1 b.2 c.3 d.4",
    " The purest form of iron is? \n a. wrought iron b.steel c.pig iron d.nickel steel",
    " Fathometer is used to measure?\n a.earthquake b.rainfall c.ocean depth d.sound intensity",
    " Which one of the following is not a mixture?\n a.air b.mercury c.milk d.cemment ",
    " What is the oxidation number of sulfur in H2S?\n a.2 b.-2 c.1 d.-1",
    " What is the capital of china?\n a. Santiago b.delhi c.bejing d.none",
    " Who is the english physicist responsible for the Big Bang Theory?\n a.Albert Einstein b.Michael Skube c.George Gamow d. sachin tendulkar",
    " Revolver discovered by?\n a.colt b.Bushwell c.denly d. daimore",
    " The first hand glider was designed by?\n a.Leonardo DaVinci b.The Wright brothers c.Francis Rogallo d. Galelio ",
    " World Blood Donar Day is observed on?\n a.14 june b.14 december c.24 june d.24 november ",
    " When is the World environment Day celebrated?\n a.3 june b.4june c.5june d.6june",
    " Which one of the following is not a true fish?\n a.Silver fish b.Saw fish c.Hammer fish d.Sucker fish",
    " Which team has won maximum number of ipl titles?\n a.CSK b.MI c.DD d.RR",
    " Which of the following is *not* written by Munshi Premchand? \n a.Gaban b.Godan c.Manasorovar d.Guide",
    " Who is the author of the book *WE INDIANS*? \n a.Khushwant Singh b.Mulk Raj Anand c.Nirad Chaudhary d.Shubham singh",
    " The book *Gullivers Travels* was written by?\n a.Charles Lamb b.Charles Dickens c.Alexander Dumas d.Jonathan Swift",
    " MS-Word is an example of ?\n a.Input device b.A processing device c.Application software d.An operating system",
    " the process of dividing the disk into tracks and sectors?\n a.Tracking b.Formatting c.Crashing d.Alloting",
    " Microsoft Office is an example of a?\n a.Closed source software b.Open source software c.Horizontal market software d.vertical market software ",
    " Nuclear sizes are expressed in a unit named?\n a.fermi b.newton c.eistein d. tesla",
    " The most suitable unit for expressing nuclear radius is?\n a.micro b.nanometre c.fermi d.angstrom",
    " The speed of light will be minimum while passing through?\n a.water b. air c.vaccum d.glass",
    " Which of the following is not a vector quantity?\n a.speed b.torque c.velocity d.displacement",
    " Who was the first Chairman of the SAARC?\n a.Mr. Zia ur Rehman b.Lt.Gen H.M.Ershad c. King Birendra d.Mrs.Indira Gandhi",
    " India is not a member of ?\n a.G-20 b.G-8 c.SAARC d.U.N",
    " Which kind of power accounts for the largest share of power generation in India?\n a.Hydro-electricity b.Thermal c.Nuclear d.Solar",
    " In India, Agriculture income is calculated by?\n a.Output method b.Input method c.Expenditure method d.Commodity flow method",
    " What is the full form of GDP?\n a.Gross domestic product b. Global domestic Ratio c.Gross depository revenue d.Global depository receipts",
    " Name the first Indian businessman who found place in the cover story of Forbes magazine?\n a.Anil Ambani b.Dr Reddy c.Azim Hasham Premji d. Narayan Murthy",
    " Which company uses tagline *Drive your way*?\n a.Yamaha b.Toyota c.Erickson d.Hyundai",
    " Which Company has launched 'Citizen First' advertisement campaign??\n a.Infosys b.NGC c.ITC d.Reliance ",
    " Union Budget is always presented first in?\n a.Lok Sabha b.The Rajya Sabha c.Joint session of the Parliament d.Meeting of the Union Cabinet",
    " The tropic of cancer does not pass through which of these Indian states?\n a.MP b.UP c.HP d.Odisha",
    " Which river of India is called Vridha Ganga?\n a.Krishna b.Godavari c.Kaveri d.Narmada",
    " Which foreign country is closest to Andaman Islands?\n a.Sri Lanka b.Indonesia c.Myanmar d.Pakistan ", 
    " India lies in the hemisphere?\n a.Northern and eastern b.Southern and eastern c.Northern and western d.Southern and western",
    " The first news paper in the world was started by ?\n a.India b.China c.USA d.Japan", 
    " Who is known as Man of Blood and Iron ?\n a. Napoleon b.Bismarck c.Ho Chi Minh d.Sir Walter Scott",
    " Who is considered as the master of Greek comedy ?\n a.Sophocles b.Aristophanes c.Philip d.Aeschylus",
    " Worlds highest railway bridge will be constructed on which river?\n a.Ganga b.Yamuna c.Chenab d. Kaveri" 
]

answers = ['a','a','b','d','a','b','c','b','a','c','a','c','b','b','c','c','a','c','a','a','c','d','b','d','a','d','c','b','c','a','c','d','a','b','b','b','a','a','c','d','c','a','d','b','c','a','b','b','b','c']



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = SERVER_PORT
s.bind(('',port))
s.listen(NUMBER_OF_CLIENTS) 

clients = [0]*NUMBER_OF_CLIENTS

for i in range(NUMBER_OF_CLIENTS): 
    clients[i], addr = s.accept()
    clients[i].send(str(i))
    print ("connection has been setup between player ",i,"and the client.")

time.sleep(0.001) 

for i in range(NUMBER_OF_CLIENTS):
    clients[i].send(str(WINNING_SCORE))
scoreboard = [0]*NUMBER_OF_CLIENTS
time.sleep

def get_ques():
    number=random.randint(0,10000)%len(questions)
    ques=questions[number]
    ans=answers[number]
    questions.pop(number)
    answers.pop(number)
    return ques,ans

def none_pressed(trueAnswerStr):

    for i in range(NUMBER_OF_CLIENTS):
        s = clients[i]
        s.send("no one")
    
    for s in clients:
        s.setblocking(1)
    time.sleep(0.1)
    givenAnswer = "None given"

    for i in range(NUMBER_OF_CLIENTS):
        clients[i].send(givenAnswer)
    time.sleep(0.01)

    givenAnswer = (givenAnswer.lower()).split()

    check = False

    for s in clients:
        s.send("Incorrect!")
    

    tallyStr = '' 
    time.sleep(0.01)

    for i in scoreboard:
        tallyStr += ' ' + str(i)

    for s in clients:
        s.send(trueAnswerStr)
        time.sleep(0.01)
        s.send(tallyStr)
        
    time.sleep(0.01)
    
    for s in clients:
        s.send("1")


def end_game():           
    time.sleep(0.01)
    for i in range(NUMBER_OF_CLIENTS):
        if scoreboard[i] == WINNING_SCORE or scoreboard[i]==WINNING_SCORE+0.5:
            clients[i].send("Congratulations,You are a true champ!")
        else:
            clients[i].send("Better Luck next time,You lose!")
    exit()

def start_game():
    while True: #game loop
        
        time.sleep(0.001)
        buzzed = -1 
        
        question,trueAnswerStr = get_ques()
        trueAnswer = (trueAnswerStr.lower()).split()
        for s in clients:
            s.send(question)
        for s in clients:
            s.setblocking(0)

        initial_time=int(time.time())
        while True:

            r, w, x = select.select(clients, [], [], 0)
            if r:
                s = r[0]
                buzzed = s.recv(1024)
                break
            elif (int(time.time())-initial_time>=10):
                none_pressed(trueAnswerStr)
                start_game()
                end_game()

                
            
        
        buzzed = int(buzzed)
        print "Player", buzzed, "buzzed."

        for i in range(NUMBER_OF_CLIENTS):
            s = clients[i]
            if i != buzzed:
                s.send("Player" + str(buzzed) + " press the buzzer.")
            else:
                s.send("You pressed the buzzer.")
        
        for s in clients:
            s.setblocking(1)
        time.sleep(0.1)
        givenAnswer = (clients[buzzed]).recv(1024)
        print "Given answer: ", givenAnswer

        for i in range(NUMBER_OF_CLIENTS):
            if i != buzzed:
                clients[i].send(givenAnswer)
        time.sleep(0.01)

        givenAnswer = (givenAnswer.lower()).split()

        check = True

        print trueAnswer, givenAnswer

        for i in trueAnswer:
            if not (i in givenAnswer):
                check = False
                break

        if check:
            print "Answered correctly."
            for s in clients:
                s.send("Correct!")
            scoreboard[buzzed]+=1
        else:
            print "Answered incorrectly."
            for s in clients:
                s.send("Incorrect!")
            scoreboard[buzzed]-=0.5
        

        tallyStr = ''
        time.sleep(0.01)

        for i in scoreboard:
            tallyStr += ' ' + str(i)

        for s in clients:
            s.send(trueAnswerStr)
            time.sleep(0.01)
            s.send(tallyStr)
            
        time.sleep(0.01)
        
        if(WINNING_SCORE in scoreboard or (WINNING_SCORE+0.5) in scoreboard):
            for s in clients:
                s.send("0")
            break
        else:
            for s in clients:
                s.send("1")

start_game()
end_game()
