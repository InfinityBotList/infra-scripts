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
	OUTPUT_DIR=tmp/services tmp/service-gen/service-gen service-templates
	mv tmp/services/service-templates/* tmp/services/
	rm -rf tmp/services/service-templates
	@cp -vf tmp/services/* /etc/systemd/system/ || : # Copy to systemd
	cd tmp/services; systemctl enable * || : # Enable all services
	rm -rf tmp
	cp -rf log.sh /usr/bin/log
	mkdir -p /etc/ibl.d
	cp service-templates/_meta.yaml /etc/ibl.d/meta.yaml
	systemctl daemon-reload