from celery import Celery

celery = Celery("pix_mail", include=['src.tasks'])
