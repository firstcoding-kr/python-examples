import dns.resolver
import smtplib
from email.mime.text import MIMEText
# pip install dnspython

# 송신자 및 수신자 이메일 주소 설정
sender_email = "test@mail.firstcoding.kr"
receiver_email = "first-coding@naver.com"

# 수신자 도메인의 MX 레코드 조회
recipient_domain = receiver_email.split("@")[1]
mx_records = dns.resolver.query(recipient_domain, 'MX')
mx_record = str(mx_records[0].exchange)

# 이메일 내용 설정
subject = "테스트 이메일 발송"
body = "안녕하세요 테스트입니다."

msg = MIMEText(body)
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# MX 서버로 직접 소켓 통신을 통해 이메일 전송
try:
    smtp_server = smtplib.SMTP(mx_record, 25)
    smtp_server.sendmail(sender_email, receiver_email, msg.as_string())
    smtp_server.quit()
    print("메일이 성공적으로 전송되었습니다.")
except Exception as e:
    print(f"메일 전송 중 오류 발생: {str(e)}")
