make
curl --ftp-method nocwd -T X-Raiders.self ftp://192.168.1.59:1337/ux0:/app/X-RAIDERS1/eboot.bin
echo launch X-RAIDERS1 | ./nc.exe 192.168.1.59 1338
