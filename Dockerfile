FROM caddy:2-alpine
COPY Caddyfile /etc/caddy/Caddyfile
COPY output/ /srv/
EXPOSE 80
