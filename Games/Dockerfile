FROM python:3.13-slim

# Set the working directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY . . 
EXPOSE 5000

# Set an app user to run the application
RUN useradd app
USER app

# Run the application
CMD ["python", "alien_invasions/alien_invasion.py"]