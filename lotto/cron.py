from crontab import CronTab


def renewer_weekend():
    print("run")

    cron = CronTab(user='username')
    job = cron.new(command="python manage.py crontab run renewer_weekend")
    job.setail('* * * * *')
    cron.write()