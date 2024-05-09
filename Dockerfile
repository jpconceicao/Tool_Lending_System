FROM python:3.12

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8001", "tool_lending_system:my_app"]