import subprocess
p = subprocess.Popen('du')
print "[Before wait] Return Code", p.returncode
p.wait()
print "[After wait] Return Code", p.returncode
