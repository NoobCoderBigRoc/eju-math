# 统计服务镜像：单文件 Python，零第三方依赖
FROM python:3.13-slim

WORKDIR /app
ENV PYTHONUNBUFFERED=1 \
    TZ=Asia/Shanghai \
    PORT=8787 \
    ANALYTICS_DB=/data/analytics.db

COPY server.py ./
COPY static ./static

RUN mkdir -p /data && useradd -m -u 10001 stats && chown -R stats /data /app
USER stats

VOLUME ["/data"]
EXPOSE 8787
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD python -c "import urllib.request,sys; sys.exit(0 if urllib.request.urlopen('http://127.0.0.1:8787/api/health',timeout=2).status==200 else 1)"

CMD ["python", "server.py"]
