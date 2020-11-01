prob = color

edit: $(prob).o
	cc -m32 $(prob).o -o $(prob)
	rm $(prob).o

install:
	@id=`id -u`; \
	if [ $$id != 0 ] ; \
	then \
		echo \*\*\* Must be root. \*\*\*; \
		exit 1; \
	fi

	useradd -m $(prob)
	echo $(prob):guest | chpasswd
	useradd $(prob)_pwn

	cp * /home/$(prob)

	@echo; \
	read -p "Input flag: " flag; \
	echo $$flag > /home/$(prob)/flag.txt

	chown -R root:root /home/$(prob)
	chmod -R 444 /home/$(prob)
	chmod 555 /home/$(prob)
	chown root:$(prob)_pwn /home/$(prob)/$(prob)
	chmod 2555 /home/$(prob)/$(prob)
	chown root:$(prob)_pwn /home/$(prob)/flag.txt
	chmod 440 /home/$(prob)/flag.txt

$(prob).o: $(prob).c
	cc -c -m32 -fno-stack-protector $(prob).c
