- hosts: map_ip
  tasks: 
  - copy:
      src: /root/mymap.xml
      dest: /etc/hadoop/mapred-site.xml

