FROM nginx:1.30.3-alpine

# Upgrade all Alpine packages to latest patched versions available at build time —
# the base image tag is pinned for reproducibility, but OS packages inside it can
# still be stale relative to upstream Alpine security fixes.
RUN apk update && apk upgrade --no-cache

#Remove default nginx config
RUN rm /etc/nginx/conf.d/default.conf

#Copy our nginx config files and static files
COPY nginx.conf /etc/nginx/conf.d/linktracker.conf
COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80 
