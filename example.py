
from openai import AzureOpenAI
from dotenv import load_dotenv
import os

import prompt_scorer

load_dotenv()

# Load environment variables
AZURE_OPENAI_ENDPOINT=os.environ["AZURE_OPENAI_ENDPOINT"]
AZURE_OPENAI_API_KEY=os.environ["AZURE_OPENAI_API_KEY"]
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=os.environ["AZURE_OPENAI_MODEL_DEPLOYMENT_NAME"]
AZURE_OPENAI_API_VERSION="2024-02-01"

# LLM client
llm_client = AzureOpenAI(
  azure_endpoint = AZURE_OPENAI_ENDPOINT, 
  api_key = AZURE_OPENAI_API_KEY,  
  api_version = AZURE_OPENAI_API_VERSION
)

# Sample input prompt
input_prompt = f"""The description for this product should be fairly short, a few sentences only, and not too much more."""

# Score the prompt calling the scoring function
prompt_scorer.score_prompt(input_prompt, llm_client, AZURE_OPENAI_MODEL_DEPLOYMENT_NAME)