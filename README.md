# sp211_2200674014

A simple Python package for shortest path analysis using Dijkstra's algorithm.

---

## Project Description

This package implements the classic Dijkstra algorithm to compute the shortest paths in a directed, weighted graph. It is designed for educational and research purposes, and can be used as a template for learning about Python packaging, testing, and documentation.

---

## Usage Example

```python
from sp211 import dijkstra

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 1, 'D': 5},
    'C': {'D': 8, 'E': 10},
    'D': {'E': 2, 'F': 6},
    'E': {'F': 2},
    'F': {},
}

distances, previous = dijkstra(graph, 'A')
print(distances)
AI Involvement / Yapay Zeka Katkısı
This project was developed with significant support from OpenAI's ChatGPT.

I used ChatGPT as an interactive assistant throughout all stages: planning the package structure, writing functions, debugging, creating test cases, and preparing documentation.

I requested step-by-step code explanations, example scripts, and advice for best practices, and I received ready-to-use code blocks and terminal commands.

Whenever I was unsure about a Python packaging standard or a command, I described my issue and got direct, actionable answers from ChatGPT.

All folder organization, code templates, and even this README structure were created with ChatGPT’s guidance.

I also asked ChatGPT to review, optimize, and comment on my code when needed.

Without this level of AI assistance, I would have spent much more time and possibly missed out on many best practices in modern Python package development.

## 🚀 Logging Feature
In this project, the Python logging module has been integrated to monitor the working steps of the Dijkstra algorithm.

The queue status and the progress of the algorithm can be monitored with log messages.

## 🤖 Artificial Intelligence Support
The package structure, logging integration, test steps and documentation of this project have been planned and implemented with ChatGPT support.
