FROM continuumio/miniconda3
WORKDIR /ai_model
COPY . /ai_model

RUN conda install -c conda-forge python=3.8
RUN conda install pytorch
RUN conda install torchvision
RUN conda install x264
RUN conda install x264 ffmpeg
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt


