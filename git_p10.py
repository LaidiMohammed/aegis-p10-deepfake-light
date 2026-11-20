import subprocess
import os

dir_path = r'C:\Users\pc\Documents\M1\IACS\Project_EthicalHacking\aegis-p10-deepfake-light'

# Reset
subprocess.run(['git', 'reset', 'HEAD', '--', '.'], cwd=dir_path, capture_output=True, text=True)

# Add files
files = [
    'src/deepfake_light_main.py',
]
for f in files:
    full = os.path.join(dir_path, f)
    if os.path.exists(full):
        subprocess.run(['git', 'add', f], cwd=dir_path, capture_output=True, text=True)
        print(f"Added: {f}")

# Commit
result = subprocess.run(['git', 'commit', '-m', 'feat(P10): detection deepfake légère (AEGIS P10)'], 
                       cwd=dir_path, capture_output=True, text=True)
print("Commit:", result.stdout.strip())

# Push
result = subprocess.run(['git', 'push'], cwd=dir_path, capture_output=True, text=True)
print("Push STDERR:", result.stderr[-200:])