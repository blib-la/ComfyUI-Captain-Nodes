import subprocess
import os
import pkg_resources

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
        parts = requirement.split('==')
        if len(parts) < 2:
            print(f"Captain says: Skipping improperly formatted requirement: {requirement}")
            continue
        package_name, required_version = parts
        installed_version = installed_packages.get(package_name)

        if not installed_version or pkg_resources.parse_version(installed_version) < pkg_resources.parse_version(required_version):
            packages_to_install.append(requirement)

    if packages_to_install:
        try:
            subprocess.check_call(['pip', 'install'] + packages_to_install)
            print(f"Captain says: Installed packages successfully: {', '.join(packages_to_install)}")
        except subprocess.CalledProcessError as e:
            print(f"Captain says: Failed to install some dependencies. Error: {e}")
    else:
        print("Captain says: All dependencies are already satisfied.")

install_dependencies()
