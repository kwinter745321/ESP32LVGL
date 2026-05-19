#
# WiFi connection and services startup
#
/home/secret.sh

wifi sta on         # Turn on wifi
wifi sta status
#wifi sta scan      # scan wifi APs

wifi sta connect $SSID $PASSWORD 20 # SSID PASS Timeout
wifi sta status -n
if $wa == False goto exit # wifi active
if $wc == False goto exit # wifi connected

ntpupdate us.pool.ntp.org

date

wifi sta ifconfig

#utelnetd start
#uftpd start
uhttpd start 

:exit
