import os

# The user should enable password-less ssh from the admin node
def subscription():
    print("Adding a subscription ")
    os.system("subscription-manager register")
    os.system("subscription-manager refresh")
    os.system('subscription-manager list --available --all --matches="*Ceph*"')
    print("Please enter the pool ID for Ceph repos:")
    pool_id = raw_input()
    cmd = "subscription-manager attach --pool="+pool_id
    os.system(cmd)
    os.system('bash subs.sh')

    
    #if (ver == '2'):
     #   os.system("bash subs_2.sh")
    #elif (ver == '3'):
     #   os.system("bash subs_3.sh")




def firewall():
    print("Testing! firewall here")
    os.system("bash /usr/share/ceph-ansible/scripts/auto_ceph/fire.sh")

def hosts():
    mon_no = int(input('Enter number of mon nodes'))
    mon = list()
    print("Enter hostnames for mon : ")
    file_hosts = open('/etc/ansible/hosts','a')
    file_hosts.write("[mons]\n")
    for i in range(0,mon_no):
        a = raw_input()
        mon.append(a)
	file_hosts.write(mon[i]+"\n")
    #print(mon) #prints mon hosts array
    osd_no = int(input('Enter no of osd hosts : '))
    osd = list()
    file_hosts.write("[osds]\n")
    print("Enter hostname for OSDs : ")
    for i in range(0,osd_no):
        a = raw_input()
        osd.append(a)
	file_hosts.write(osd[i]+"\n")
    #print(osd)
    mgr_no = int(input('Enter no of mgr hosts : '))
    mgr = list()
    file_hosts.write("[mgrs]\n")
    print("Enter hostname for MGRs : ")
    for i in range(0,mgr_no):
        a = raw_input()
        mgr.append(a)
        file_hosts.write(mgr[i]+"\n")


def auto_config():
    #configuring all.yml
    pub_net = raw_input("Enter public network ")
    mon_interface = raw_input("Enter monitor interface ")
    admin_user = 'node'
    os.system('mkdir /home/node/ceph-ansible-keys')
    os.system('ln -s /usr/share/ceph-ansible/group_vars /etc/ansible/group_vars')
    os.system('cp /usr/share/ceph-ansible/group_vars/all.yml.sample /usr/share/ceph-ansible/group_vars/all.yml')
    os.system('cp /usr/share/ceph-ansible/group_vars/osds.yml.sample /usr/share/ceph-ansible/group_vars/osds.yml')
    os.system('cp /usr/share/ceph-ansible/site.yml.sample /usr/share/ceph-ansible/site.yml')
    #all.yml config
    file_all = open('/usr/share/ceph-ansible/group_vars/all.yml','a')
    public_network = "\npublic_network: " + pub_net +"\n"
    monitor_interface = "\nmonitor_interface: " + mon_interface+"\n"
    origin = "ceph_origin: repository\n"
    repo = "ceph_repository: rhcs\n"
    repo_type = "ceph_repository_type: cdn\n"
    version = "ceph_rhcs_version: 3\n"
    file_all.write(public_network)
    file_all.write(monitor_interface)
    file_all.write(origin)
    file_all.write(repo)
    file_all.write(repo_type)
    file_all.write(version)
    file_all.close()
    #osds.yml configuration
    fosd = open('/usr/share/ceph-ansible/group_vars/osds.yml','a')
    fosd.write('\nosd_scenario: collocated \n')
    fosd.write('\nosd_auto_discovery: true \n')
    fosd.close()
    #mon_no = int(input('Enter number of mon nodes'))
    #mon = list()
    #print("Enter hostnames for mon")
    #for i in range(0,mon_no):
     #   a = input()
     #   mon.append(mon)
    #osd_no = int(input('Enter no of osd hosts'))
    #osd = list()
    #print("Enter hostname for OSDs")
    #for i in range(0,osd_no):
     #   a = input()
     #   osd.append(a)


def main():
    inp = '1'
    
    while(inp!=0):
        print("-----Deploy Ceph-----")
        print("1. Firewall\n")
        print("2. Subscription\n")
        print("3. Configuring hosts")
	print("4. Auto config")
	print("5. Run the playbook")
        print("6. Purge the cluster")
        print("----------------------\n")
        inp = input("Enter your input:")

        if(inp == '0'):
            exit()
        elif(inp == 1):
            firewall()
        elif(inp == 2):
            #ver = input("Enter version of RHCS to install <2/3>")
            subscription()
            print("Subscription Added")
	elif(inp == 4):
	    print("Configuring Ceph")
	    auto_config()
	    print("Configuration done , Ready for deployment")
        elif(inp == 3):
            print("Configuring hosts")
            hosts()
	elif(inp == 5):
	    #print("Run the following commands for running the playbook")
	    #print("\ncd /usr/share/ceph-ansible \n")
	    #print("ansible-playbook site.yml -v(verbosity)")
	    #os.system('su - node')
	    os.system('su node -c "bash test.sh"')
	elif(inp == 6):
            print("Run the following commands for pruging the cluster")
            print("\ncd /usr/share/ceph-ansible \n")
            print("ansible-playbook infrastructure-playbooks/purge-cluster.yml -v(verbosity)\n")
            os.system('su node -c "bash purge.sh"')
	    
        else:
            print("Enter correct input value")


main()
