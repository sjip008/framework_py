# -*- coding: utf-8 -*-
import logging
import datetime

from celery import task
from celery.task import periodic_task

import base64


def base64_encode(string):
    """
    对字符串进行base64编码
    """
    return base64.b64encode(string).decode("utf-8")


from blueapps.account.models import User
from blueking.component.shortcuts import get_client_by_user

user = User.objects.get(username='314629925')
client = get_client_by_user(user)

script_content = base64_encode(b"df -h / | sed -e '1d' |awk '{if($5>0) print $5}'")
script_param = base64_encode(b'/')

ip_list = [{
    "bk_cloud_id": 0,
    "ip": '10.0.1.80'
}]


def fast_execute_script(client, script_content, script_param, ip_list):
    """
    快速执行脚本函数
    """
    kwargs = {
        'bk_app_code': 'hsqapp1',
        'bk_app_secret': 'a2531495-82e2-44e8-8e70-a0bfb6a0354e',
        # 'bk_token': 'a2531495-82e2-44e8-8e70-a0bfb6a0354e',
        'bk_username': '314629925',
        'ip_list': ip_list,
        'bk_biz_id': 4,
        'script_content':script_content,
        'script_param':script_param

    }
    return client.job.fast_execute_script(kwargs)


FORMAT = "%(asctime)s %(thread)d %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt="[%Y-%m-%d %H:%M:%S]")

logger = logging.getLogger('config')


@task()
def get_capacity_task():
    """
    定义一个获取磁盘使用率异步任务
    """
    fast_execute_script_result = fast_execute_script(client, script_content, script_param, ip)

    logger.info('disk usage work end')


@periodic_task(run_every=datetime.timedelta(seconds=3))
def get_disk_periodic():
    """
    获取磁盘使用率周期执行定义
    """
    get_capacity_task.delay()
    logger.info('get disk work starting')
