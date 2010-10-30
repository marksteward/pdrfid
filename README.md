
    sudo apt-get install pcscd libpcsclite1 python-pyscard
    sudo service pcscd start
    sudo wget -O /usr/share/pcsc/smartcard_list.txt http://ludovic.rousseau.free.fr/softwares/pcsc-tools/smartcard_list.txt
    ./pdrfid.py -L
    ./pdrfid.py -r0

