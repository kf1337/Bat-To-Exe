import subprocess
import os

# Path to your batch file
batch_file = 'build'

# Extract the base name without extension
base_name = os.path.splitext(batch_file)[0]

# Create a temporary Python script to run the batch file
python_script = f"""
import subprocess

batch_file = '{batch_file}'
subprocess.run(batch_file, shell=True)
"""

# Save the temporary Python script
with open('run_batch.py', 'w') as file:
    file.write(python_script)

# Use PyInstaller to convert the Python script to an executable
subprocess.run(['pyinstaller', '--onefile', '--name', base_name, 'run_batch.py'])

# Clean up the temporary Python script and build files
os.remove('run_batch.py')
os.remove(f'{base_name}.spec')
os.rmdir('build')
os.rmdir('dist')

print(f"Executable '{base_name}.exe' created successfully!")
