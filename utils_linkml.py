"""Collection of useful linkml commands. Basically command line called via python. """

import os
import subprocess
import pypandoc as docgenerator

from typing import Optional

my_env = os.environ.copy()

def create_python_schema(yamlschema: str, pythonschema: str) -> None:
    """Creates python schema from yaml schema and imports python script.

    :param yamlschema: Name of .yaml schema.
    :type yamlschema: str
    :param data: Name of .py schema to be created.
    :type data: str
    """
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

    p = subprocess.Popen(
        ['linkml-validate', '-s', yamlschema, yamldata], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=my_env,
        cwd=os.getcwd())
    output, error = p.communicate()

    if error is not None:
        print(error)
    else:
        print(output)

def convert_data_to_csv(yamlschema: str, yamldata: str, csvdata: str) -> None:
    """Validates .yaml data against linkml data schema.

    :param yamlschema: Name of .yaml schema.
    :type yamlschema: str
    :param yamldata: name of data to be validated
    :type yamldata: str
    :param csvdata: name/path of csv data to be generated
    :type yamldata: str
    """  

    #["linkml-validate -s", yamlschema, data]

    p = subprocess.Popen(
        ['linkml-convert', '-t', 'csv', '-s', yamlschema, yamldata, '>', csvdata], shell=True, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, env=my_env,
        cwd=os.getcwd())
    output, error = p.communicate()
    if error is not None:
        print(error)
    else:
        print(output)
    
def generate_schema_png(yamlschema: str, directory: str) -> None:
    """Generates sketch of data schema using yuml - not recommended, linkml does not continue to support it.

    :param yamlschema: Name of .yaml schema.
    :type yamlschema: str
    :param directory: Path/name of the directory the schema image should be saved in.
    :type directory: str
    """
    p = subprocess.Popen(
        ['gen-yuml', '-f', 'png', '-d', directory, '--diagram-name', 'schema', yamlschema], shell=True, stderr=subprocess.PIPE, env=my_env,
        cwd=os.getcwd())
    _, error = p.communicate()
    if error is not None:
        print(error)
    else:
        print(f'Suceeded in creating image for schema.')

def generate_schema_image_md(yamlschema: str, directory: str) -> None:
    """Generates scetch of data schema using mermaid and markdown.

    :param yamlschema: Name of .yaml schema.
    :type yamlschema: str
    :param directory: Path/name of the directory the schema image should be saved in.
    :type directory: str
    """
    p = subprocess.Popen(
        ['gen-erdiagram', yamlschema, '--follow-references'], shell=True, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, env=my_env, cwd=os.getcwd()
        )
    output, error = p.communicate()
    if error is not None:
        print(error)
    if output is not None:
        with open(os.path.join(directory,"schema_image.md"), "w") as f:
            f.write(f'# Schema image \n')
            f.write(output.decode('utf-8'))
            f.write('\n')
        print(f'Suceeded in creating image for schema.')


def generate_schema_image(yamlschema: str, directory: str) -> None:
    """Generates sketch of data schema.

    :param yamlschema: Name of .yaml schema.
    :type yamlschema: str
    :param directory: Path/name of the directory the schema image should be saved in.
    :type directory: str
    """
    p = subprocess.Popen(
        ['gen-yuml', '-f', 'png', '-d', directory, '--diagram-name', 'schema', yamlschema], shell=True, stderr=subprocess.PIPE, env=my_env,
        cwd=os.getcwd())
    _, error = p.communicate()
    if error is not None:
        print(error)
    else:
        print(f'Suceeded in creating image for schema.')

def generate_schema_excel(yamlschema: str, excelschema: str) -> None:
    """Generates excel file representing data schema.

    :param yamlschema: Name of .yaml schema.
    :type yamlschema: str
    :param excelschema: Directory and name of .xlsx schema to be generated
    :type yamlschema: str
    """
    p = subprocess.Popen(
        ['gen-excel', yamlschema, '--output', excelschema, '--include-mixins'], shell=True, stderr=subprocess.PIPE, env=my_env,
        cwd=os.getcwd())
    _, error = p.communicate()
    if error is not None:
        print(error)
    else:
        print(f'Suceeded in creating spreadsheet for schema.')

def generate_schema_documentation(
        yamlschema:str, directory: str, example_directory: Optional[str] = None
        ) -> None:
    """Generates documentation of data model.

    :param yamlschema: Name of .yaml schema.
    :type yamlschema: str
    :param directory: Directory where .doc file should be saved to
    :type directory: str
    :param example_directory: Directory where example data entry can be found.
    :type example_directory: str
    """    
    if example_directory is not None:
        p = subprocess.Popen([
            'gen-doc', '--subfolder-type-separation',
            '-d', directory, yamlschema, '--diagram-type', 'plantuml_class_diagram',
            '--example-directory', example_directory,
            ], shell=True, stderr=subprocess.PIPE, env=my_env, cwd=os.getcwd()
            )
    else:
        p = subprocess.Popen([
            'gen-doc', '--subfolder-type-separation',
            '-d', directory, yamlschema, '--diagram-type', 'plantuml_class_diagram',
            ], shell=True, stderr=subprocess.PIPE, env=my_env, cwd=os.getcwd()
            )
    _, error = p.communicate()
    if error is not None:
        print(error)
    else:
        print(f'Suceeded in creating spreadsheet for schema.')

    if os.path.isfile(os.path.join(directory, 'scema_image.md')):
        pass
        ### TODO: render mermaid markdown to either png or docx - current workaround: open with obsidian and save as image
        # docgenerator.convert_file(
        #     f'{directory}/schema_image.md','docx', outputfile=f'{directory}/schema_image.docx'
        # )

    docgenerator.convert_file(
        f'{directory}/index.md','docx', outputfile=f'{directory}/schema.docx'
        )
    docgenerator.convert_file(
        f'{directory}/classes/*.md','docx', outputfile=f'{directory}/details_classes.docx'
        )
    docgenerator.convert_file(
        f'{directory}/enums/*.md','docx', outputfile=f'{directory}/details_enums.docx'
        )
    docgenerator.convert_file(
        f'{directory}/slots/*.md','docx', outputfile=f'{directory}/details_slots.docx'
        )