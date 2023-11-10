class EmailService:
    def send(self, message, receiver):
        print(f"Sending email: {message} to {receiver}")


class SmsService:
    def send(self, message, receiver):
        print(f"Sending SMS: {message} to {receiver}")


class NotificationService:
    def __init__(self, service):
        self.service = service


    def send_notification(self, message, receiver):
        self.service.send(message, receiver)


email_chanal = EmailService()
sms_chanal = SmsService()
notification_service_email = NotificationService(email_chanal)
notification_service_sms = NotificationService(sms_chanal)

notification_service_email.send_notification("Hello", 'glazglojon@gmail.com')
notification_service_sms.send_notification('World', "+380663737524")
