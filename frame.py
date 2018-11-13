import subprocess
import os

# The user should enable password-less ssh from the admin node
def subscription():
    print("Adding a subscription ")
    #subprocess.call(["subscription-manager","register"])
    #subprocess.call(["subscription-manager", "refresh"])
    os.system('subscription-manager list --available --all --matches="*Ceph*"')
    print("Please enter the pool ID for Ceph repos:")
    pool_id = input()
    cmd = "subscription-manager attach --pool="+pool_id
    #if (ver == '2'):
     #   os.system("bash subs_2.sh")
    #elif (ver == '3'):
     #   os.system("bash subs_3.sh")

    print(type(cmd))



def firewall():
    print("Testing! firewall here")
    #subprocess.call(["bash fire.sh"])

def pwdless_ssh():
    no = input("Enter the number of hosts on which you want to deploy\n")
    hosts = list()
    print("Enter hostnames and their ip addresses in format : <ip> <hostname>")
    for i in range(0,int(no)):
        a = input()
        hosts.append(a)
    print(hosts)
    

def auto_config():
    #configuring all.yml
    pub_net = input("Enter public network ")
    mon_interface = input("Enter monitor interface")
    admin_user = 'node'
    os.system('mkdir /home/node/ceph-ansible-keys')
    os.system('ln -s /usr/share/ceph-ansible/group_vars /etc/ansible/group_vars')
    os.system('cp /usr/share/ceph-ansible/group_vars/all.yml.sample /usr/share/ceph-ansible/group_vars/all.yml')
    os.system('cp /usr/share/ceph-ansible/group_vars/osds.yml.sample /usr/share/ceph-ansible/group_vars/osds.yml')
    os.system('cp /usr/share/ceph-ansible/site.yml.sample /usr/share/ceph-ansible/site.yml')
    #all.yml config
    file_all = open('testall.yml','a')
    public_network = "\npublic_network: " + pub_net +"\n"
    monitor_interface = "\nmonitor_interface: " + mon_interface+"\n"
    file_all.write(public_network)
    file_all.write(monitor_interface)

    #osds.yml configuration
    fosd = open('testosds.yml','a')
    fosd.write('\nosd_scenario: collocated \n')
    fosd.write('\nosd_auto_discovery: true \n')
    fosd.close()
    mon_no = int(input('Enter number of mon nodes'))
    mon = list()
    print("Enter hostnames for mon")
    for i in range(0,mon_no):
        a = input()
        mon.append(mon)
    osd_no = int(input('Enter no of osd hosts'))
    osd = list()
    print("Enter hostname for OSDs")
    for i in range(0,osd_no):
        a = input()
        osd.append(a)


def main():
    inp = '1'
    
    while(inp!=0):
        print("-----Deploy Ceph-----")
        print("1. Firewall\n")
        print("2. Subscription\n")
        print("3. Enabling password-less ssh")
        print("----------------------\n")
        inp = input("Enter your input:")

        if(inp == '0'):
            exit()
        elif(inp == '1'):
            firewall()
        elif(inp == '2'):
            #ver = input("Enter version of RHCS to install <2/3>")
            subscription()
        elif(inp == '3'):
            pwdless_ssh()
        else:
            print("Enter correct input value")


main()


