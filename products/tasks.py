from celery import shared_task
from celery.decorators import periodic_task
from celery.task.schedules import crontab


@shared_task
def do_some_task(params):
    # the task required to be done periodically written here using the passed params
    pass


@periodic_task(run_every=(crontab(minute='*/1')))
def recrusive_save():
    do_some_task.delay(params='param_data')
