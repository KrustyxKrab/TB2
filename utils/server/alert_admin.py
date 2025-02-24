from ofunctions.mailer import Mailer
import streamlit as st

def alert_admin():

    recipients = st.secrets['admin_mail']

    mailer = Mailer(smtp_server = st.secrets['mail_server'], smtp_port = 465, security = 'ssl', debug = True,
                    verify_certificates = False)
    mailer.send_email(subject = 'test', sender_mail = st.secrets["sender_mail"], recipient_mails = recipients,
                      body = 'some body just told me', split_mails = True)
