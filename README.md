## MCP Notes Server + OpenAI Agent Integration

This repo demonstrates how to integrate a Model Context Protocol (MCP) server with an OpenAI agent.
It uses a simple notes_server.py to expose local text files as MCP tools (list_notes, read_note, search_notes) and an OpenAI agent to query them intelligently.

## Features

- MCP Server over stdio → provides note management tools

- OpenAI Agent Integration → invokes MCP tools automatically based on prompts

- Tracing Support → monitor execution with OpenAI Traces dashboard

- Sample Notes → included .txt files (kubernetes.txt, llm.txt, etc.) for testing

<img width="1600" height="757" alt="image" src="https://github.com/user-attachments/assets/8c8d453f-efa8-4037-b260-e98f5c7c04a8" />
