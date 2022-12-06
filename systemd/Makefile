# makefile for installing service

SERVICE=rgbxmastree.service

install: /etc/systemd/system/$(SERVICE)

/etc/systemd/system/$(SERVICE): $(SERVICE)
	sudo cp $(SERVICE) $@
	sudo /bin/systemctl daemon-reload
