import subprocess
command="netsh wlan show profiles"
output=subprocess.check_output(command,shell=True).decode()
print(output)