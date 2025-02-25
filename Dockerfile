# FROM python:3.8

# WORKDIR /src/fastapi_api

# COPY requirements.txt .

# RUN pip install -r requirements.txt

# # RUN curl -fsSL https://ollama.com/install.sh | sh

# # RUN ollama run llama3:instruct

# COPY . .

# EXPOSE 8000

# # CMD ["python", "src/fastapi_api/client.py"]
# # CMD ["uvicorn", "src.fastapi_api.app:app","--port 0.0.0.0", "--reload"  ]
# CMD ["uvicorn", "src.fastapi_api.app:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["python","-m", "src.fastapi_api.app"]
# CMD ["uvicorn", "app:app", "--reload"]






# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /src/fastapi_api

# Install curl and other necessary packages
RUN apt-get update && apt-get install -y curl

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Install Ollama
# RUN curl -fsSL https://ollama.com/install.sh | sh

# # Pull the llama3 model (use the correct path if necessary)
# RUN /root/.ollama/bin/ollama pull llama3:instruct || echo "Failed to pull llama3 model"
# RUN /root/.ollama/bin/ollama run llama3:instruct || echo "Failed to pull llama3 model"

# Copy the rest of the application's code
COPY . .

# Expose the port where the application runs
EXPOSE 8000

# Command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "src.fastapi_api.app:app", "--host", "0.0.0.0", "--port", "8000"]

# CMD ["/root/.ollama/bin/ollama", "run", "llama3:instruct", "&&", "uvicorn", "src.fastapi_api.app:app", "--host", "0.0.0.0", "--port", "8000"]