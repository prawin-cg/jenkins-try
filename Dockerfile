FROM gcr.io/famous-strategy-344516/base-img:1.1

COPY . .

CMD python load_job.py
