# auto_ceph
Set of scripts to minimize admin intervention for Ceph installation.  
Passwordless ssh is a pre-requisite for running this script.
## Instructions  
Clone the repo and run the script using `python frame.py`
The menu will be displayed, before running the deployment, steps 1 and 2 are compulsory which will configure firewall and subscription. Currently the script needs to be run on all host nodes for step 1 & 2 which can be further automated.  
```
-----Deploy Ceph-----  
1. Firewall  

2. Subscription  

3. Configuring hosts  
4. Auto config  
5. Run the playbook  
6. Purge the cluster  
----------------------  
  
Enter your input:  
```  
By default for this deployment we are considering `osd_scenario : collocated` and `osd_auto_discovery: true` and the hostname for the admin user as `node` which can be changed to something else.  
