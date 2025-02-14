**# SIA_Dataset**

This is a dataset about Security Incident Analysis Tasks. This repository contains different type of tasks such as Network Forensics, Disk & Memory Forensics, Malware Analysis and Others.

# Dataset Structure

**Restricted Information:** These fields contain metadata that may not be publicly available but are essential for tracking and referencing the scenario.

1. Source: A URL pointing to the original reference where the scenario was sourced from.

2. Scenario Name: A unique identifier for the security scenario.

3. Last accessed: The last date when the scenario was accessed or updated.

4. Task Category: Defines the primary focus of the challenge, such as "Malware Analysis," "Network Forensics" etc.

5. Complexity: The difficulty level of the scenario, such as "Easy," "Medium," or "Hard."

6. Writeup: A URL leading to a solution guide or writeup for the challenge.

**Public Information:** These fields describe the scenario that security analysts/LLM will use and investigate.

1. Scenario: A brief background of the incident and the objectives for the analyst.

2. Files available: The evidence file(s) provided for analysis. 

3. Tools available: A list of built-in suggested tools that can be used for analysis, including tshark, pdfparser, volatility, python, md5sum, and more.

4. Instructions: Some Guidelines for using tools, often within a Kali Linux terminal.

5. Directory: The file path where the scenario data is stored on the system.

6. Questions: A list of specific key investigative questions analysts must answer by examining the provided files.

7. Answer: The answer for the investigative questions.

8. Adversarial Tactic: The MITRE ATT&CK framework tactic associated with the investigative question.
