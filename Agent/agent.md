# SIA Agent 🚨🛡️

## Introduction

**SIA Agent** is an advanced, LLM-powered system designed to tackle **Security Incident Analysis (SIA)** tasks with precision and adaptability. We evaluate the current capabilities of various large language models (LLMs) while utilizing the **[LangChain](https://www.langchain.com/)** framework for robust implementation.

At the core of SIA Agent is the **[ReAct (Reason + Act)](https://arxiv.org/pdf/2210.03629)** framework, empowering the agent to dynamically plan, execute, and refine its analysis through iterative cycles of:

- **Thought :** Assess the current state and plan the next investigation step.
- **Action :** Execute specific actions based on the assessment.
- **Observation :** Analyze the results and refine future steps.

## 🔍 Key Features

### ✅ Dynamic Interactions

Standalone LLMs can't interact with the external environment and are limited to static, memorized knowledge. To overcome this, **SIA Agent integrates different functionalities**, enabling real-time interaction with the host system. The agent can interact with the **Kali Linux Terminal** to execute different command-line tools to analyze artifacts (e.g. PCAP, Memory Dumps and more.)

### ✅ Tool Output Processing

Security tool outputs can be massive and cause LLMs to hallucinate, lose context, take wrong plans, or fail due to token limitations. SIA Agent solves this with intelligent output handling:

- Segments tool outputs into manageable chunks (32K, 64K, or custom token sizes).
- For outputs larger than **640K tokens**, SIA Agent prompts the LLM to retry the analysis more efficiently. This is configurable according to your preference.
- **Built-in summarization module** (LLM-based) optimizes lengthy outputs to keep context clear and concise. You can choose the summarizer LLM that best suits your workflow.

### ✅ Multi-state Workflow Automation

SIA Agent is designed to handle **multi-question incident scenarios** without getting stuck or wasting resources. It processes questions sequentially within a scenario, skipping over questions it cannot answer after reasonable attempts ensuring efficient analysis without redundant effort.

---

## 🚀 Why Use SIA Agent?

- Fully automated, **intelligent security incident analysis**.
- Leverages **state-of-the-art LLM reasoning and planning**.
- Adapts dynamically to complex, multi-stage investigations.
- Compatible with industry-standard tools in a **Kali Linux** environment.
- Designed to scale, with optimized token management and summarization.

---

>  **Note:** Code will be available soon.

### ⚙️ Model Configuration

To ensure **deterministic and reliable results** from generative LLMs, we use the following default configurations:

- **Temperature:** `0`
- **Seed Value:** `0`
- **Max Iterations Per Scenario:** `number_of_questions × 10`
- **Max Turns per Question:** `15`

---

## 🎥 How to Add a New Model to Our SIA Agent

We have recently added DeepSeek-R1 to our SIA Agent. In the following, we will demonstrate the steps that were involved in the process.

Check out our upcoming video tutorial:  
[📺 Watch the Tutorial (Coming Soon)](#)

---

## 📝 How to Add a New Task

To add a new task to SIA Agent:

1. Create a JSON file within the `../Tasks_Dataset/` directory.
2. Define the scenario, the questions, input artifacts, directory etc.
3. Give specific tool instruction also if needed.

Detailed documentation and examples are coming soon!
[📺 Watch the Tutorial (Coming Soon)](#)

---

## 📌 Upcoming Features

- Support for Additional Human Feedback.
- Evaluate Guided Performance when LLM gives up.

---
