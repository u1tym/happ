sudo apt install python3-virtualenv


python 3.12 のインストール
sudo apt install -y build-essential zlib1g-dev libssl-dev libffi-dev python3-pip libsqlite3-dev libbz2-dev libreadline-dev libncursesw5-dev libgdbm-dev liblzma-dev libgdbm-compat-dev
cd /usr/src
sudo wget https://www.python.org/ftp/python/3.12.0/Python-3.12.0.tar.xz
sudo tar -xf Python-3.12.0.tar.xz
cd Python-3.12.0

./configure --enable-optimizations
sudo make -j$(nproc)
sudo make altinstall
python3.12 --version

sudo update-alternatives --install /usr/bin/python python /usr/local/bin/python3.12 1
python --version


