import smtplib
import credentials
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#store the credientials in environment variables for security
username=credentials.username
password=credentials.password

def send_mail(text,subject,from_email,to_emails,html=None):
    assert isinstance(to_emails,list)
    msg=MIMEMultipart('alternative')
    msg['From']=from_email
    msg['To']=', '.join(to_emails)
    msg['Subject']=subject

    txt_part=MIMEText(text,'plain')
    msg.attach(txt_part)
    
    if html !=None:
        html_part=MIMEText("<h1>This is working</h1>",'html')
        msg.attach(html_part)
    
    msg_str=msg.as_string()
    
    #login to my smtp server
    server=smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(from_email,to_emails,msg_str)
    server.quit()

if __name__=='__main__':
    print('From : {}'.format(username))
    recievers=input('To : ').split()
    sub=input('Subject here : ')
    text=input('Body : ')
    try:
        send_mail(text,sub,'Abhishek Mulik <{}>'.format(username),recievers)     
        print('Mail sent successfully!!!')
    except:
        print('Try Again!!!')