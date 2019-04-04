# import subprocess
# import sys
# port = "netstat -lntup|grep %s|wc -l" %sys.argv[1]
#
# def result(port):
#     obj=subprocess.Popen(port,
#                      shell=True,
#                      stdout=subprocess.PIPE,
#                      stderr=subprocess.PIPE
#                      )
#     port = obj.stdout.read().decode('gbk')
#     return port
# if __name__ == '__main__':
#     prot2 = int(result(port))
#     if prot2 == 0:
#         print('not ok,try Start it')
#         cmd='/usr/local/nginx/sbin/nginx'
#         result(cmd)
#         prot3 = int(result(port))
#         if prot3 == 0:
#             print('is not ok')
#         else:
#             print('ok')
#     else:
#         print('port is ok')

n = 0
while n < 10:
    n = n+1
    if n!=7:
        print(n)
