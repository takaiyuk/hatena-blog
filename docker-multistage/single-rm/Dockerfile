FROM python:3.7.7-slim
ENV APP_HOME /workspace
WORKDIR $APP_HOME
ADD requirements.txt $APP_HOME
RUN mkdir /root/.kaggle \
  && apt-get -y update \
  && apt-get -y install clang cmake git nodejs npm vim \
  && git clone --recursive https://github.com/microsoft/LightGBM && cd LightGBM && mkdir build && cd build && cmake .. && make -j4 && cd ../python-package && python setup.py install && cd ../.. && rm -r LightGBM \
  && git clone --recursive https://github.com/dmlc/xgboost && cd xgboost && mkdir build && cd build && cmake .. && make -j$(nproc) && cd ../python-package && python setup.py install && cd ../.. && rm -r xgboost \
  && pip install -r requirements.txt \
  && export NODE_OPTIONS=--max-old-space-size=4096 \
  && jupyter labextension install @jupyterlab/toc \
  && jupyter labextension install jupyterlab-plotly@4.7.1 \
  && jupyter nbextension enable --py widgetsnbextension \
  && apt-get -y remove clang cmake nodejs npm \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
CMD jupyter lab \
  --no-browser \
  --port=8888 \
  --ip=0.0.0.0 \
  --allow-root 
