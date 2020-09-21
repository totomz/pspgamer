import logging
import multiprocessing
import socket
import sys
from multiprocessing import Pool, Queue

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)])
ilog = logging.getLogger("master")


def create_logger():
    import multiprocessing, logging
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('    --> %(processName)s - %(message)s'))

    # this bit will make sure you won't have
    # duplicated messages in the output
    if not len(logger.handlers):
        logger.addHandler(handler)
    return logger


# Generates a list of ip in the host LAN (eg 192.168.1.[1-255])
def ip_in_network():
    base = '.'.join(socket.gethostbyname(socket.gethostname()).split('.')[:-1])
    for i in range(1, 255):
        ip = f"{base}.{i}"
        yield ip


# Return true if {port} is open on the {host}
def port_check(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((host, port))
        s.close()
        return True
    except:
        s.close()
        return False


def scan_pool(ip, port, queue):
    log = create_logger()
    log.info(f"    --> PING {ip}")
    if port_check(ip, port):
        log.info(f"    --> PING {ip} OK")
        queue.put_nowait(ip)


# Return all the ip that have the port open
def ip_scan_for_port(port):
    log = create_logger()
    lan = list(ip_in_network())
    lan = lan[:5]
    manager = multiprocessing.Manager()
    results = manager.Queue()
    with Pool(processes=16) as pool:
        for ip in lan:
            res = pool.apply_async(scan_pool, (ip, port, results,))
        pool.close()
        pool.join()

    done = False
    ip_list = list()
    while not done:
        try:
            ip = results.get(block=True, timeout=2)
            ip_list.append(ip)
        except Exception:
            done = True

    log.info("Ciao")
    return ip_list


if __name__ == '__main__':
    ip_list = ip_scan_for_port(55000)
    for ip in ip_list:
        print(f"Ciocchino {ip}")
