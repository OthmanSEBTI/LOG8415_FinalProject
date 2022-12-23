# LOG8415_FinalProject

# Requirements

- clonning the project repo in local machin
- crendentials and config file in ~/.aws folder
- python, pip and necessary modules boto3, paramiko, ping should be installed in local machine (commands provided bellow)

sudo apt-get update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.9 -y

sudo apt install python3-pip -y
sudo pip install boto3
sudo pip install paramiko
sudo pip install ping3

# Instructions to run the code

steps to run in the order:

1. copy the aws credentials and config to 'LOG8415_FinalProject/credentials' and 'LOG8415_FinalProject/config'
2. execute Infrastructure_setup.py to create key pair, security group, and instances
3. copy the private DNS name of the private ip for the cluster instances in 'LOG8415_FinalProject/Cluster_setup/config_content' (all adresses)
4. copy the private DNS name of the public ip for the cluster instances in the following files: 'LOG8415_FinalProject/Cluster_setup/Slave_setup.sh' Line 2 (only the master adress)
   'LOG8415_FinalProject/Benchmark.py' Line 26 and Line 34 (only the master adress)
   'LOG8415_FinalProject/Proxy_app_random.py' Line 13 (only the master adress)
   'LOG8415_FinalProject/Proxy_app_customize.py' Line 7 to 10 (all adresses)
5. push the modifications in the git repo
6. execute Sessions_setup.py to establish ssh sessions
7. execute Environnement_deployment.py for setting the standalone mysql and the cluster and the proxy with all the installations and necessary steps
8. run Benchmark.py to launch the benchmark on the cluster and standalone
9. run Main_proxy_app.py for launching the proxy application
