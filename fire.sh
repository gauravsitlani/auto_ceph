systemctl enable firewalld
systemctl start firewalld
firewall-cmd --permanent --add-port=6789/tcp
firewall-cmd --permanent --add-port=6800-7300/tcp
firewall-cmd --permanent --add-port=7480/tcp
firewall-cmd --permanent --add-port=80/tcp
firewall-cmd --permanent --add-port=443/tcp
firewall-cmd --reload

systemctl status firewalld
firewall-cmd --list-all





