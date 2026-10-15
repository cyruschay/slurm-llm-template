#!/bin/bash
#SBATCH --job-name=llm_test
#SBATCH --partition=gpu
#SBATCH --time=00:10:00    #(HH:MM:SS)

#SBATCH --output=slurm_logs/slurm-%j_output.txt    # %j: jobID
#SBATCH --error=slurm_logs/slurm-%j_error.txt

#SBATCH --gpus=2
#SBATCH --cpus-per-gpu=2

###################################################
# SETTING UP

#module load python3/3.9.2
module load ollama
# Set environmental variables (LLM API keys, NCBI keys, etc.)
export SOME_API_KEY="some_value"
# Set conda environment
#source activate ai_env

###################################################
start_time=$SECONDS
echo "============== Slurm Job Info =============="
echo " Job ID:           $SLURM_JOB_ID"
echo " Job Name:         ${SLURM_JOB_NAME:-N/A}"
echo " User:             ${SLURM_JOB_USER:-$USER}"
echo " Account:          ${SLURM_JOB_ACCOUNT:-N/A}"
echo " Partition:        ${SLURM_JOB_PARTITION:-N/A}"
echo " Node List:        ${SLURM_JOB_NODELIST:-N/A}"
echo
echo " Submit Host:      ${SLURM_SUBMIT_HOST:-N/A}"
echo " Submit Directory: ${SLURM_SUBMIT_DIR:-N/A}"
echo " Work Directory:   $(pwd)"
echo
echo " Allocated CPUs:   $SLURM_CPUS_ON_NODE"
echo " Allocated GPUs:   $SLURM_JOB_GPUS"
echo
echo " Current Time:     $(date +%T)"
echo "============================================"

###################################################

OLLAMA_CONTEXT_LENGTH=40960 ollama serve &

python test_llm.py


###################################################
echo "============================================"
end_time=$SECONDS
echo " Finish Time:      $(date +%T)"
echo " Time Taken:       $((end_time - start_time)) seconds"