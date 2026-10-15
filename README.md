# Slurm LLM invocation template

Run a Python LLM request with Ollama on a GPU node managed by Slurm. `test_llm.py` uses LangChain to invoke `deepseek-r1:8b` on a sample abstract.

> [!NOTE]
> Ollama should already have been installed on the server and is available through <code>module load ollama</code>.

## Quick Start

### 1. Download the model on a login node

Use the login node only to download the model; run inference in a Slurm GPU job.

In your first SSH terminal, start the Ollama server in the foreground:

```bash
module load ollama
ollama serve
```

Leave this terminal running. Open a second SSH terminal connected to the **same
login node**, using the same user account, then download and verify the model:

```bash
module load ollama
ollama pull deepseek-r1:8b
ollama list
```

Confirm that `deepseek-r1:8b` appears in the list. Return to the first terminal
and press **Ctrl+C** to stop `ollama serve` before submitting inference jobs.
Pulling downloads the model; it does not require running an inference request.

### 2. Install Python requirements

From the repository directory, load your cluster's Python module if needed
(`module avail` shows available modules), then install the requirements using
that Python:

```bash
python -m pip install -r requirements.txt
```

### 3. Submit the GPU job

`slurm.sh` requests two GPUs in the `gpu` partition for ten minutes, loads the
Ollama module, starts a server with a context length of 40960, and runs
`python test_llm.py`. Check these resource settings against your cluster and
model requirements.

Submit from the repository directory on the login node. Slurm schedules the
script on an allocated GPU node. The `slurm_logs/` folder will be created regardless.

```bash
sbatch slurm.sh
squeue -u "$USER"
```

Use the job ID printed by `sbatch` to inspect
`slurm_logs/slurm-<job-id>_output.txt` and
`slurm_logs/slurm-<job-id>_error.txt`. Cancel a job with `scancel <job-id>`.
If you change the model name in `test_llm.py`, download that exact model tag
using the two-terminal procedure before submitting again.
