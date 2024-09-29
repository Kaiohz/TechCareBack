# Use the official Node.js 14 image as the base image
FROM node:22

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy the rest of the project files to the working directory
COPY . .

# Expose the port your Node.js app is listening on (replace 3000 with your actual port)
EXPOSE 3000

# Start the Node.js app
CMD [ "npm", "run", "start" ]