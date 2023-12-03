from celery import shared_task
import time 

@shared_task
def send_build_emails(n):
    time.sleep(10)
    for x in range(n):
        print(f"Sending email to {x}")


