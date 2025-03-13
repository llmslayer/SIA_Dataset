# Dataset

**SIA_Dataset** is the first dataset designed specifically for **Blue Team investigations**, focusing on **multistep, multi-objective security tasks that require dynamic interaction with the environment**. It covers key cybersecurity domains such as **Network Forensics, Disk & Memory Forensics, Malware Analysis, and more.**  

📌 The dataset consists of **21 security incident scenarios**, each represented by a JSON file. In total, it includes **193 investigative questions** covering the most common and critical security investigation tasks.

---

## 📂 Dataset Structure

### 🔒 **Restricted Information**
*(These metadata fields may not be publicly available but are crucial for tracking and referencing each scenario.)*

1. **Source** → URL pointing to the original reference where the scenario was sourced from.
2. **Scenario Name** → A unique identifier for each security scenario.
3. **Last Accessed** → The most recent date when the scenario was accessed or updated.
4. **Task Category** → Defines the primary focus of the challenge (e.g., *Malware Analysis, Network Forensics, etc.*).
5. **Complexity** → The difficulty level of the scenario (*Easy, Medium, or Hard*).
6. **Writeup** → URL to a solution guide or writeup for the challenge.

### 🌍 **Public Information**
*(These fields describe the scenario that security analysts or AI models will investigate.)*

1. **Scenario** → A brief background of the incident and the investigation objectives.
2. **Files Available** → The evidence files provided for analysis.
3. **Tools Available** → A list of recommended built-in tools for analysis (*e.g., tshark, pdfparser, volatility, python, md5sum, etc.*).
4. **Instructions** → Guidelines for using analysis tools, within a *Kali Linux* terminal.
5. **Directory** → The file path where the scenario data is stored on the system.
6. **Questions** → Key investigative questions analysts must answer based on the provided files.
7. **Answer** → The expected answers to the investigative questions.
8. **Adversarial Tactic** → The **MITRE ATT&CK** framework tactic associated with the investigative question.

---
