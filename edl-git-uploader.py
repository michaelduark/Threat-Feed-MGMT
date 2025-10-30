import os
import git
import logging

# Define repository path and URL
repo_path = '/scripts/python3/timfeeds'
repo_url = 'https://git.uark.edu/net-automation/timfeeds.git'

# Define the symlink files to upload
file_list = ['IPs.txt', 'FQDNs.txt']

# Set up logging
logging.basicConfig(filename='git_upload.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

try:
    # Clone the repository to the local machine
    if not os.path.exists(repo_path):
        git.Repo.clone_from(repo_url, repo_path)
        logging.info(f"Repository cloned from {repo_url} to {repo_path}")

    # Open the repository
    repo = git.Repo(repo_path)

    # Add the specified symlink files to the index
    for file_name in file_list:
        file_path = os.path.join(repo_path, file_name)
        if not os.path.exists(file_path):
            logging.warning(f"{file_name} does not exist")
            continue
        repo.index.add([file_path], follow_symlinks=True)
        logging.info(f"{file_name} added to the index")

    # Commit the changes
    if repo.index.diff("HEAD"):
        repo.index.commit("Added symlink files")
        logging.info("Changes committed")
    else:
        logging.warning("No changes to commit")

    # Push the changes to the remote repository
    origin = repo.remote(name='origin')
    origin.push()
    logging.info("Changes pushed to remote repository")

except Exception as e:
    logging.error(str(e))
    raise
