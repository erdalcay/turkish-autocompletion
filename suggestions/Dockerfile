FROM python:3

ENV VIRTUAL_ENV=/virtualenv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .
CMD ["flask", "run"]