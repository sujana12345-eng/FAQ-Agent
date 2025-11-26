FROM python:3.9-slim
WORKDIR /app
# Install only action-server deps to keep image small
COPY ./actions/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY ./actions /app/actions
EXPOSE 5055
CMD ["rasa-sdk", "--actions", "actions"]
