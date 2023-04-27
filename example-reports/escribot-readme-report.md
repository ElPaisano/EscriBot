

## REVIEW: EscriBot


<!-- CLASSIFIED AS NARRATIVE !-->


### Original:
```
This repository is under konstraction 

EscriBot is a Python skript that uses Langchain, ChatGPT and sum custom hacky Python helpers to:

- Review a Markdown document for general writing and readability things (grammar, spelling, phrasing, etc.)
- Output suggested fixes and Markdown edited according to those suggested fixes as a formatted report. 

EscriBot is currently in beta, so it's not ready for production, nor is it intended to be (yet)
```

### Errors:
- "konstraction" should be spelled as "construction"
- "skript" should be spelled as "script"
- "sum" should be spelled as "some"

### Edited:

### Original:
This repository is under konstraction 

EscriBot is a Python skript that uses Langchain, ChatGPT, and some custom hacky Python helpers to:

- Review a Markdown document for general writing and readability things (grammar, spelling, phrasing, etc.)
- Output suggested fixes and Markdown edited according to those suggested fixes as a formatted report. 

EscriBot is currently in beta, so it's not ready for production, nor is it intended to be (yet)

### Edited:
This repository is under construction.

EscriBot is a Python script that uses Langchain, ChatGPT, and some custom hacky Python helpers to:

- Review a Markdown document for general writing and readability (grammar, spelling, phrasing, etc.).
- Output suggested fixes and edited Markdown as a formatted report according to those suggestions.

EscriBot is currently in beta and not yet ready for production.



 <!-- END_REVIEW: EscriBot !-->



## REVIEW: Examples:


<!-- CLASSIFIED AS NARRATIVE !-->


### Original:

N/A

### Errors:

N/A

### Edited:

N/A



 <!-- END_REVIEW: Examples: !-->



## REVIEW: Intitial test case


<!-- CLASSIFIED AS NARRATIVE !-->


No errors found.



 <!-- END_REVIEW: Intitial test case !-->



## REVIEW: Prerequisites


<!-- CLASSIFIED AS NARRATIVE !-->


The text appears to be well-written and free of errors. No edits are necessary.



 <!-- END_REVIEW: Prerequisites !-->



## REVIEW: How to use


<!-- CLASSIFIED AS PROCEDURE !-->


### Original:
## How to use.

### Errors:
N/A

### Edited:
## Instructions for Use.

### Original:
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
7. Give us feedback so that we can develop this tool to make it useful for you :).

### Errors:
- "local" should be "locally"
- "i.e." should be "e.g."
- "completeing" should be "completing"

### Edited:
1. Copy `escribot.py` to your local machine (you don't need the README).
2. Edit the following empty variables in `escribot.py`:
   - `file_path`: set this to the full path of the file that you would like reviewed (e.g. `\Users\me\mydocs\doc.md`).
   - `report_path`: set this to the full path of the report to be generated (e.g. `\Users\me\gpt-reports\report-1.md`).
3. Open a terminal.
4. Run the script:
   ```shell
   python3 base-demo.py
   ```
5. Grab a snack and fire up your Nintendo Gameboy, because it's going to be a few minutes before the script completes.
   > WARNING: The script will hang while it is completing. Do not exit your terminal.
6. Once the script completes, navigate to `report_path` and view the report.
7. Give us feedback so that we can develop this tool to make it more useful for you.



 <!-- END_REVIEW: How to use !-->



## REVIEW: Todo items


<!-- CLASSIFIED AS NARRATIVE !-->


### Original:

 ## Todo items

- [ ] Clean up code so that it’s generic, won’t break on edge cases, is actually well-written code :D
- [ ] Fix report formatting
- [ ] Create a procedure describing how to use this script
- [ ] Currently, this script is slow, (I think) partially due to not using any parallelization - need to figure that out 
- [ ] Figure out how to define a full writing style guide to GPT
- [ ] Figure out how to scale this 
- [ ] Figure out how this can be used as a foundation for other tools -  a GH Action / GH App, a command line tool, all of the above, etc. - and develop accordingly
- [ ] Understand what sort of help technical writers need when it comes to writing, and develop future versions of this with all that in mind

### Errors:

No errors found.

### Edited:

## To-do items

- [ ] Clean up the code to make it generic, prevent it from breaking on edge cases, and ensure it is well-written.
- [ ] Fix the report formatting.
- [ ] Create a procedure that describes how to use this script.
- [ ] Investigate why the script is slow, possibly due to the lack of parallelization, and find a solution.
- [ ] Define a complete writing style guide for GPT.
- [ ] Determine how to scale this script.
- [ ] Explore how this script can serve as a foundation for other tools, such as a GH Action/GH App, a command-line tool, or a combination of these, and develop accordingly.
- [ ] Understand the type of assistance technical writers require when it comes to writing and develop future versions of this script with that in mind.



 <!-- END_REVIEW: Todo items !-->

