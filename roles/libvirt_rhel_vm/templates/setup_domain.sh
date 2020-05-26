#!/usr/bin/env bash

set -ex -o pipefail

# exit 0 = success, no changes
# exit 1 = error
# exit 2 = success, changes

domain_name="{{ libvirt_rhel_vm_domain.name }}"

if [[ $(virsh domid "${domain_name}") ]]; then
	exit 0
fi

cd "{{ libvirt_rhel_vm_storage }}"

# Create an empty qcow2 file for a base image
qemu-img create -f qcow2 "${domain_name}.qcow2" "{{ libvirt_rhel_vm_domain.disk }}"

# Use virt-resize to dump the guest image into the qcow2 file we just created.
virt-resize \
  --expand /dev/sda1 "{{ libvirt_rhel_vm_domain.img_path | basename }}" \
  "${domain_name}.qcow2"

# - Remove cloud-init (causes delays and problems when not used on a cloud)
# - Set UseDNS=no for initial login
# - Set root user password
# - Inject root user SSH key
# - Copy in templated domain NIC configs
virt-customize \
  -a "${domain_name}.qcow2" \
  --run-command "yum remove cloud-init* -y; sed -i 's/^#UseDNS.*\$/UseDNS no/g' /etc/ssh/sshd_config" \
  --root-password password:'{{ libvirt_rhel_vm_domain.root_passwd }}' \
{% for key in libvirt_rhel_vm_domain.root_ssh_pub_keys %}
  --ssh-inject root:string:"{{ key }}" \
{% endfor %}
  --copy-in "{{ libvirt_rhel_vm_nic_config_path }}:/etc/sysconfig/" \
  --selinux-relabel

virt-install \
  --ram "{{ libvirt_rhel_vm_domain.ram | mandatory }}" \
  --vcpus "{{ libvirt_rhel_vm_domain.vcpus | mandatory }}" \
  --os-variant "{{ libvirt_rhel_vm_domain['os-variant'] }}" \
  --disk "path={{ libvirt_rhel_vm_storage }}/${domain_name}.qcow2,device=disk,bus=virtio,format=qcow2" \
  --import \
  --noautoconsole \
  --vnc \
{% for bridge in libvirt_rhel_vm_domain.bridges %}
  --bridge "{{ bridge }}" \
{% endfor %}
  --autostart \
  --name "${domain_name}"

exit 2
