FROM takaiyuk/ml-multimodal-ja:latest
COPY ./docker/train/requirements.txt .
ENV APP_HOME /workspace
RUN pip install -r requirements.txt
WORKDIR $APP_HOME
