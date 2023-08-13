'''Build for Android
'''

import os
import sys
import shutil

script_dir = os.path.dirname(__file__)
root_app_dir = os.path.abspath(script_dir + '/../..')
os.chdir(root_app_dir)

BUILD_DIR = root_app_dir + '/build'

try:
	os.makedirs(BUILD_DIR)
except FileExistsError:
	pass

try:
	os.remove(f'{BUILD_DIR}/buildozer.spec')
except (FileExistsError, FileNotFoundError):
	pass

shutil.copy('tools/build/buildozer.spec', f'{BUILD_DIR}/buildozer.spec')
shutil.copy('tools/build/requirements.txt', f'{BUILD_DIR}/')
shutil.copy('tools/build/requirements_build_android.txt', f'{BUILD_DIR}/')
os.chdir(BUILD_DIR)

commands = [
	f'{sys.executable} -m pip install docopts',
	f'{sys.executable} -m pip install -r requirements_build_android.txt',
	f'{sys.executable} -m buildozer -v android debug']

import subprocess
for cmd in commands:
	subprocess.run(cmd.split(' '))