import subprocess
import re
import shutil

config_file = './openwrt/.config'

def package_enable_disable(package_name, option):

    shutil.copyfile('./openwrt/.config', './openwrt/.oldconfig')

    package = 'CONFIG_PACKAGE_' + package_name
    with open(config_file, 'r') as f, open('./openwrt/.newconfig', 'w') as new_config:
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
                    print('already ' + option)
            else:
                new_config.write(line)
    shutil.copyfile('./openwrt/.newconfig', './openwrt/.config')



feeds_util = './openwrt/scripts/feeds '

update = feeds_util + 'update -a'

basic = "luci file "
ble = "libexpat bluez-utils bluez-libs "

packages_install = feeds_util + 'install ' + basic + ble 

for arg in [update, packages_install]:
    popen = subprocess.Popen(arg.split(), stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    print(output)

for package in basic.split() + ble.split():
    package_enable_disable(package, 'y')


