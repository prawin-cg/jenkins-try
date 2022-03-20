FROM gcr.io/famous-strategy-344516/base-img:1.2

COPY . .

CMD python load_job.py
