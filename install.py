import os
import subprocess
import pkg_resources
import sys

def get_pip_commands():
    if "python_embeded" in sys.executable or "python_embedded" in sys.executable:
        pip_install = [sys.executable, '-s', '-m', 'pip', 'install']
        pip_upgrade = [sys.executable, '-s', '-m', 'pip', 'install', '-U']
    else:
        pip_install = [sys.executable, '-m', 'pip', 'install']
        pip_upgrade = [sys.executable, '-m', 'pip', 'install', '-U']
    return pip_install, pip_upgrade

def install_dependencies():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    requirements_path = os.path.join(dir_path, 'requirements.txt')

    if not os.path.exists(requirements_path):
        print("Captain says: requirements.txt not found in", dir_path)
        return

    with open(requirements_path, 'r') as file:
        requirements = [line.strip() for line in file if line.strip() and not line.startswith('#')]

    installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
    packages_to_install = []

    for requirement in requirements:
        try:
            req = pkg_resources.Requirement.parse(requirement)
            package_name = req.key
            required_version = req.specs[0][1] if req.specs else None
            installed_version = installed_packages.get(package_name)

            if not installed_version or (required_version and pkg_resources.parse_version(installed_version) < pkg_resources.parse_version(required_version)):
                packages_to_install.append(requirement)
        except Exception as e:
            print(f"Captain says: Skipping improperly formatted requirement: {requirement}. Error: {e}")

    if packages_to_install:
        pip_install, _ = get_pip_commands()
        try:
            print(f"Captain says: Installing packages: {', '.join(packages_to_install)}")
            subprocess.check_call(pip_install + packages_to_install)
            print(f"Captain says: Installed packages successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Captain says: Failed to install some dependencies. Error: {e}")
    else:
        print("Captain says: All dependencies are already satisfied.")

install_dependencies()
