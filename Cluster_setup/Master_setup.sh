sudo mkdir -p /opt/mysqlcluster/deploy
cd /opt/mysqlcluster/deploy
sudo mkdir conf
sudo mkdir mysqld_data
sudo mkdir ndb_data
cd conf
echo | cat /home/ubuntu/LOG8415_FinalProject/Cluster_setup/mycnf_content | sudo tee -a my.cnfg
echo | cat /home/ubuntu/LOG8415_FinalProject/Cluster_setup/configini_content | sudo tee -a config.ini
