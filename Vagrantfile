#ARM/M1 Vmware

# Vagrant.configure("2") do |config|  
#   # Provisioning Python App
#   config.vm.define "pythonproj" do |pythonproj|
#     nodeapp.vm.box = "spox/ubuntu-arm"
#     nodeapp.vm.network "private_network", ip: "192.168.56.30"
#     nodeapp.vm.provider "vmware_fusion" do |vb|
#       pythonproj.vm.synced_folder "app/", "/home/vagrant/app/"
#       pythonproj.vm.synced_folder "env/", "/home/vagrant/env"
#     end
#     nodeapp.vm.provision "shell", inline: <<-SHELL
#       systemctl disable apt-daily.service
#       systemctl disable apt-daily.timer
#       sudo apt remove unattended-upgrades -y
#     SHELL
#     nodeapp.vm.provision "shell", path: "env/script.sh"
#   end
# end

# INTEL/AMD VIRTUAL BOX

Vagrant.configure("2") do |config|
config.vm.define "pythonproj" do |pythonproj|
  pythonproj.vm.box = "generic/ubuntu2010"
  pythonproj.vm.network "private_network", ip: "192.168.56.30"
  pythonproj.hostsupdater.aliases = ["nology.training"]
  pythonproj.vm.provider "virtualbox" do |vb|
    pythonproj.vm.synced_folder "app/", "/home/vagrant/app/"
    pythonproj.vm.synced_folder "env/", "/home/vagrant/env"
  end
  pythonproj.vm.provision "shell", path: "env/script.sh"
end
end

