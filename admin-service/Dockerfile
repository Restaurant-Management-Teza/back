# Use Node.js as the base image
FROM node:20-alpine

# Set the working directory
WORKDIR /usr/src/app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy all source code
COPY . .

EXPOSE 3003

# Start app in development mode (direct from src)
CMD ["npm", "run", "start:dev"]