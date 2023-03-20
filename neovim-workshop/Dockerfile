FROM debian:latest

RUN apt-get -y update && apt-get -y upgrade && apt-get install -y unzip \
                       pip \
        		       openssh-server \
                       curl \
                       wget \
                       tmux \
                       xclip \
                       net-tools \
                       sudo \
                       ripgrep \
                       npm \
                       ninja-build \
                       gettext \
                       libtool \
                       libtool-bin \
                       autoconf \
                       automake \
                       cmake \
                       g++ \
                       pkg-config \
                       doxygen \
                       black

# INSTALL NODE JS
RUN curl -sL https://deb.nodesource.com/setup_16.x -o /tmp/nodesource_setup.sh
RUN sudo bash /tmp/nodesource_setup.sh
RUN sudo apt install -y nodejs

# INSTALL NEOVIM
COPY ./neovim /neovim
RUN cd /neovim && make CMAKE_BUILD_TYPE=RelWithDebInfo && sudo make install

# OPEN SSH CONFIG
RUN mkdir /var/run/sshd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN ssh-keygen -A
COPY ./start.sh /usr/bin/start.sh
RUN chmod 755 /usr/bin/start.sh
EXPOSE 22

# INSTALL LOCALES
RUN apt-get install -y locales && \
    sed -i -e 's/# de_DE.UTF-8 UTF-8/de_DE.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales

# FIX PYHTON LINK
RUN ln -s /usr/bin/python3 /usr/bin/python

# DEACTIVATE ROOT
RUN chsh -s /usr/sbin/nologin root

# CREATE USER
RUN groupadd -r ordix && useradd -m -r -g ordix ordix
RUN echo 'ordix:$ordix123456' | chpasswd
RUN sed -Ei 's|(ordix.*)/bin/sh|\1/bin/bash|g' /etc/passwd

WORKDIR /home/ordix
ENV HOME /home/ordix

# INSTALL NEOVIM AND TMUX CONFIG
COPY ./.tmux.conf /home/ordix/.tmux.conf
COPY ./nvim /home/ordix/.config/nvim

# MOVE SOURCE CODE IN
COPY ./code /home/ordix/code
RUN chown -R ordix /home/ordix/

# SETUP UP TERMINAL STYLING
ENV TERM xterm-256color
ENV LC_ALL de_DE.utf-8

# GIT INIT TO MAKE PYTHON CODE A WORKSPACE IN NVIM
RUN git init /home/ordix/code

CMD ["/usr/bin/start.sh"]

# CHANGE USER
# USER ordix 
