# auto_ceph
Set of scripts to minimize admin intervention for Ceph installation.  
Some pre-requisites :  
*Passwordless ssh
*/etc/ansible/hosts configured for ceph deployment
*Ansbile admin user for ceph deployment
*`pool_id` for subscription manager 
## Instructions  
Clone the repo and run the script using `sudo python frame.py`
If you run the script without any argument, it will run the ansible playbook site.yml.  
###Command Line arguments needed for Ceph deployment  
* Value : 1 - Deploying a fresh ceph cluster with subscription, firewall and yml files configured over hosts mentioned in /etc/ansible/hosts.  
* Value : 2 - Purging the existing Ceph cluster. 
By default for this deployment we are considering `osd_scenario : collocated` and `osd_auto_discovery: true` and the hostname for the admin user as `node` which can be changed to something else.  
