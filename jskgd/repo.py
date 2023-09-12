import subprocess

repo_url = 'https://github.com/AUTOMATIC1111/stable-diffusion-webui'
destination_path = '/content/Repo'

# Run the git clone command
try:
    subprocess.run(['git', 'clone', repo_url, destination_path], check=True)
    print('Clone operation completed successfully! 😄')
except subprocess.CalledProcessError:
    print('Clone operation failed! 😞')
