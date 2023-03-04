#################
# compile-to-zipped-markdown.py
#
# Overview:
# This file consolidates the various model documentation files
# into a single Markdown file. It then saves that file, along with
# a directory of images cited in the original files, as a zip archive.
# 
# Output:
# Zip folder with 
#   - single model documentation Markdown file
#   - subdirectory of images
# Outputs zip folder to {your git repo}/docs/model_doc_src
# 
# Instructions:
# python docs/model_doc_src/doc-tools/compile-to-zipped-markdown.py
# 
# You can invoke this file from wherever. It will change your working 
# directory to handle its operations.
# 
#################

import re
import os
import shutil
import time

class stdout_colors:
    HEADER = '\033[95m'
    OKCYAN = '\033[96m'
    ENDC = '\033[0m'

def change_working_directory():

    '''
    Checks if script is being run from the same working directory
    as this file. Changes to this directory if not.
    '''
    global pwd
    pwd = os.getcwd()
    file_location = os.path.abspath(__file__)
    target_directory = os.path.dirname(file_location)

    if pwd != target_directory:
        os.chdir(target_directory)
        pwd = os.getcwd()

    return pwd

def get_project_name():

    global project_name
    print("")
    project_name = input(stdout_colors.OKCYAN + "Enter project name (no spaces, dash-separated): ")

def create_temp_output_folder():

    '''
    Creates a temporary output folder for output files.
    This is done to make the process of outputting the zip folder easier.
    '''
    global images_path
    global model_doc_single_file
    global output_path

    output_path = f'{pwd}/../output'
    images_path = f'{output_path}/images'
    model_doc_single_file = f"{output_path}/{project_name}-model-documentation.md"
        
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    if not os.path.exists(images_path):
        os.mkdir(images_path)

def concatenate_files():

    '''
    Concenates text from multiple Markdown files into a single string.
    Prerequisite to applying further processing changes with regex.

    This particular function assumes text is stored one directory above 
    current working directory and in a 'modeldocumentation' folder that
    is parallel to the present working directory.
    '''

    raw_text =""

    for file in os.listdir('../'):
        if file.endswith(".md"):
            with open(f"../{file}", 'r') as f:
                text = f.read()
                raw_text = raw_text + "\n" + text

    for file in os.listdir('../modeldocumentation'):
        if file.endswith(".md"):
            with open(f"../modeldocumentation/{file}", 'r') as f:
                text = f.read()
                raw_text = raw_text + "\n\n" + text

    return raw_text

def strip_help_text(text):

    '''
    Removes the various admonitiions (help text, examples, notes)
    from the raw combined Markdown string.

    Args: raw single Markdown (str)
    '''

    text = text
    result = re.sub(r'```\{admonition\}([a-zA-Z0-9_\s ]*)```', '', text)
    result = re.sub(r'(\n){3,}', '\n\n', result)
    stripped_text = result
    
    return stripped_text

def replace_string_variables(text):

    '''
    Determines whether the content reuse variables have been assigned within
    the conf.py's "html_context." If yes, replaces the variable with the 
    string value of the variable.

    Note that this will cause unexpected output if a non-string value has been 
    assigned to a variable in html_context (e.g., a Pandas dataframe). 

    Args: raw text (str)
    '''

    html_context = r'(html_context \{)\n+([a-zA-Z0-9\r\'\:\,\.\(\)\r\s\<\>\=\/\"]+)\}'

    with open ('../conf.py', 'r') as file:
            file_read = file.read()
            if re.findall(html_context, file_read):
                match = re.search(html_context, file_read).group(0)
                remove_html_context = re.sub(r'(html_context \{)(\n)', '', match)
                remove_bracket = re.sub(r'\}', '',remove_html_context)
                remove_tabs = re.sub(r'\s', '', remove_bracket)
                html_context_values = remove_tabs.split(',')
                file.close()

## Check for instances of variables being called in single text file
    for assignment in html_context_values:
        # Extract values defined in html_context
        array_match = assignment.split(":") 
        variable_name = array_match[0].replace("'", "")
        variable_value = array_match[1]  

        # Find values in the body of the text 
        text_variable_match = r'(\{\{)\s*'+ variable_name + r'\s*(\}\})'
        variable_present = re.search(text_variable_match, text)
        if variable_present:
            # Update text by rendering defined values
            text = re.sub(text_variable_match, variable_value, text)
    
    updated_text = text

    global output_path
    output_path = f'{pwd}/../output'

    return updated_text

