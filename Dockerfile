FROM registry.fedoraproject.org/f29/s2i-base:latest

USER root

ADD . /opt/sms

WORKDIR /opt/sms

ENV PYTHON_VERSION=3.6 \
    PATH=$HOME/.local/bin/:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    PIP_NO_CACHE_DIR=off

ENV NAME=python3 \
    VERSION=0 \
    RELEASE=1 \
    ARCH=x86_64


RUN INSTALL_PKGS="python3 python3-devel python3-setuptools python3-pip" && \
        dnf -y --setopt=tsflags=nodocs install $INSTALL_PKGS && \
        dnf -y clean all --enablerepo='*'&& \
        pip3 install -r /opt/sms/requirements.txt && \
        rm /opt/sms/requirements.txt

RUN chmod 777 /opt/sms /opt/sms/ /opt/sms/*
RUN chmod 755 /opt/sms/app.py
RUN chown 185 /opt/sms

EXPOSE 8080

LABEL io.k8s.description="Frontend for image upload service" \
      io.k8s.display-name="image-uploader-service" \
      io.openshift.expose-services="8080:http" 

USER 185

CMD ./run.sh