# EscriBot

> This repository is under construction

EscriBot is a Python script that uses Langchain, ChatGPT and some custom hacky Python helpers to:

- Review a Markdown document for general writing and readability things (grammar, spelling, phrasing, etc.)
- Output suggested fixes and Markdown edited according to those suggested fixes as a formatted report. 

## Todo items
- [ ] Clean up code so that it’s generic, won’t break on edge cases, is actually well-written code :D
- [ ] Fix report formatting
- [ ] Create a procedure describing how to use this script
- [ ] Currently, this script is slow, (I think) partially due to not using any parallelization - need to figure that out 
- [ ] Figure out how to define a full writing style guide to GPT
- [ ] Figure out how to scale this 
- [ ] Figure out how this can be used as a foundation for other tools -  a GH Action / GH App, a command line tool, all of the above, etc. - and develop accordingly
- [ ] Understand what sort of help technical writers need when it comes to writing, and develop future versions of this with all that in mind
