import json
import logging
from dotenv import load_dotenv
from pathlib import Path   
from marketing_agency.configs.agents import *
from .eval_utils import run_function_evals
from .eval_config import get_eval_config

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_test_cases(path: str) -> list:
    try:
        with open(path, "r") as file:
            return json.load(file)
    except Exception as e:
        logger.error(f"Error loading test cases from {path}: {e}")
        raise

def main():
    config = get_eval_config()
    test_cases = {
        "manager": ("marketing_agency/evals/eval_cases/manager_cases.json", manager),
        "creative": ("marketing_agency/evals/eval_cases/creative_cases.json", creative_director),
        "copywriter": ("marketing_agency/evals/eval_cases/copywriter_cases.json", copywriter),
        "designer": ("marketing_agency/evals/eval_cases/designer_cases.json", graphic_designer),
        "analyst": ("marketing_agency/evals/eval_cases/analyst_cases.json", data_analyst),
        "client": ("marketing_agency/evals/eval_cases/client_cases.json", client_liaison)
    }

    for role, (test_case_path, agent) in test_cases.items():
        logger.info(f"Running {role} evaluations...")
        try:
            test_cases = load_test_cases(test_case_path)
            result = run_function_evals(
                agent,
                test_cases,
                config["iterations_per_case"],
                eval_path=config["result_paths"][role]
            )
            logger.info(f"Completed {role} evaluations with "
                       f"accuracy: {result['overall_accuracy_percent']}")
        except Exception as e:
            logger.error(f"Failed to run {role} evaluations: {e}")

if __name__ == "__main__":
    main()
