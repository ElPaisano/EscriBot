import re
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.text_splitter import MarkdownTextSplitter
from langchain.prompts import (
    ChatPromptTemplate, 
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate
)
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import UnstructuredMarkdownLoader


def load_doc(fname):
   loader = UnstructuredMarkdownLoader(fname, mode="elements")
   return loader.load()

def set_prompt(sys_template, user_template):
   system_message_prompt = SystemMessagePromptTemplate.from_template(sys_template)
   human_message_prompt = HumanMessagePromptTemplate.from_template(user_template)
   return ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

def chunk_MD_on_header(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()
    
    chunks = []
    current_chunk = ""
    
    for line in file_contents.splitlines():
        if line.startswith("#"):
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = line + "\n"
        else:
            current_chunk += line + "\n"
    
    if current_chunk:
        chunks.append(current_chunk)
    
    return chunks

def write_markdown_file(file_path, markdown_list):
    with open(file_path, "w") as file:
        for markdown_string in markdown_list:
            file.write(markdown_string + "\n")

def chunkIsProcedure(chunk):
   # Check if the text is a Markdown list using only "1. "
    pattern1 = r"^[ ]{0,3}1\.[ ]{1,}"
    if re.search(pattern1, chunk, flags=re.MULTILINE):
        return True

    # Check if the text is a Markdown list using sequential numbers
    pattern2 = r"^[ ]{0,3}\d+\.[ ]{1,}"
    if re.search(pattern2, chunk, flags=re.MULTILINE):
        return True

    # If neither pattern matches, the text is not a procedure
    return False

def extract_first_header_title(text):
    # Define the regular expression pattern for matching headers
    #pattern = r"^#\s+(.*)$"
    pattern = r"^(#+)\s+(.*)$"


    # Search for a match using the pattern and extract the header title
    match = re.search(pattern, text, flags=re.MULTILINE)
    if match:
        return match.group(2).strip()
    else:
        return "UNKNOWN SECTION TITLE"

def split_paragraphs(md_string):
    # Find the index of the first blank line after the header
    header_end = md_string.find('\n\n')
    if header_end == -1:
        header_end = len(md_string)

    # Split the text after the header on blank lines
    paragraphs = [p.strip() for p in md_string[header_end:].split('\n\n') if p.strip()]

    # Return the list of paragraphs
    return paragraphs

def split_on_first_step(markdown_str):
    # Split the string into lines
    lines = markdown_str.split('\n')

    # Find the index of the line that contains a step
    step_index = None
    for i, line in enumerate(lines):
        if line.strip().startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')):
            step_index = i
            break

    if step_index is not None:
        # If a step was found, split the markdown string into two parts
        before_step = '\n'.join(lines[:step_index-1])
        after_step = '\n'.join(lines[step_index-1:])

        # Remove any extra whitespace from the before_step string
        before_step = before_step.strip()

        # Return the two parts as a list of strings
        return [before_step, after_step]
    else:
        # If no step was found, return the entire markdown string as a list with a single string
        return [markdown_str]

def split_on_last_step(markdown_str):
    # Split the string into lines
    lines = markdown_str.split('\n')

    # Find the index of the line that contains the last step
    step_index = None
    for i in range(len(lines)-1, -1, -1):
        if lines[i].strip().startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')):
            step_index = i
            break

    if step_index is not None:
        # If a step was found, split the markdown string into two parts
        before_step = '\n'.join(lines[:step_index])
        after_step = '\n'.join(lines[step_index:])

        # Remove any extra whitespace from the before_step string
        before_step = before_step.strip()

        # Return the two parts as a list of strings
        return [before_step, after_step]
    else:
        # If no step was found, return the entire markdown string as a list with a single string
        return [markdown_str]

def prune_procedure(markdown_str):
    # Split the string into lines
    lines = markdown_str.split('\n')

    # Remove empty lines and image lines
    cleaned_lines = []
    for line in lines:
        if not line.strip() or line.strip().startswith('!['):
            continue
        else:
            cleaned_lines.append(line)

    # Join the remaining lines into a single string and return it
    cleaned_markdown = '\n'.join(cleaned_lines)
    return cleaned_markdown

def create_report_comment(chunk):
   aiMsg4Para = chat(proc_chat_prompt.format_prompt(section = chunk).to_messages())
   resp = str(aiMsg4Para.content)
   report_list.append(resp+"\n")

def build_section_report(chunks):
   for chunk in chunks:
      create_report_comment(chunk)

chat = ChatOpenAI(temperature=0)

# add the path to your MD file here
file_path = ''
doc = load_doc(file_path)

### TODO: Handle front mater
front_matter = doc[0].page_content
## This var is not yet being used, need to parse and send to GPT, append results to front of report

md_chunks = chunk_MD_on_header(file_path)

report_list = []

proc_sys_template="You are a helpful assistant that reviews technical procedures for American English spelling, grammar, phrasing and conciseness."
proc_user_template="Review: \n\n {section}. Output is formatted as Markdown. Output contains a bulleted list of errors found in that section, an empty line, a title `### EDITED VERSION`, another empty line, and the edited version of the section returned as markdown and contained in a fenced code block."

proc_chat_prompt = set_prompt(proc_sys_template, proc_user_template)

for chunk in md_chunks:
   chunk_header = extract_first_header_title(chunk)
   report_list.append("\n\n ## REVIEW: "+chunk_header+"\n")

   if chunkIsProcedure(chunk):
      report_list.append("\n<!-- CLASSIFIED AS PROCEDURE !-->\n\n")
      chunk_splits_on_step_1 = split_on_first_step(chunk)

      pruned_procedure = prune_procedure(chunk_splits_on_step_1[1])

      chunk_splits_on_last_step = split_on_last_step(pruned_procedure)

      if len(chunk_splits_on_last_step) > 2:
         chunks = chunk_splits_on_last_step.insert(0, chunk_splits_on_step_1[0])
         build_section_report(chunks)

      else:
         chunks = [chunk_splits_on_step_1[0], pruned_procedure]
         build_section_report(chunks)

   else:
      chunk_paras = split_paragraphs(chunk)
      report_list.append("\n<!-- CLASSIFIED AS NARRATIVE !-->\n\n")

      build_section_report(chunk_paras)

   report_list.append("\n\n <!-- END_REVIEW: "+chunk_header+" !-->\n")

# add the name and path for the markdown report that the script creates
report_path = ''

write_markdown_file(report_path, report_list)
