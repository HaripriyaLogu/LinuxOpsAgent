import paramiko


class LinuxSSHClient:
    def __init__(self, host, username, key_path):
        self.host = host
        self.username = username
        self.key_path = key_path

    def execute_command(self, command):
        ssh = paramiko.SSHClient()

        # Automatically trust the server's SSH key
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the VM
        ssh.connect(
            hostname=self.host,
            username=self.username,
            key_filename=self.key_path
        )

        # Execute command
        stdin, stdout, stderr = ssh.exec_command(command)

        output = stdout.read().decode()
        error = stderr.read().decode()

        ssh.close()

        return output, error