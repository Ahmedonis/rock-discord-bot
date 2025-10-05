# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy all files from your repo into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable (optional, can also set in Fly.io secrets)
# ENV DISCORD_TOKEN=your_token_here

# Command to run your bot
CMD ["python", "bot.py"]
