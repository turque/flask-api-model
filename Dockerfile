# ================================== BUILDER ===================================
ARG INSTALL_PYTHON_VERSION=${INSTALL_PYTHON_VERSION:-PYTHON_VERSION_NOT_SET}

FROM python:${INSTALL_PYTHON_VERSION}-slim-buster AS builder

WORKDIR /api

RUN pip install -U pip
COPY setup.py .
COPY requirements requirements


# ================================= PRODUCTION =================================
FROM python:${INSTALL_PYTHON_VERSION}-slim-buster as production

WORKDIR /api

RUN useradd -m api
RUN chown -R api:api /api
USER api
ENV PATH="/home/api/.local/bin:${PATH}"

COPY setup.py .
COPY requirements requirements
RUN pip install -U pip
RUN pip install --no-cache --user -r requirements/prod.txt
RUN pip install -e .

COPY supervisord.conf /etc/supervisor/supervisord.conf
COPY supervisord_programs /etc/supervisor/conf.d

COPY . .

EXPOSE 5000
ENTRYPOINT ["/bin/bash", "shell_scripts/supervisord_entrypoint.sh"]
CMD ["-c", "/etc/supervisor/supervisord.conf"]


# ================================= DEVELOPMENT ================================
FROM builder AS development

RUN pip install --no-cache -r requirements/dev.txt
RUN pip install -e .

EXPOSE 5000
CMD [ "flask", "run", "--host=0.0.0.0" ]