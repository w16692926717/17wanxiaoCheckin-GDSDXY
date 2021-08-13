from login.denglu import initLogging, check_in
import logging
from xinxi import server

def main_handler(*args, **kwargs):
    initLogging()
    raw_info = []
    username_list = [""]  #  完美校园APP登录时使用的手机号
    password_list = [""]  #  完美校园APP登录时使用的密码
    device_id_list = [""]  #  虚拟设备ID
    sckey = ""   #  Server 酱接收人的KAY
    key = ""  #  Qmsg的KEY
    qq_num = ""  #  QQ号
    send_email = ""  #  发送邮件的邮箱
    send_pwd = "bjvdhtjzvpuvbeaa"  #  去邮箱后台开启服务：POP3/SMTP服务生成的密码
    receive_email = ""  #  接收邮件的邮箱
    for username, password, device_id in zip(
            [i.strip() for i in username_list if i != ''],
            [i.strip() for i in password_list if i != ''],
            [i.strip() for i in device_id_list if i != '']):
        check_dict = check_in(username, password, device_id)
        raw_info.extend(check_dict)
    if sckey:
        logging.info(server.wanxiao_server_push(sckey, raw_info))
    if send_email and send_pwd and receive_email:
        logging.info(server.wanxiao_qq_mail_push(send_email, send_pwd, receive_email, raw_info))
    if key:
        logging.info(server.wanxiao_qmsg_push(key, qq_num, raw_info, send_type="send"))

if __name__ == "__main__":
    main_handler()
