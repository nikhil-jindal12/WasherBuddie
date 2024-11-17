# Step 1: Use Python 3.12-slim as the base image
FROM python:3.12-slim

# Install Node.js and npm
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Step 2: Set up Python dependencies (if you have any)
# Copy and install Python dependencies
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# Step 3: Set up React
WORKDIR /app/washerbuddie

# Copy package.json and package-lock.json for React dependencies
COPY washerbuddie/package.json washerbuddie/package-lock.json ./

# Install React dependencies, including react-router-dom
RUN npm install

# Copy React source code
COPY washerbuddie/ .

# Expose the React port (3000)
EXPOSE 3000

# Step 4: Define the command to run React
CMD ["npm", "start"]
