import os
import shutil
import subprocess

ERROR = "[\x1b[1;31mERROR\x1b[0m]"
SUCCESS = "[\x1b[1;32mOK\x1b[0m]"
INFO = "[\x1b[1;33mINFO\x1b[0m]"


TO_DELETE = [
    f'{% if not cookiecutter.sentry %}{{cookiecutter.package_dir}}/common/clients/sentry.py{% endif %}',
]

def delete_unused_files():
    print(f"{INFO} Deleting unused files...")
    for path in TO_DELETE:
        path = path.strip()
        if path and os.path.exists(path):
            print(f"{INFO}\t\t• Deleting {path}", end=" ")
            os.unlink(path) if os.path.isfile(path) else shutil.rmtree(path)
            print(f"{SUCCESS}")
    print(f"{SUCCESS} Deleted all the unused files")


def run_cmd(cmd: list[str], description: str) -> bool:
    try:
        subprocess.run(cmd, capture_output=True, check=True)
        print(f"{SUCCESS} {description}")
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        print(f"{ERROR} {description} failed")
        return False


print(f"{SUCCESS} Sucesfully created {{cookiecutter.repo_dir}} directory")

delete_unused_files()

shutil.copy("env.sample", ".env")
print(f"{SUCCESS} Copied env.sample to .env")

run_cmd(["git", "init"], "Initialized git repository")
print(f"{INFO} Installing dependencies, wait a moment...")
run_cmd(["poetry", "install"], "Installed dependencies")
run_cmd(["poetry", "run", "pre-commit", "install"], "Installed pre-commit hooks")
run_cmd(["poetry", "run", "black", "."], "Formatted with black")
run_cmd(["poetry", "run", "isort", "."], "Formatted with isort")
run_cmd(["git", "add", "."], "Staged files for commit")
print(f"{INFO} Commiting files, might take a moment because of the pre-commit hooks...")
run_cmd(["git", "commit", "-m", "Initial commit"], "Committed files")
print(f"{SUCCESS} Succesfully created project, now you can start developing!")