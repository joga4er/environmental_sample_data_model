"""Collection of useful linkml commands. Basically command line called via python. """

import os
import subprocess

def create_python_schema(yamlschema: str, pythonschema: str) -> None:
    """Creates python schema from yaml schema and imports python script.

    :param yamlschema: Name of .yaml schema.
    :type yamlschema: str
    :param data: Name of .py schema to be created.
    :type data: str
    """
    my_env = os.environ.copy()

    p = subprocess.Popen(
        ['gen-python', yamlschema, '>', pythonschema], shell=True, stderr=subprocess.PIPE, env=my_env,
        cwd=os.getcwd())
    _, error = p.communicate()
    if error is not None:
        print(error)
        return None
    else:
        print(f'Suceeded in converting yaml schema to python.')

def validate_data_to_schema(yamlschema: str, yamldata: str, ) -> None:
    """Validates .yaml data against linkml data schema.

    :param yamlschema: Name of .yaml schema.
    :type yamlschema: str
    :param yamldata: name of data to be validated
    :type yamldata: str
    """  

    #["linkml-validate -s", yamlschema, data]
    my_env = os.environ.copy()

    p = subprocess.Popen(
        ['linkml-validate', '-s', yamlschema, yamldata], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=my_env,
        cwd=os.getcwd())
    output, error = p.communicate()

    if error is not None:
        print(error)
    else:
        print(output)

def convert_data_to_csv(yamlschema: str, yamldata: str, ) -> None:
    """Validates .yaml data against linkml data schema.

    :param yamlschema: Name of .yaml schema.
    :type yamlschema: str
    :param yamldata: name of data to be validated
    :type yamldata: str
    """  

    #["linkml-validate -s", yamlschema, data]
    my_env = os.environ.copy()

    p = subprocess.Popen(
        ['linkml-convert', '-t', 'csv', '-s', yamlschema, yamldata, '>', 'outputs/data.csv'], shell=True, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, env=my_env,
        cwd=os.getcwd())
    output, error = p.communicate()
    if error is not None:
        print(error)
    else:
        print(output)
    
def generate_schema_png(yamlschema: str) -> None:
    """Generates sketch of data schema.

    :param yamlschema: Name of .yaml schema.
    :type yamlschema: str
    """
    my_env = os.environ.copy()

    p = subprocess.Popen(
        ['gen-yuml', '-f', 'png', '-d', 'outputs', '--diagram-name', 'schema', yamlschema], shell=True, stderr=subprocess.PIPE, env=my_env,
        cwd=os.getcwd())
    _, error = p.communicate()
    if error is not None:
        print(error)
    else:
        print(f'Suceeded in creating image for schema.')

def generate_schema_excel(yamlschema: str) -> None:
    """Generates excel file representing data schema.

    :param yamlschema: Name of .yaml schema.
    :type yamlschema: str
    """
    my_env = os.environ.copy()

    p = subprocess.Popen(
        ['gen-excel', yamlschema, '--output', 'outputs/schema.xlsx'], shell=True, stderr=subprocess.PIPE, env=my_env,
        cwd=os.getcwd())
    _, error = p.communicate()
    if error is not None:
        print(error)
    else:
        print(f'Suceeded in creating spreadsheet for schema.')