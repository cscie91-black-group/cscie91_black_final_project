# Use nginx webserver
FROM    nginx:latest

# Change working directory to location where site files are stored
WORKDIR /usr/share/nginx/html

# Copy both the index file and the images files to the proper nginx directory
COPY    index.html index.html
COPY    images images
