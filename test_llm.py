from datetime import datetime
from langchain_ollama import ChatOllama
corpus = """
Abstract

Purpose: A subset of pancreatic ductal adenocarcinomas (PDACs) is highly resistant to systemic chemotherapy, but no markers are available in clinical settings to identify this subset. We hypothesized that a glycan biomarker for PDACs called sialylated tumor-related antigen (sTRA) could be used for this purpose.

Experimental design: We tested for differences between PDACs classified by glycan expression in multiple systems: sets of cell lines, organoids, and isogenic cell lines; primary tumors; and blood plasma from human subjects.

Results: The sTRA-expressing models tended to have stem-like gene expression and the capacity for mesenchymal differentiation, in contrast to the nonexpressing models. The sTRA cell lines also had significantly increased resistance to seven different chemotherapeutics commonly used against pancreatic cancer. Patients with primary tumors that were positive for a gene expression classifier for sTRA received no statistically significant benefit from adjuvant chemotherapy, in contrast to those negative for the signature. In another cohort, based on direct measurements of sTRA in tissue microarrays, the patients who were high in sTRA again had no statistically significant benefit from adjuvant chemotherapy. Furthermore, a blood plasma test for the sTRA glycan identified the PDACs that showed rapid relapse following neoadjuvant chemotherapy.

Conclusions: This research demonstrates that a glycan biomarker could have value to detect chemotherapy-resistant PDAC in clinical settings. This capability could aid in the development of stratified treatment plans and facilitate biomarker-guided trials targeting resistant PDAC.

©2020 American Association for Cancer Research. 
"""

start_time = datetime.now()

model = ChatOllama(model = "deepseek-r1:8b", temperature = 0)
messages = [
    ("system",
     "You are a glycan biomarker curator. Given a scientific article, extract and summarize the key findings related to glycan biomarkers for cancer diagnosis."
    ),
    ("user",
	corpus
    )
]
response = model.invoke(messages)
print(response.content)

end_time = datetime.now()
print("Time taken:", end_time - start_time)
