import re
import time
import subprocess
import os

ORIGINAL_FOLDER_NAME = 'django-base'
ORIGINAL_PROJECT_NAME = 'baseproject'
project_name = input("Nombre del proyecto: ")
project_url = input("URL del proyecto (git): ")


if re.fullmatch("[a-zA-Z0-9_]+(?<!_)$", project_name):

	print('-----------------------------------------------------------------------------')
	print('Configurando el proyecto')

	subprocess.run(['mv {0} {1}'.format(ORIGINAL_FOLDER_NAME, project_name)], shell=True)
	subprocess.run(['mv {0}/{1} {0}/{0}'.format(project_name, ORIGINAL_PROJECT_NAME)], shell=True)
	print('✓ Carpetas configuradas')

	files_to_replace = [
		'{0}/{0}/asgi.py'.format(project_name), 
		'{0}/{0}/wsgi.py'.format(project_name), 
		'{0}/{0}/settings.py'.format(project_name), 
		'{0}/manage.py'.format(project_name),
		'{0}/.coveragerc'.format(project_name),
		'{0}/.gitlab-ci.yml'.format(project_name),
		]

	for file_to_replace in files_to_replace:
		with open(file_to_replace, 'r') as file :
		  	filedata = file.read()

		# Replace the target string
		filedata = filedata.replace(ORIGINAL_PROJECT_NAME, project_name)

		# Write the file out again
		with open(file_to_replace, 'w') as file:
			file.write(filedata)

	time.sleep(1)
	print('✓ Nombre configurado')
	subprocess.run(['cd {0} && git remote set-url origin {1}'.format(project_name, project_url)], shell=True)
	time.sleep(1)
	print('✓ git configurado')
else:
	print('El nombre del proyecto no es válido, solo se aceptan letras, numeros o guiones bajos')