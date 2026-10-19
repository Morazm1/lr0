FROM alpine:3.20

RUN addgroup -g 1000 app && adduser -D -u 1000 -G app app

WORKDIR /app
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh && chown -R app:app /app

USER app

CMD ["/app/entrypoint.sh"]
