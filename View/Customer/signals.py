import platform
import socket
from datetime import datetime
from Model.login_activity import LoginActivity
from Model import Global
from Controller.login_activity_dbms import store_login_details

def login_device_details():

    # TO FETCH THE CURRENT DATE AND TIME
    current_datetime = datetime.now()

    # TO FETCH THE DEVICE INFO
    device_type = platform.machine()
    os = platform.system()
    node_device_name = platform.node()
    processor = platform.processor()

    login_date = current_datetime.date()
    login_time = current_datetime.time()

    loginActivity = LoginActivity(device_type=device_type, os= os, processor=processor, node_device_name=node_device_name, login_date=login_date, login_time=login_time, user_id=Global.current_user[0])
    is_stored = store_login_details(loginActivity)

    return is_stored




