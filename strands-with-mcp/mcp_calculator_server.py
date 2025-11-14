from mcp.server import FastMCP
import boto3
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

mcp = FastMCP("Calculator Server")

# Initialize AWS Bedrock client
# Credentials will be loaded from environment variables or AWS credentials file
bedrock_runtime = boto3.client(
    service_name='bedrock-runtime',
    region_name=os.getenv('AWS_REGION', 'us-east-2')  # TODO: Match Region to your Bedrock's region
)

@mcp.tool(description="Add two numbers together")
def add(x: int, y: int) -> int:
    """Add two numbers and return the result."""
    return x + y

@mcp.tool(description="Subtract two numbers")
def subtract(x: int, y: int) -> int:
    """Subtract two numbers and return the result."""
    return x - y

@mcp.tool(description="Multiply two numbers")
def multiply(x: int, y: int) -> int:
    """Multiply two numbers and return the result."""
    return x * y

@mcp.tool(description="Divide two numbers using AWS Bedrock")
def divide(x: int, y: int) -> float:
    """Divide two numbers using AWS Bedrock and return the result."""
    
    # Prepare the prompt for the model
    prompt = f"Calculate the result of {x} divided by {y}. Return only the numeric answer, nothing else."
    
    # Prepare the request body for Claude 3 Sonnet
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    })
    
    # Invoke the model
    response = bedrock_runtime.invoke_model(
        modelId='',  # TODO: Add inference profile ARN from AWS Bedrock > Infer > Cross Region Inference
        body=body
    )
    
    # Parse the response
    response_body = json.loads(response['body'].read())
    result_text = response_body['content'][0]['text'].strip()
    
    # Convert the result to float
    try:
        result = float(result_text)
        return result
    except ValueError:
        # If the model returns something we can't parse, fall back to regular division
        return x / y

mcp.run(transport="streamable-http")