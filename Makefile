inf:
	@echo "Select from 'nginx' or 'systemd' target(s). If starting out, do the 'all' target"

all: 
	@make nginx 
	@make systemd

.PHONY: nginx
nginx:
	rm -rf /etc/nginx
	cp -rf nginx /etc/
	nginx -t

systemd:
	@echo "Compiling service-gen"
	@mkdir tmp tmp/services tmp/services/service-templates
	cd tmp; git clone https://github.com/Infinitybotlist/service-gen; cd service-gen; go build -v;
	SERVICE_DIR=service-templates OUTPUT_DIR=tmp/services tmp/service-gen/service-gen all
	mv tmp/services/service-templates/* tmp/services/
	rm -rf tmp/services/service-templates
	@cp services/zfsmongo.service tmp/services/ # Add zfsmongo manually as it is not templatable+core infra service
	@cp services/*.target tmp/services/ # Add targets 
	@cp -vf tmp/services/* /etc/systemd/system/ || : # Copy to systemd
	cd tmp/services; systemctl enable * || : # Enable all services
	rm -rf tmp
	cp -rf log.sh /usr/bin/log
	systemctl daemon-reload