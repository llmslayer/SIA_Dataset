# SIA_Dataset

Welcome to the **SIA_Dataset** repository! 🚀 This dataset is designed for **Security Incident Analysis (SIA)** tasks, encompassing various cybersecurity investigation domains such as **Network Forensics, Disk & Memory Forensics, Malware Analysis, and more.**

📌 The dataset consists of **21 unique security scenarios** with **193 investigative questions** in total. [📄 Detailed Dataset Information](Tasks_Dataset/Dataset.md)

We evaluate different LLMs with our dataset using [🤖 SIA Agent](Agent/agent.md).

---

## 🔔 What's New?

🔹 **New Model Evaluation Added:** Claude-3.5! 
🔹 **Upcoming Reasoning Models:** DeepSeek-R1 & OpenAI o3-mini  
 
Stay updated as we continue expanding and refining our dataset and evaluation! ✨

---

## 📊 Performance Evaluation on SIA_Dataset

###  **Latest Results:**
| Model | Fully Solved Scenarios (FS) | Overall Solving Percentage (%) |
|-------|-----------------------------|----------------|
| Claude-3.5 | 3/21 | 72.02% |

###  **Previous Results:**
| Model | Fully Solved Scenarios (FS) | Overall Solving Percentage (%) |
|-------|-----------------------------|----------------|
| GPT-4o | 4/21 | 58.55% |
| Gemini-1.5-pro | 3/21 | 39.37% |
| GPT-4o-mini | 1/21 | 29.53% |
| LLaMA-3.1-405B | 0/21 | 20.72% |
| LLaMA-3.1-70B | 0/21 | 15.54% |
| LLaMA-3.1-8B | 0/21 | 6.21% |

<details>
<summary>📊 Click to view the full detailed table</summary>

The table below compares the performance of various LLMs across different categories and difficulty levels on the SIA_Dataset:

| Model                |NF-E (3S, 25Q)  | NF-M (3S, 38Q)  | NF-H (1S, 10Q)  | DMF-E (3S, 18Q)  | DMF-M (2S, 16Q)  | DMF-H (1S, 15Q)  | MA-E (2S, 11Q)  | MA-M (2S, 22Q)  | MA-H (1S, 13Q)  | MS-E (3S, 25Q)  | 🌟**Overall** |
|---------------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|----------------|
| **Claude-3.5**     | **1/3** (92.50%) | **0/3** (66.72%) | **0/1** (60.00%) | **1/3** (84.12%) | **0/2** (65.00%) | **0/1** (53.33%) | **1/2** (83.33%) | **0/2** (72.30%) | **0/1** (23.07%) | **0/3** (79.44%) | **3/21 (72.02%)** |
| **GPT-4o**         | **0/3** (64.04%) | **0/3** (47.55%) | **0/1** (40.00%) | **1/3** (69.84%) | **0/2** (68.33%) | **0/1** (33.33%) | **1/2** (91.67%) | **0/2** (58.46%) | **0/1** (23.07%) | **2/3** (81.94%) | **4/21 (58.55%)** |
| **GPT-4o-mini**    | **0/3** (29.28%) | **0/3** (21.99%) | **0/1** (20.00%) | **0/3** (33.33%) | **0/2** (20.95%) | **0/1** (0.00%)  | **1/2** (83.33%) | **0/2** (17.69%) | **0/1** (16.67%) | **2/3** (58.33%) | **1/21 (29.53%)** |
| **Gemini-1.5-pro** | **0/3** (62.97%) | **0/3** (29.05%) | **0/1** (40.00%) | **0/3** (38.41%) | **0/2** (31.67%) | **0/1** (6.67%)  | **1/2** (83.33%) | **1/2** (7.69%)  | **0/1** (23.07%) | **2/3** (80.55%) | **3/21 (39.37%)** |
| **LLaMA-3.1-405B** | **0/3** (32.38%) | **0/3** (12.08%) | **0/1** (20.00%) | **0/3** (20.00%) | **0/2** (5.00%)  | **0/1** (0.00%)  | **0/2** (42.86%) | **0/2** (15.38%) | **0/1** (15.38%) | **0/3** (53.33%) | **0/21 (20.72%)** |
| **LLaMA-3.1-70B**  | **0/3** (17.5%)  | **0/3** (13.44%) | **0/1** (0.00%)  | **0/3** (6.07%)  | **0/2** (6.07%)  | **0/1** (0.00%)  | **0/2** (26.67%) | **0/2** (0.00%)  | **0/1** (15.38%) | **0/3** (47.78%) | **0/21 (15.54%)** |
| **LLaMA-3.1-8B**   | **0/3** (8.33%)  | **0/3** (0.00%)  | **0/1** (0.00%)  | **0/3** (0.00%)  | **0/2** (0.00%)  | **0/1** (0.00%)  | **0/2** (25.00%) | **0/2** (12.50%) | **0/1** (7.69%)  | **0/3** (27.50%) | **0/21 (6.21%)** |


---

</details>

🔹 **FS** = Fully Solved Scenario  
🔹 **PS** = Partially Solved Scenarios  
🔹 **S** = Scenarios, **Q** = Questions  

**Legend:**  
- **NF** = Network Forensics  
- **DMF** = Disk & Memory Forensics  
- **MA** = Malware Analysis  
- **MS** = Miscellaneous  
- **E** = Easy, **M** = Medium, **H** = Hard  

---

## 🧠 Model Integrations

### ✅ **List of Models Already Evaluated**  
SIA Agent has been tested and integrated with **7 popular LLMs**:  

| Model                | Provider     | API Used         |
|----------------------|--------------|------------------|
| Claude-3.5              | Anthropic       | [Claude API](https://docs.anthropic.com/en/docs/about-claude/models/all-models) |
| GPT-4o              | OpenAI       | [OpenAI API](https://platform.openai.com/docs/overview)      |
| GPT-4o-mini         | OpenAI       | [OpenAI API](https://platform.openai.com/docs/overview)      |
| Gemini-1.5-pro      | Google       | [Google Gemini API](https://ai.google.dev/) |
| LlaMa-3.1-8B        | Meta    | [Fireworks API](https://fireworks.ai/models)    |
| LlaMa-3.1-70B       | Meta    | [Fireworks API](https://fireworks.ai/models)     |
| LlaMa-3.1-405B      | Meta    | [Fireworks API](https://fireworks.ai/models)     |

---

### 🔮 **Upcoming Model Evaluations**  
We are actively working on integrating the latest advanced reasoning models to evaluate the capabilities of recent LLMs in automated SIA tasks, including:  

- **[DeepSeek-R1](https://api-docs.deepseek.com/guides/reasoning_model)**  
- **[OpenAI o3-mini](https://openai.com/index/openai-o3-mini/)**  

Stay tuned for updates!  

---

## 📂 Repository Structure

```plaintext
/SIA_Dataset
  ├── Tasks_Dataset/      # Contains the JSON files with scenarios
  └── Agent/              # Contains the code and guidelines to run the SIA agent
README.md
```

--- 

## 🛡️ Ethics Statement  
All the selected scenarios in our dataset are chosen from platforms and websites that were publicly available and free to access at the time of selection. These problems are either retired or explicitly offered for free. The artifacts related to the chosen problems are downloaded solely for research purposes, and these are not distributed. The selected problems have publicly available write-ups or solutions, which are referenced in our dataset. All source links to the platforms and problems are clearly cited in our dataset.
