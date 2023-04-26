# EscriBot

> This repository is under construction 

EscriBot is a Python script that uses Langchain, ChatGPT and some custom hacky Python helpers to:

- Review a Markdown document for general writing and readability things (grammar, spelling, phrasing, etc.)
- Output suggested fixes and Markdown edited according to those suggested fixes as a formatted report. 

> EscriBot is currently in beta, so it's not ready for production, nor is it intended to be (yet)

## Prerequisites

- A paid OpenAI account
- An OpenAI API key
- A terminal
- Python 3
- All packages used in `escribot.py` installed (use pip or pip3)
- Patience (this script is currently not optimized and hacky, so it takes a few minutes to complete. Also, GPT has issues sometimes)

## How to use

1. Copy `escribot.py` to your local (you don't need the README)
2. Edit the following empty variables in `escribot.py`:
   - `file_path`: set this to the full path of the file that you would like reviewed i.e. `\Users\me\mydocs\doc.md`
   - `report_path`: set this to the full path of the report to be generated i.e. `\Users\me\gpt-reports\report-1.md`
3. Open a terminal
4. Run the script:

   ```shell
   python3 base-demo.py
   ```
5. Grab a snack and fire up your Nintendo Gameboy, because it's going to be a few minutes before the script completes.

   > WARNING: The script will hang while it is completeing. Do not exit your terminal

6. Once the script completes, navigate to `report_path` and view the report.

7. Give us feedback so that we can develop this tool to make it useful for you :)

## Todo items
- [ ] Clean up code so that it’s generic, won’t break on edge cases, is actually well-written code :D
- [ ] Fix report formatting
- [ ] Create a procedure describing how to use this script
- [ ] Currently, this script is slow, (I think) partially due to not using any parallelization - need to figure that out 
- [ ] Figure out how to define a full writing style guide to GPT
- [ ] Figure out how to scale this 
- [ ] Figure out how this can be used as a foundation for other tools -  a GH Action / GH App, a command line tool, all of the above, etc. - and develop accordingly
- [ ] Understand what sort of help technical writers need when it comes to writing, and develop future versions of this with all that in mind
