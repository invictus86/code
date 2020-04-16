import os, shutil


def copyfile_to_folder(sourceDir, targetDir):
    """
    copy source file to target file
    :param sourceDir: source file (str)
    :param targetDir: target file (str)
    :return: None
    """
    shutil.copy(sourceDir, targetDir)
    print "copy file success"


def modify_file_version(old_file_path, new_file_path, old_str1, new_str1):
    with open(old_file_path, "r") as f1, open(new_file_path, "w") as f2:
        for line in f1:
            if old_str1 in line:
                line = line.replace(old_str1, new_str1)
            f2.write(line)
    print "generate new file {} success".format(new_file_path)


def make_vmlinux_fsi_size():
    big_app_size = int(9.6 * 1024 * 1024)

    old_file_path = "./cut.sh"
    new_file_path = "./cut_big_vmlinux_size.sh"

    old_str1 = "./cutsize ./bootlogo.bin 262144  "
    new_str_1 = "./cutsize ./vmlinux.bin {}  ".format(big_app_size)

    modify_file_version(old_file_path, new_file_path, old_str1, new_str_1)
    print "make_big_app_size file Generate complete"
    os.system('chmod -R 777 ./*')
    os.system('./cut_big_vmlinux_size.sh')
    os.rename("image_cut.bin", "big_vmlinux_size.bin")


def make_big_fsi_size():
    big_app_size = 23 * 1024 * 1024

    old_file_path = "./cut.sh"
    new_file_path = "./cut_big_fsi_size.sh"

    old_str1 = "./cutsize ./bootlogo.bin 262144  "
    new_str_1 = "./cutsize ./fsi.bin {}  ".format(big_app_size)

    modify_file_version(old_file_path, new_file_path, old_str1, new_str_1)
    print "make_big_app_size file Generate complete"
    os.system('chmod -R 777 ./*')
    os.system('./cut_big_fsi_size.sh')
    os.rename("image_cut.bin", "big_fsi_size.bin")


def make_big_bootlogo_size():
    big_bootlogo_size = 800 * 1024

    old_file_path = "./cut.sh"
    new_file_path = "./cut_big_bootlogo_size.sh"

    old_str1 = "./cutsize ./bootlogo.bin 262144  "
    new_str_1 = "./cutsize ./bootlogo.bin {}  ".format(big_bootlogo_size)

    modify_file_version(old_file_path, new_file_path, old_str1, new_str_1)
    print "make_big_bootlogo_size file Generate complete"

    os.system('chmod -R 777 ./*')
    os.system('./cut_big_bootlogo_size.sh')
    os.rename("image_cut.bin", "big_bootlogo_size.bin")


def make_big_see_size():
    big_bootlogo_size = 4 * 1024 * 1024

    old_file_path = "./cut.sh"
    new_file_path = "./cut_big_see_size.sh"

    old_str1 = "./cutsize ./bootlogo.bin 262144  "
    new_str_1 = "./cutsize ./see.ubo {}  ".format(big_bootlogo_size)

    modify_file_version(old_file_path, new_file_path, old_str1, new_str_1)
    print "make_big_bootlogo_size file Generate complete"

    os.system('chmod -R 777 ./*')
    os.system('./cut_big_see_size.sh')
    os.rename("image_cut.bin", "big_see_size.ubo")


def make_big_cfg_size():
    big_bootlogo_size = 0.4 * 1024 * 1024

    old_file_path = "./cut.sh"
    new_file_path = "./cut_big_cfg_size.sh"

    old_str1 = "./cutsize ./bootlogo.bin 262144  "
    new_str_1 = "./cutsize ./EKT_CFG_DATA.squashfs {}  ".format(big_bootlogo_size)

    modify_file_version(old_file_path, new_file_path, old_str1, new_str_1)
    print "make_big_cfg_size file Generate complete"

    os.system('chmod -R 777 ./*')
    os.system('./cut_big_cfg_size.sh')
    os.rename("image_cut.bin", "big_cfg_size.squashfs")


