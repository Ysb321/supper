from git import Repo

# Clone a repository
repo_url = 'https://github.com/AUTOMATIC1111/stable-diffusion-webui'
local_path = './destination_folder'
Repo.clone_from(repo_url, local_path)

# The repository has been cloned successfully
print("Repository cloned successfully! 😄")
