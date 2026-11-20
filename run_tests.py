import subprocess
import os

# Change to the P10 directory
dir_path = r'C:\Users\pc\Documents\M1\IACS\Project_EthicalHacking\aegis-p10-deepfake-light'
result = subprocess.run(
    [os.path.join(dir_path, '.venv', 'Scripts', 'python.exe'), '-m', 'pytest', 'tests/', '-v'],
    cwd=dir_path,
    capture_output=True,
    text=True
)
print('STDOUT:', result.stdout[-500:])
print('STDERR:', result.stderr[-500:])
print('Return code:', result.returncode)