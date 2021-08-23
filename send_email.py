import smtplib

email = "bilgeaiasistan@gmail.com"
password = "bilgeaiasistan2021"

def send_email(target, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()   
        server.login(email, password)
        to = [target]
        subject = 'Bilge Asistan Tarafından Gönderilen Mesaj'
        fmt = 'From: {}\r\nTo: {}\r\nSubject: {}\r\n{}'
        server.sendmail(email, to, fmt.format(to, email, subject, message).encode('utf-8'))
        server.close()
        return True
    
    except:
        return False
    
