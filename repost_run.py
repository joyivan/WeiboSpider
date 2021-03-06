# 获取转发信息# -*-coding:utf-8 -*-
from multiprocessing import Process, Manager
from time import sleep, ctime
from get_cookie import get_session
from task.repost import get_all
from logger.log import other


if __name__ == '__main__':
    is_sleep = 1
    while 1:
        mgr = Manager()
        d = mgr.dict()
        pw = Process(target=get_session, args=(d,))
        pw.daemon = True
        pr = Process(target=get_all, args=(d,))
        other.info('本轮抓取开始,开始时间为{endtime}'.format(endtime=ctime()))

        try:
            pw.start()
            pr.start()
        except Exception as e:
            other.error(e)
            is_sleep = 0

        pr.join()

        pw.terminate()
        other.info('本轮抓取已经结束,结束时间为{endtime}'.format(endtime=ctime()))
        # 使其可以更新状态
        pw.join()

        if is_sleep:
            sleep(2*60*60)



