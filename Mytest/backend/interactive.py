import socket
import sys
import time
from paramiko.py3compat import u
from web01 import models
nocommond = {'cd','ls','ll'}
try:
    import termios
    import tty
    has_termios = True
except ImportError:
    has_termios = False


def interactive_shell(chan,hostinfo):
    if has_termios:
        posix_shell(chan,hostinfo)
    else:
        windows_shell(chan)


def posix_shell(chan,hostinfo):
    import select

    oldtty = termios.tcgetattr(sys.stdin)
    try:
        tty.setraw(sys.stdin.fileno())
        tty.setcbreak(sys.stdin.fileno())
        chan.settimeout(0.0)
        user_id = models.UserInfo.objects.get(username=hostinfo['user']).nid
        host_id = models.Host.objects.get(in_ip=hostinfo['ip']).id
        cmd = []
        #f = open('ssh_test.log','w')   # 创建操作日志文件写入，后面也可用表
        while True:
            r, w, e = select.select([chan, sys.stdin], [], [])
            if chan in r:
                try:
                    x = u(chan.recv(1024))
                    if len(x) == 0:
                        sys.stdout.write('\r\n*** EOF\r\n')
                        break
                    sys.stdout.write(x)
                    sys.stdout.flush()
                except socket.timeout:
                    pass
            if sys.stdin in r:
                x = sys.stdin.read(1)
                if len(x) == 0:
                    break
                if x == '\r':
                    #print('>>',''.join(cmd))
                    #log = "%s   %s\n" %(time.strftime("%Y-%m-%d %X", time.gmtime()), ''.join(cmd))
                    #f.write(log)
                    # 或
                    # 记录操作日志表信息
                    if len(cmd) !=0:
                        command=''.join(cmd)
                        if command.split(' ')[0] not in nocommond:
                            models.CommandIog.objects.create(user_id=user_id,host_id=host_id,command=command)
                    cmd = []
                else:
                    cmd.append(x)
                chan.send(x)
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)
        #f.close()



# windows_shell 该函数没有用
def windows_shell(chan):

    print("window chan",chan.host_to_user_obj)
    print("window chan",chan.crazyeye_account)
    import threading

    sys.stdout.write("Line-buffered terminal emulation. Press F6 or ^Z to send EOF.\r\n\r\n")

    def writeall(sock):
        while True:
            data = sock.recv(256)
            if not data:
                sys.stdout.write('\r\n*** EOF ***\r\n\r\n')
                sys.stdout.flush()
                break
            sys.stdout.write(data)
            sys.stdout.flush()

    writer = threading.Thread(target=writeall, args=(chan,))
    writer.start()

    try:
        while True:
            d = sys.stdin.read(1)
            if not d:
                break
            chan.send(d)
    except EOFError:
        # user hit ^Z or F6
        pass
