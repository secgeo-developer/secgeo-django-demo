# Önce varsayılan değeri belirle
ARG NGINX_VERSION=1.25.2-alpine

FROM nginx:${NGINX_VERSION}

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
