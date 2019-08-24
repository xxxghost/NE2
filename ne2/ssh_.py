import paramiko
import time
def ssh2(ip,username,passwd,cmd):

        result = []
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, passwd, timeout=1)
        chan = ssh.invoke_shell()
        print ("ssh ok")
        cmd.append(str('\n'))
        print(cmd)
        for key in cmd:
            output = chan.recv(-1)
            chan.send(key+'\n')
            output=str(output).split('\r\n', -1)
            #output = output.split('\r\n', -1)
            result.append(output)
            time.sleep(1)
        chan.close()
        return result

