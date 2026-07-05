FROM nginx:1.30.3-alpine

#Remove default nginx config
RUN rm /etc/nginx/conf.d/default.conf

#Copy our nginx config files and static files
COPY nginx.conf /etc/nginx/conf.d/linktracker.conf
COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80 
