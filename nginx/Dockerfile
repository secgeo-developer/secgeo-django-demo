# Önce varsayılan değeri belirle
ARG NGINX_VERSION=1.29.0-alpine-slim

FROM docker.io/nginx:${NGINX_VERSION}

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
