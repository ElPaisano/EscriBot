# EscriBot

> WARNING
>
> This repository is under very much in beta mode/ under construction and is liable to change frequently.

EscriBot is a Python script that uses Langchain, ChatGPT, and some custom hacky Python helpers to:

- Review a Markdown document for general writing and readability (grammar, spelling, phrasing, etc.).
- Output suggested fixes and edited Markdown as a formatted report according to those suggestions.

> EscriBot is currently in beta and not yet ready for production.

## Examples:

More examples to be added shortly.

### Intitial test case
- _Example input_: A copy of the Filecoin docs [ERC-20 quickstart page](https://gist.github.com/ElPaisano/5985b02c82f6eba48a5892b8dca276e4), with a few extra writing mistakes intentionally introduced for test purposes.
- _Example output_: [A report](https://gist.github.com/ElPaisano/82712cafaca2b1fe26e6dcb50ea8af56), formatted as a Markdown file (not handling front matter in this script yet)

### This README

EscriBot was run against this repositories README as of [577e48136f4ab91966bed6bb33242185fc7e3a4e](https://github.com/ElPaisano/EscriBot/commit/577e48136f4ab91966bed6bb33242185fc7e3a4e). The report produced for this repositories README can be found in `\example-reports`. Note that the report has formatting issues and missed a section - this tool is still very much under construction. However, if you review the README as of latest commit, you'll see that the suggestions were useful, so they were incorporated.

## Prerequisites

- A paid OpenAI account
- An OpenAI API key
- A terminal
- Python 3
- All packages used in `escribot.py` installed. You can use pip or pip3 for this:
  - `re`
  - `langchain`
- Patience. This script is currently not optimized, so it takes at least a minute to complete, and can take 5-10 minutes for longer files. Also, GPT just breaks sometimes.

## Instructions for Use

1. Copy `escribot.py` to your local machine. You don't need the README.
1. Edit the following empty variables in `escribot.py`:
   - `file_path`: set this to the full path of the file that you would like reviewed (e.g. `\Users\me\mydocs\doc.md`).
   - `report_path`: set this to the full path of the report to be generated (e.g. `\Users\me\gpt-reports\report-1.md`).
1. Open a terminal.
1. In the terminal, set your OpenAI API key `<key>`:

   ```shell
   export OPENAI_API_KEY="<key>"
   ```
1. Run the script:

   ```shell
   python3 escribot.py
   ```
   
1. Grab a snack and fire up your Nintendo Gameboy, because it's going to be a few minutes before the script completes.

   > WARNING: The script will hang while it is completing. Do not exit your terminal.
   
1. Once the script completes, navigate to `report_path` and view the report.
1. Give us feedback so that we can develop this tool to make it more useful for you.

## To-do items

- [ ] Clean up code so that it’s generic, won’t break on edge cases, is actually well-written code :D
- [ ] Fix report formatting
- [ ] Currently, this script is slow, (I think) partially due to not using any parallelization - need to figure that out 
- [ ] Figure out how to teach a full writing style guide to GPT, so that it edits according to that
- [ ] Figure out how to scale this 
- [ ] Figure out how this can be used as a foundation for other tools -  a GH Action / GH App, a command line tool, all of the above, etc. - and develop accordingly
- [ ] Understand what sort of help technical writers need when it comes to writing, and develop future versions of this with all that in mind
