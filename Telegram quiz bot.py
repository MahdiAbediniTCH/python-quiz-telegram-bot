from time import clock
from telepot.namedtuple import KeyboardButton,ReplyKeyboardMarkup
import telepot as t
#attention : dont change array '' in lists.
k=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='start test')]])
k1=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='try again')]])
start=0
lis=['']
lis1=['','5*6',
      '2+2','4*3','80*100','200*300','123*534','872*634','1024*2048','1*1','80-423']#strings are the questions
lis2=['',ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='11'),KeyboardButton(text='30')],[KeyboardButton(text='65'),KeyboardButton(text='56')]]),
      ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='42'),KeyboardButton(text='0')],[KeyboardButton(text='22'),KeyboardButton(text='4')]]),
      ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='12'),KeyboardButton(text='34')],[KeyboardButton(text='43'),KeyboardButton(text='7')]]),
      ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='8100'),KeyboardButton(text='180')],[KeyboardButton(text='80000'),KeyboardButton(text='8000')]]),
      ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='300200'),KeyboardButton(text='43')],[KeyboardButton(text='230'),KeyboardButton(text='60000')]]),
      ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='54321'),KeyboardButton(text='534123')],[KeyboardButton(text='123534'),KeyboardButton(text='65682')]]),
      ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='552848'),KeyboardButton(text='872634')],[KeyboardButton(text='635872'),KeyboardButton(text='65432')]]),
      ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='10242048'),KeyboardButton(text='2^21')],[KeyboardButton(text='2^110'),KeyboardButton(text='765432')]]),
      ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='0'),KeyboardButton(text='2')],[KeyboardButton(text='11'),KeyboardButton(text='1')]]),
      ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='-343'),KeyboardButton(text='343')],[KeyboardButton(text='503'),KeyboardButton(text='-503')]])
      ]
# about lis2 : strings are choices(to answer)
lis3=['','30','4','12','8000','60000','65682','552848','2^21','1','-343']#list of right answers
start_time=None
def main(ms):
    global lis
    global start
    global start_time
    i=ms['chat']['id']
    c=ms['text']
    print(ms['from']['username'],' : ')
    print(c)
    if c=='/start':
        bot.sendMessage(i,'Test',reply_markup=k)#name of test
    if c=='start test' or c=='try again':
        start=1
        start_time=clock()
    if start and start<12:#number of questions-2
        if c!='start test' and c!='try again':
            lis.append(c)
        if start<11:
            bot.sendMessage(i,lis1[start],reply_markup=lis2[start])
        else:
            end_time=clock()
            timer=int(end_time-start_time)
            start=0
            co=0
            no=-1
            for i in lis:
                if i==lis3[co]:
                    no=no+1
                co=co+1
            timerer=timer
            if timer>=70:#note : formula can be changed depends on hardness and number of question
                final_score=no*5
            else:
                if timer<30:
                    timer=30
                final_score=no*(70-timer)/4
            if final_score>100:
                final_score=100
            lis=['']
            bot.sendMessage(ms['chat']['id'],'Time : '+str(int(timerer))+' seconds \n Number of write answers : '+str(no)+'/10 \n Final score : '+str(int(final_score))+'/100',reply_markup=k1)
        if start!=0:
            start=start+1
bot=t.Bot('605459910:AAGZJcgAE9PPKvvVxYCuUwn7xVs-C5w-pw0')
bot.message_loop(main)
while True:
    s=1
