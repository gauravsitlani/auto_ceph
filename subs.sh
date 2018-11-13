subscription-manager repos --disable=*
subscription-manager repos --enable=rhel-7-server-rpms
subscription-manager repos --enable=rhel-7-server-extras-rpms
yum update -y
yum install yum-utils vim -y
yum install bash-completion -y
yum-config-manager --disable epel
subscription-manager repos --enable=rhel-7-server-rhceph-3-mon-rpms
subscription-manager repos --enable=rhel-7-server-rhceph-3-osd-rpms
subscription-manager repos --enable=rhel-7-server-rhceph-3-tools-rpms
subscription-manager repos --enable=rhel-7-server-ansible-2.4-rpms
yum install ceph-ansible -y

