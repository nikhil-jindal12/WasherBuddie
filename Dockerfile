# Step 1: Use Python 3.12 slim image for the backend (Flask)
FROM python:3.12-slim 

# Set working directory for backend (Flask)
WORKDIR /app

# Copy the requirements file and install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Step 2: Use Node.js 16-alpine for the frontend (React)
FROM node:16-alpine

# Set working directory for frontend (React)
WORKDIR /app/washerbuddie

# Copy package.json and install React dependencies (will be created later)
COPY washerbuddie/package.json .
RUN npm install

# Step 3: Expose the ports Flask (5000) and React (3000)
EXPOSE 5000 3000

# Copy the rest of the project files into the container
COPY . /app/

# Step 4: Set up Flask environment variables (optional)
ENV FLASK_APP=/app/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Step 5: Run both Flask and React servers
CMD flask run --host=0.0.0.0 --port=5000 & cd /app/washerbuddie && npm start
