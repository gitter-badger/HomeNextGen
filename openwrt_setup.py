import subprocess
import re
import shutil

try:
    import pytoml as toml
except:
    import pip
    pip.main(['install', 'pytoml'])
    import pytoml as toml


#NOTE: After 'feeds install', '.config' is reflecting the installs only after saving the 'menuconfig'. So save after running the script first
#NOTE: Rerun this script
#NOTE: Make sure you do 'make menuconfig' and save to enable dependent packages on the packages that you have enabled

#Base System:
	#block-mount
#Kernel modules -> Other Modules:
	#kmod-bluetooth
	#kmod-bluetooth_6lowpan
#Kernel modules ->USB Support:
	#kmod-usb-core
	#kmod-usb-ohci
	#kmod-usb-storage
	#kmod-usb2
#Libraries:
	#bluez-libs
#Utilities:
	#bluez-utils


def package_enable_disable(package_name, option):
    shutil.copyfile('./openwrt/.config', './openwrt/.oldconfig')

    package = 'CONFIG_PACKAGE_' + package_name
    package = package.encode('utf-8')

    with open('./openwrt/.config', 'r') as f, open('./openwrt/.newconfig', 'w') as new_config:
        for line in f:
            package_select = re.split(' |=', line, 2)
            if package in package_select:
                if option == 'y' and package_select[1] != 'y\n' and package_select[2] == 'is not set\n':
                    print('enabling` -->', package_name)
                    new_config.write(package + '=y\n')
                elif option == 'n' and package_select[1] == 'y\n':
                    print('disbling -->', package_name)
                    new_config.write('# ' + package + ' is not set\n')
                else:
                    if option == 'y':
                        print(package_name + ' already enabled')
                    elif option == 'n':
                        print(package_name + ' already disabled')
            else:
                new_config.write(line)
    shutil.copyfile('./openwrt/.newconfig', './openwrt/.config')


def execute_command(command):
    popen = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    print(output)


def package_install(package):
    print('@@@@@@ installing ' + package + ' @@@@@@')
    package_install_command = './openwrt/scripts/feeds install ' + package
    execute_command(package_install_command)

#there is no .config file in the beginning. create a .config with basic config
execute_command("make -C ./openwrt defconfig")

#download all the feeds
execute_command("./openwrt/scripts/feeds update -a")

#install and enable packages based on config file
with open('packages.toml', 'rb') as f:
    config = toml.load(f)
    for section in config:
        if section == 'install_enable':
            categories = config[section]
            for category in categories:
                packages = categories[category]
                for package in packages:
                    package_install(package)
            # package won't be available in .config first time after install.
            # menuconfig should be save for these sections to reflect in .config
            # do something here to simulate that
            execute_command("make -C ./openwrt defconfig")
            for category in categories:
                packages = categories[category]
                for package in packages:
                    package_enable_disable(package, 'y')

        if section == 'enable':
            categories = config[section]
            for category in categories:
                packages = categories[category]
                for package in packages:
                   package_enable_disable(package, 'y')

#by now, your packages have been enabled, but not their dependencies
execute_command("make -C ./openwrt defconfig")
