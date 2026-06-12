# 🌱 EcoSmart AI Chatbot

An AI-powered desktop chatbot that provides smart energy-saving tips
using semantic search and natural language understanding.

Instead of relying on simple keyword matching, the chatbot uses the
**Sentence Transformers** model (`all-MiniLM-L6-v2`) to understand the
meaning behind user questions and return the most relevant advice.

## Features

-   🤖 Semantic similarity matching with Sentence Transformers
-   💡 Intelligent energy-saving recommendations
-   🖥️ Desktop GUI built with Tkinter
-   🌍 Supports English and Greek queries
-   ⚡ Fast local inference
-   📊 Displays a confidence score for each response

## Technologies

-   Python
-   Sentence Transformers
-   PyTorch
-   Tkinter

## Installation

``` bash
pip install sentence-transformers torch
```

## Run

``` bash
python chatbot.py
```

## Example

<p align="center">
<img width="515" height="617" alt="PrintScreen" src="https://github.com/user-attachments/assets/c192072a-6bd4-4cd0-884c-f31375f09faa" />
</p>

## Purpose

This project demonstrates how semantic embeddings can be used to build a
lightweight intelligent assistant that helps users reduce electricity
consumption through practical advice.
