sudo apt-get update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.9 -y

sudo apt install python3-pip -y
pip install boto3
pip install paramiko

sudo git clone https://github.com/OthmanSEBTI/LOG8415_FinalProject.git

mkdir  ~/.aws
# set credantials

python3 ./LOG8415_FinalProject/Sessions_setup.py

