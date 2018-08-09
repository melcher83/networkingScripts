import paramiko
import time
import getpass


def disable_paging(remote_conn):
    '''Disable paging on a Cisco router'''

    remote_conn.send("terminal length 0\n")
    time.sleep(1)

    # Clear the buffer on the screen
    output = remote_conn.recv(1000)

    return output


if __name__ == '__main__':

    # VARIABLES THAT NEED CHANGED
    ip = raw_input("IP: ")
    file_name = raw_input("Filename: ")
    username = raw_input("Username: ")
    password = getpass.getpass("Password: ")

    # Create instance of SSHClient object
    remote_conn_pre = paramiko.SSHClient()

    # Automatically add untrusted hosts (make sure okay for security policy in your environment)
    remote_conn_pre.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())

    # initiate SSH connection
    remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
    print "SSH connection established to %s" % ip

    # Use invoke_shell to establish an 'interactive session'
    remote_conn = remote_conn_pre.invoke_shell()
    print "Interactive SSH session established"

    # Strip the initial router prompt
    output = remote_conn.recv(1000)

    # See what we have
    print output

    # Turn off paging
    disable_paging(remote_conn)

    # Now let's try to send the router a command
    remote_conn.send("\n")
    remote_conn.send("sh run\n")

    # Wait for the command to complete
    time.sleep(2)
    full_filename = "c:\scripts\\" + file_name
    f = open(full_filename, 'w')
    rcv_timeout = 500
    interval_length = 0.1

    while (rcv_timeout > 0):
        if remote_conn.recv_ready():
            output += (remote_conn.recv(5000))

        else:
            rcv_timeout -= interval_length

    print output
    f.write(output)

    f.close()
