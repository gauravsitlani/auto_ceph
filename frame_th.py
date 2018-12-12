#pre-requisites - passwordless ssh ; get a pool_id for subscription ; /etc/ansible/hosts file - to get the hosts ; username for ansible-admin
# add more for other enhancements 
# by default the script runs the playbook directly if no arguments specified

import os
import getpass
import re
import sys
from multiprocessing.dummy import Pool

#Getting hosts from /etc/ansible/hosts
hosts_exp = re.compile('[a-z]+')
brack = re.compile('^\[')
hsh = re.compile('^#')
letters = re.compile('[a-z0-9]+')
hosts = list()
with open('/etc/ansible/hosts', 'r') as fobj:
            a = fobj.readlines()
for i in range(0,len(a)):
     if(brack.match(a[i]) or hsh.match(a[i])):
         continue
     else:
         lt = a[i].split('\n')
         hosts.append(lt[0])
hosts = list(set(hosts))
print(hosts)

#CLI  which seems to be necessary
#Commands : 
username = raw_input("Enter username for subscription-manager : ")
passwrd = getpass.getpass(prompt='Enter password for subscription manager : ')
print("Please enter the pool ID for Ceph repos:")
pool_id = raw_input()
attach_pool = "subscription-manager attach --pool="+pool_id
register = "subscription-manager register --username="+username+" --password='"+passwrd+"'"
os.system('touch /root/subs.sh')
with open('/root/subs.sh','w') as sub:
	sub.write(register)

#print(register)
refresh = "subscription-manager refresh"
subs_disable = "subscription-manager repos --disable=*"
enable_repo1 = "subscription-manager repos --enable=rhel-7-server-rpms"
enable_repo2 = "subscription-manager repos --enable=rhel-7-server-extras-rpms"
yum_update = "yum update -y"
install1 = "yum install yum-utils vim -y"
install2 = "yum install bash-completion -y"
enable_repo3 = "subscription-manager repos --enable=rhel-7-server-rhceph-3-mon-rpms"
enable_repo4 = "subscription-manager repos --enable=rhel-7-server-rhceph-3-osd-rpms"
enable_repo5 = "subscription-manager repos --enable=rhel-7-server-rhceph-3-tools-rpms"
enable_repo6 = "subscription-manager repos --enable=rhel-7-server-ansible-2.4-rpms"
install3 = "yum install ceph-ansible -y"


# The user should enable password-less ssh from the admin node
def subscription(host):
   if(letters.match(host)):
       os.system('ssh root@'+host+' systemctl disable firewalld')
       os.system('ssh root@'+host+' systemctl stop firewalld')
       os.system('scp /root/subs.sh root@'+host+':/root/subs.sh')
       os.system('ssh root@'+host+' bash /root/subs.sh')
       os.system('ssh root@'+host+' '+refresh)
       os.system('ssh root@'+host+' '+attach_pool)
       os.system('ssh root@'+host+' '+subs_disable)
       os.system('ssh root@'+host+' '+enable_repo1)
       os.system('ssh root@'+host+' '+enable_repo2)
       os.system('ssh root@'+host+' '+yum_update)
       os.system('ssh root@'+host+' '+install1)
       os.system('ssh root@'+host+' '+install2)
       os.system('ssh root@'+host+' '+enable_repo3)
       os.system('ssh root@'+host+' '+enable_repo4)
       os.system('ssh root@'+host+' '+enable_repo5)

#pool = Pool(13)
#pool.map(subscription,hosts)
#pool.close()
#pool.join()

#os.system(enable_repo6)
#os.system(install3)

#os.system("sed -i 's+fetch_directory: ~/ceph-ansible-keys+fetch_directory: /root/ceph-ansible-keys+g' /usr/share/ceph-ansible/group_vars/all.yml")

def auto_config():
    #configuring all.yml
    pub_net = raw_input("Enter public network ")
    mon_interface = raw_input("Enter monitor interface ")
    makedir = "mkdir /root/ceph-ansible-keys"
    os.system(makedir)
    #os.system('ln -s /usr/share/ceph-ansible/group_vars /etc/ansible/group_vars')
    os.system('cp /usr/share/ceph-ansible/group_vars/all.yml.sample /usr/share/ceph-ansible/group_vars/all.yml')
    os.system('cp /usr/share/ceph-ansible/group_vars/osds.yml.sample /usr/share/ceph-ansible/group_vars/osds.yml')
    os.system('cp /usr/share/ceph-ansible/site.yml.sample /usr/share/ceph-ansible/site.yml')
    #all.yml config
    public_network = "\npublic_network: " + pub_net +"\n"
    monitor_interface = "\nmonitor_interface: " + mon_interface+"\n"
    repo_type = "ceph_repository_type: cdn\n"
    with open('/usr/share/ceph-ansible/group_vars/all.yml', 'a') as all_obj:
	all_obj.write(repo_type)
	all_obj.write(monitor_interface)
	all_obj.write(public_network)
	#osds.yml configuration
    with open('/usr/share/ceph-ansible/group_vars/osds.yml', 'a') as osd_obj:
    	osd_obj.write('\nosd_auto_discovery: true \n')
	osd_obj.write('\nosd_scenario: collocated \n')

auto_config()
os.system('bash test.sh')
for host in hosts:
	os.system('ssh root@'+host+' rm -rf /root/subs.sh')
