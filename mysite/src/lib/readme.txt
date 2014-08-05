1.将sourcecode/lib文件夹中的mod_wsgi.so文件复制到apache/modules文件夹下
2.将sourcecode/lib文件夹中的httpd-wsgi.conf文件复制到apache/conf/extra文件夹下
3.修改httpd-wsgi.conf文件，在<VirtualHost *:88></VirtualHost>之间有关本项目的路径，都改成本机上的路径。
4.修改apache/conf文件夹下的httpd.conf文件，添加一行【Include "conf/extra/httpd-wsgi.conf"】保存。
5.重启apache。