def convert_images(text):

    '''
    Identifies images in compiled Markdown text, copies images from the 
    _static/ directory to a new, standalone images directory, and updates
    the image call in the Markdown

    Assumes images are stored in a _static/ directory that is parallel to
    the present working directory 

    Args: single, compiled Markdown text (str)
    '''
    text=text
    image_markdown_regex = r"(!\[[a-zA-Z0-9\'\:\,\.\(\)\s\<\>\=\/\"]+\](?:\(\.\.\/\_|\(\_)static\/[a-zA-Z0-9\'\:\,\.\(\)\s\<\>\=\/\-]+\))"
    images_path = f'{pwd}/../output/images'
    images_path_exists = os.path.exists(images_path)
    image_list = re.findall(image_markdown_regex, text)

    if not images_path_exists:
        os.mkdir(images_path)

    for image_original_markdown in image_list:
        image_markdown_alt_text_regex = r'(!\[[a-zA-Z0-9\'\:\,\.\(\)\r\s\<\>\=\/\"]+\])'
        image_alt_text = re.search(image_markdown_alt_text_regex, image_original_markdown).group(1)
        image_markdown_without_alt = re.sub(image_markdown_alt_text_regex, '', image_original_markdown)
        static_markup = r'(\(\.\.\/_static\/)|(\(_static\/)'
        file = re.sub(static_markup, '',image_markdown_without_alt)
        final_file = file.strip(')') # remove trailing close paranethesis
        shutil.copy(f'{pwd}/../_static/{final_file}', f'{images_path}/{final_file}') # copy files from _static/ to images/
        new_image_markdown = f'{image_alt_text}(images/{final_file})'
        text = text.replace(image_original_markdown, new_image_markdown)

    updated_text_with_images_converted = text

    return updated_text_with_images_converted

def convert_snippets(text):

    '''
    Identifies calls to content reuse ("doc-snippets") and replaces the 
    call with the value of the called text.

    Assumes doc-snippets are stored in a directory called 'doc-snippets' that
    is parallel to the present working directory.

    Args: raw text (str)
    '''

    text=text    
    snippets_regex = '(```\s*{include}\s*\/*doc-snippets\/[a-zA-Z0-9\:\,\.\(\)\s\<\>\=\/]+(?:.md|.rst)\s*```)'
    snippet_file_regex = '[a-zA-Z0-9\.\=\-]+(?:.md|.rst)'

    snippets_list= re.findall(snippets_regex, text)
    leading_include_regex = '(```\s*{include}\s*\/*doc-snippets/)'
    trailing_backtick_regex = '(?<=.md\n)```'
    pwd = os.getcwd()

    for snippet_call in snippets_list:
        trailing_backticks_removed = re.sub(trailing_backtick_regex, '', snippet_call)
        leading_include_removed = re.sub(leading_include_regex, '', trailing_backticks_removed)
        snippet_file = leading_include_removed.strip()
        with open(f'{pwd}/../doc-snippets/{snippet_file}') as snippet_file:
            snippet_source_text = snippet_file.read()
        text = text.replace(snippet_call, snippet_source_text)
    
    final_text = text

    return final_text

def output_single_markdown_file(final_text):

    final_text = final_text

    with open(f'{output_path}/{project_name}-model-documentation.md', 'w+') as output_file:
        output_file.write(final_text)
        output_file.close()

    return output_file


def create_zip_folder():

    '''
    Outputs a zip folder that contains the single Markdown file +
    a directory with the images cited in the Markdown file.
    '''

    shutil.make_archive(f'{pwd}/../{project_name}-model-documentation', format='zip', root_dir=f'{output_path}')

    print("")
    print(stdout_colors.OKCYAN + f"Condensed documentation available at: ")
    os.chdir("../")
    final_dir = os.getcwd()
    print(stdout_colors.HEADER + f'{final_dir}/{project_name}-model-documentation.zip' + stdout_colors.ENDC)
    print("")
    
def delete_temp_output_folder_and_single_file(output_file):

    '''
    Deletes the temporary folder that was created as a prereq to the 
    zip folder's creation.

    Args: location of the temporary folder (str).
    '''
    shutil.rmtree(output_path)

if __name__ == "__main__":

    get_project_name()
    change_working_directory()
    start = time.time()
    create_temp_output_folder()
    raw_text = concatenate_files()
    stripped_text = strip_help_text(raw_text)
    string_vars_replaced = replace_string_variables(stripped_text)
    images_converted = convert_images(string_vars_replaced)
    final_text = convert_snippets(images_converted)
    output_file = output_single_markdown_file(final_text)
    create_zip_folder()
    end = time.time()
    delete_temp_output_folder_and_single_file(output_file)
    print("")
    print("Compiled documentation in ", (end - start), " second(s).")
    print("")

