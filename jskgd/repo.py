import subprocess

repo_url = 'https://github.com/AUTOMATIC1111/stable-diffusion-webui'

# Run the git clone command
try:
    subprocess.run(['git', 'clone', repo_url], check=True)
    print('Clone operation completed successfully! 😄')
except subprocess.CalledProcessError:
    print('Clone operation failed! 😞')
