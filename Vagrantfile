# -*- mode: ruby -*-
# vi: set ft=ruby :

#Vagrant::Config.run do |config|
VAGRANTFILE_API_VERSION = "2"

Vagrant.require_version ">= 1.5"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "trusty"
  config.vm.box_url = "file://ubuntu-14.04.1-server-amd64_virtualbox.box"
  #config.vm.network :hostonly, "192.168.33.8"
  config.vm.network "private_network", ip: "192.168.33.8"
  config.ssh.forward_agent = true
  config.vm.synced_folder ".", "/home/vagrant/spanky"
  config.vm.provider "virtualbox" do |v|
    v.name = "spanky"
    v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    v.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
  end

end