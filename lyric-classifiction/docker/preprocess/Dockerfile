FROM takaiyuk/ml-multimodal-ja:latest
COPY ./docker/preprocess/requirements.txt .
ENV APP_HOME /workspace
RUN pip install -r requirements.txt
WORKDIR $APP_HOME
