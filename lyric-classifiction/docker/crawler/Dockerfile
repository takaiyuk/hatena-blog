FROM python:3.8.3-slim-buster
COPY ./docker/crawler/requirements.txt .
ENV APP_HOME /workspace
ENV PYTHONPATH=/usr/local:$PYTHONPATH
ENV CHROMEDRIVER_VERSION 85.0.4183.87
ENV CHROMEDRIVER_PREFIX /usr/bin
ENV CHROMEDRIVER_DIR $CHROMEDRIVER_PREFIX/chromedriver
ENV PATH $CHROMEDRIVER_DIR:$PATH
# hadolint ignore=DL3018, DL4006, SC2094
RUN apt-get update -y \
  && apt-get install -y gnupg libfontconfig1 libgconf-2-4 libglib2.0-0 libnss3 tzdata wget xvfb unzip \
  && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
  && apt-get update -y \
  && apt-get install -y google-chrome-stable \
  && pip install -r requirements.txt \
  && wget -q --continue -P $CHROMEDRIVER_PREFIX "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip" \
  && unzip $CHROMEDRIVER_PREFIX/chromedriver*.zip -d $CHROMEDRIVER_PREFIX \
  && rm $CHROMEDRIVER_PREFIX/chromedriver*.zip
WORKDIR $APP_HOME

ENTRYPOINT ["python"]
