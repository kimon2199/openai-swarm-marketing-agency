from typing import Dict, Any

EVAL_CONFIG = {
    "iterations_per_case": 5,
    "max_turns": 1,
    "timeout_seconds": 30,
    "save_results": True,
    "result_paths": {
        "manager": "eval_results/manager_evals.json",
        "creative": "eval_results/creative_evals.json",
        "copywriter": "eval_results/copywriter_evals.json",
        "designer": "eval_results/designer_evals.json",
        "analyst": "eval_results/analyst_evals.json",
        "client": "eval_results/client_evals.json"
    }
}

def get_eval_config() -> Dict[str, Any]:
    return EVAL_CONFIG 
