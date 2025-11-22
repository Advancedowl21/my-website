# Simple nginx Dockerfile to serve a static site
FROM nginx:stable-alpine

# Remove default conf if present and add our custom conf
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy the site content
COPY . /usr/share/nginx/html

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s CMD wget -qO- http://localhost/ || exit 1
