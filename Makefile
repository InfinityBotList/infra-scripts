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
	$(foreach file, $(wildcard ./services/*), echo $(file) && ./addtosystemd.sh $(file);)
