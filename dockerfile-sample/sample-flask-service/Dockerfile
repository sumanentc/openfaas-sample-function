FROM openfaas/of-watchdog:0.8.0 as watchdog
FROM sumand/python-sample-flask:latest

RUN mkdir -p /home/app

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog

# Add non root user
RUN addgroup --system app && adduser app --system --ingroup app
RUN chown app /home/app

USER app
ENV PATH=$PATH:/home/app/.local/bin

USER root
WORKDIR /home/app/
RUN chown -R app:app *
USER app

ENV fprocess="python app.py"
RUN ls -lrt

ENV upstream_url="http://127.0.0.1:5000"
ENV mode="http"
ENV cgi_headers="true"

CMD ["fwatchdog"]
