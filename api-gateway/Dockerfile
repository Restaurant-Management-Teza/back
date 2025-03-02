# Use Node.js as the base image
FROM node:20-alpine

# Set the working directory
WORKDIR /usr/src/app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy all source code
COPY . .

# Expose port 3000 (or your service port)
EXPOSE 3000

# Start app in development mode (direct from src)
CMD ["npm", "run", "start:dev"]