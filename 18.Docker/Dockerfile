FROM debian:bullseye-slim

ARG INSTALL_FILE=actions-runner-linux-x64-2.309.0.tar.gz
ARG TOKEN=AKMX4A3GZWLVG6KPRTLZAVDFBBSOA
ENV RUNNER_ALLOW_RUNASROOT="1"

WORKDIR /runner

RUN apt-get update && apt-get install -y curl wget \
    && wget https://packages.microsoft.com/config/debian/11/packages-microsoft-prod.deb -O packages-microsoft-prod.deb \
    && dpkg -i packages-microsoft-prod.deb \
    && rm packages-microsoft-prod.deb \
    && apt-get update \
    && apt-get install -y aspnetcore-runtime-7.0 dotnet-sdk-7.0 \
    && curl -o $INSTALL_FILE -L https://github.com/actions/runner/releases/download/v2.309.0/$INSTALL_FILE \
    && tar xzf ./actions-runner-linux-x64-2.309.0.tar.gz  \
    && rm $INSTALL_FILE
RUN /n | ./config.sh --url https://github.com/EugenMol/test_self_hosted_GHA --token $TOKEN

ENTRYPOINT ["/bin/bash"]

CMD ["./run.sh"]