def make_excessive_big_vmlinux_size():
    excessive_big_app_size = 13 * 1024 * 1024

    old_file_path = "./cut.sh"
    new_file_path = "./cut_excessive_big_vmlinux_size.sh"

    old_str1 = "./cutsize ./bootlogo.bin 262144  "
    new_str_1 = "./cutsize ./vmlinux.bin {}  ".format(excessive_big_app_size)

    modify_file_version(old_file_path, new_file_path, old_str1, new_str_1)
    print "make_excessive_big_app_size file Generate complete"
    os.system('chmod -R 777 ./*')
    os.system('./cut_excessive_big_vmlinux_size.sh')
    os.rename("image_cut.bin", "excessive_big_vmlinux_size.bin")


def make_excessive_big_fsi_size():
    excessive_big_app_size = 27 * 1024 * 1024

    old_file_path = "./cut.sh"
    new_file_path = "./cut_excessive_big_fsi_size.sh"

    old_str1 = "./cutsize ./bootlogo.bin 262144  "
    new_str_1 = "./cutsize ./fsi.bin {}  ".format(excessive_big_app_size)

    modify_file_version(old_file_path, new_file_path, old_str1, new_str_1)
    print "make_excessive_big_app_size file Generate complete"
    os.system('chmod -R 777 ./*')
    os.system('./cut_excessive_big_fsi_size.sh')
    os.rename("image_cut.bin", "excessive_big_fsi_size.bin")


def make_excessive_big_bootlogo_size():
    excessive_big_bootlogo_size = int(1.1 * 1024 * 1024)

    old_file_path = "./cut.sh"
    new_file_path = "./cut_excessive_big_bootlogo_size.sh"

    old_str1 = "./cutsize ./bootlogo.bin 262144  "
    new_str_1 = "./cutsize ./bootlogo.bin {}  ".format(excessive_big_bootlogo_size)

    modify_file_version(old_file_path, new_file_path, old_str1, new_str_1)
    print "make_excessive_big_app_size file Generate complete"
    os.system('chmod -R 777 ./*')
    os.system('./cut_excessive_big_bootlogo_size.sh')
    os.rename("image_cut.bin", "excessive_big_bootlogo_size.bin")


def make_excessive_big_see_size():
    excessive_big_bootlogo_size = int(6 * 1024 * 1024)

    old_file_path = "./cut.sh"
    new_file_path = "./cut_excessive_big_see_size.sh"

    old_str1 = "./cutsize ./bootlogo.bin 262144  "
    new_str_1 = "./cutsize ./see.ubo {}  ".format(excessive_big_bootlogo_size)

    modify_file_version(old_file_path, new_file_path, old_str1, new_str_1)
    print "make_excessive_big_app_size file Generate complete"
    os.system('chmod -R 777 ./*')
    os.system('./cut_excessive_big_see_size.sh')
    os.rename("image_cut.bin", "excessive_big_see_size.ubo")


def make_excessive_big_cfg_size():
    excessive_big_bootlogo_size = int(0.6 * 1024 * 1024)

    old_file_path = "./cut.sh"
    new_file_path = "./cut_excessive_big_cfg_size.sh"

    old_str1 = "./cutsize ./bootlogo.bin 262144  "
    new_str_1 = "./cutsize ./EKT_CFG_DATA.squashfs {}  ".format(excessive_big_bootlogo_size)

    modify_file_version(old_file_path, new_file_path, old_str1, new_str_1)
    print "make_excessive_big_app_size file Generate complete"
    os.system('chmod -R 777 ./*')
    os.system('./cut_excessive_big_cfg_size.sh')
    os.rename("image_cut.bin", "excessive_big_cfg_size.squashfs")


make_vmlinux_fsi_size()
make_big_fsi_size()
make_big_bootlogo_size()
make_big_see_size()
make_excessive_big_vmlinux_size()
make_excessive_big_fsi_size()
make_excessive_big_bootlogo_size()
make_excessive_big_see_size()
