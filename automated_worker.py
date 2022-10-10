import multiprocessing
from WebServersMonitoring import WebServersMonitoring
import requests
import time


def get_status(webserver):
    while True:
        start_time = time.perf_counter()
        try:
            resp = requests.get(url=webserver[1])
            status = 'success' if time.perf_counter() - start_time < 60 and resp.status_code == 200 else 'fail'
            WebServersMonitoring.request(webserver[0], status)

            statuses = WebServersMonitoring.read_webserver(webserver[0])
            if all(item[0] == 'success' for item in statuses[1:6]):
                WebServersMonitoring.update_webserver(old_name=webserver[0], new_health_status='Healthy')

            elif all(item[0] == 'fail' for item in statuses[1:4]):
                WebServersMonitoring.update_webserver(old_name=webserver[0], new_health_status='Unhealthy')

        except requests.ConnectionError:
            print("failed to connect")
        end_time = time.perf_counter()
        if end_time - start_time < 60:
            time.sleep(60 - (end_time - start_time))


if __name__ == '__main__':
    webservers_old = set()
    processes = {}
    while True:
        webservers_new = set([(webserver[0], webserver[1]) for webserver in WebServersMonitoring.get_all()])
        to_kill = webservers_old - webservers_new
        to_add = webservers_new - webservers_old
        webservers_old = webservers_new

        for webserver in to_add:
            process = multiprocessing.Process(target=get_status, args=(webserver,))
            processes[webserver[0]] = process
            process.start()
        for webserver in to_kill:
            process = processes[webserver[0]]
            process.terminate()

        time.sleep(60)
