import os


def modify_file_version1(old_file_path, new_file_path, old_str1, new_str1, old_str20, new_str20, old_str30, new_str30):
    with open(old_file_path, "r") as f1, open(new_file_path, "w") as f2:
        for line in f1:
            if old_str1 in line:
                line = line.replace(old_str1, new_str1)
            if old_str20 in line:
                line = line.replace(old_str20, new_str20)
            if old_str30 in line:
                line = line.replace(old_str30, new_str30)
            f2.write(line)
    print "generate new file {} success".format(new_file_path)


def modify_file_version2(old_file_path, new_file_path, old_str1, new_str1, old_str2, new_str2, old_str20, new_str20,
                         old_str30, new_str30):
    with open(old_file_path, "r") as f1, open(new_file_path, "w") as f2:
        for line in f1:
            if old_str1 in line:
                line = line.replace(old_str1, new_str1)
            if old_str2 in line:
                line = line.replace(old_str2, new_str2)
            if old_str20 in line:
                line = line.replace(old_str20, new_str20)
            if old_str30 in line:
                line = line.replace(old_str30, new_str30)
            f2.write(line)
    print "generate new file {} success".format(new_file_path)


def modify_file_version3(old_file_path, new_file_path, old_str1, new_str1, old_str2, new_str2, old_str3, new_str3,
                         old_str20, new_str20, old_str30, new_str30):
    with open(old_file_path, "r") as f1, open(new_file_path, "w") as f2:
        for line in f1:
            if old_str1 in line:
                line = line.replace(old_str1, new_str1)
            if old_str2 in line:
                print old_str2, new_str2
                line = line.replace(old_str2, new_str2)
            if old_str3 in line:
                line = line.replace(old_str3, new_str3)
            if old_str20 in line:
                line = line.replace(old_str20, new_str20)
            if old_str30 in line:
                line = line.replace(old_str30, new_str30)
            f2.write(line)
    print "generate new file {} success".format(new_file_path)


def modify_file_version4(old_file_path, new_file_path, old_str1, new_str1, old_str2, new_str2, old_str3, new_str3,
                         old_str4, new_str4, old_str20, new_str20, old_str30, new_str30):
    with open(old_file_path, "r") as f1, open(new_file_path, "w") as f2:
        for line in f1:
            if old_str1 in line:
                line = line.replace(old_str1, new_str1)
            if old_str2 in line:
                print old_str2, new_str2
                line = line.replace(old_str2, new_str2)
            if old_str3 in line:
                line = line.replace(old_str3, new_str3)
            if old_str4 in line:
                line = line.replace(old_str4, new_str4)
            if old_str20 in line:
                line = line.replace(old_str20, new_str20)
            if old_str30 in line:
                line = line.replace(old_str30, new_str30)
            f2.write(line)
    print "generate new file {} success".format(new_file_path)


def modify_file_version9(old_file_path, new_file_path, old_str1, new_str1, old_str2, new_str2, old_str3, new_str3,
                         old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40, new_str40,
                         old_str50, new_str50, old_str60, new_str60):
    with open(old_file_path, "r") as f1, open(new_file_path, "w") as f2:
        for line in f1:
            if old_str1 in line:
                line = line.replace(old_str1, new_str1)
            if old_str2 in line:
                print old_str2, new_str2
                line = line.replace(old_str2, new_str2)
            if old_str3 in line:
                line = line.replace(old_str3, new_str3)
            if old_str4 in line:
                line = line.replace(old_str4, new_str4)
            if old_str20 in line:
                line = line.replace(old_str20, new_str20)
            if old_str30 in line:
                line = line.replace(old_str30, new_str30)
            if old_str40 in line:
                line = line.replace(old_str40, new_str40)
            if old_str50 in line:
                line = line.replace(old_str50, new_str50)
            if old_str60 in line:
                line = line.replace(old_str60, new_str60)
            f2.write(line)
    print "generate new file {} success".format(new_file_path)


def modify_file_version10(old_file_path, new_file_path, old_str1, new_str1, old_str2, new_str2, old_str3, new_str3,
                          old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40, new_str40,
                          old_str50, new_str50, old_str60, new_str60, old_str70, new_str70):
    with open(old_file_path, "r") as f1, open(new_file_path, "w") as f2:
        for line in f1:
            if old_str1 in line:
                line = line.replace(old_str1, new_str1)
            if old_str2 in line:
                print old_str2, new_str2
                line = line.replace(old_str2, new_str2)
            if old_str3 in line:
                line = line.replace(old_str3, new_str3)
            if old_str4 in line:
                line = line.replace(old_str4, new_str4)
            if old_str20 in line:
                line = line.replace(old_str20, new_str20)
            if old_str30 in line:
                line = line.replace(old_str30, new_str30)
            if old_str40 in line:
                line = line.replace(old_str40, new_str40)
            if old_str50 in line:
                line = line.replace(old_str50, new_str50)
            if old_str60 in line:
                line = line.replace(old_str60, new_str60)
            if old_str70 in line:
                line = line.replace(old_str70, new_str70)
            f2.write(line)
    print "generate new file {} success".format(new_file_path)


def modify_file_version11(old_file_path, new_file_path, old_str1, new_str1, old_str2, new_str2, old_str3, new_str3,
                          old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40, new_str40,
                          old_str50, new_str50, old_str60, new_str60, old_str70, new_str70, old_str80, new_str80):
    with open(old_file_path, "r") as f1, open(new_file_path, "w") as f2:
        for line in f1:
            if old_str1 in line:
                line = line.replace(old_str1, new_str1)
            if old_str2 in line:
                print old_str2, new_str2
                line = line.replace(old_str2, new_str2)
            if old_str3 in line:
                line = line.replace(old_str3, new_str3)
            if old_str4 in line:
                line = line.replace(old_str4, new_str4)
            if old_str20 in line:
                line = line.replace(old_str20, new_str20)
            if old_str30 in line:
                line = line.replace(old_str30, new_str30)
            if old_str40 in line:
                line = line.replace(old_str40, new_str40)
            if old_str50 in line:
                line = line.replace(old_str50, new_str50)
            if old_str60 in line:
                line = line.replace(old_str60, new_str60)
            if old_str70 in line:
                line = line.replace(old_str70, new_str70)
            if old_str80 in line:
                line = line.replace(old_str80, new_str80)
            f2.write(line)
    print "generate new file {} success".format(new_file_path)


def make_app_file():
    new_str_dict = {1006: [1001, 1001], 1007: [1002, 1002], 1008: [1003, 1003], 1009: [1004, 1004], 1010: [1005, 1005],
                    20001: [20001, 20001], 998: [1000, 1000], 988: [988, 988], 991: [1000, 1000]}
    old_file_path = "./ekt_loader_tool.cfg"
    new_file_path = "./ekt_loader_tool-app-{}.cfg"
    old_str1 = "DSN 1000"
    old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
    old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
    old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
    old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'

    old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAOutputFile "UpgradeFile.ts"'

    for dsn_ver, [vmlinux_ver, fsi_ver] in new_str_dict.items():
        new_file_path = new_file_path.format(dsn_ver)
        new_str_1 = "DSN {}".format(dsn_ver)
        new_str2 = 'InputFileNumber 2'

        new_str3 = 'InputFile1 "4 vmlinux.bin 1 {}"'.format(vmlinux_ver)
        new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
        new_str20 = ''
        new_str30 = ''
        new_str40 = ''

        new_str50 = 'USBOutputFile "./7414v-103/{}/UpgradeFile.bin"'.format(dsn_ver)
        new_str60 = 'OTAOutputFile "./7414v-103/{}/UpgradeFile.ts"'.format(dsn_ver)

        modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                             new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                             new_str40, old_str50, new_str50, old_str60, new_str60)
        new_file_path = "./ekt_loader_tool-app-{}.cfg"


def make_same_low_app_file():
    new_str_dict = {998: [1002, 1002], 1002: [998, 998], 1000: [1002, 1002], 1003: [1000, 1000]}
    old_file_path = "./ekt_loader_tool.cfg"
    new_file_path = "./ekt_loader_tool-s-l-app-{}.cfg"
    old_str1 = "DSN 1000"
    old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
    old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
    old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
    old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'

    old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAOutputFile "UpgradeFile.ts"'

    for dsn_ver, [vmlinux_ver, fsi_ver] in new_str_dict.items():
        if dsn_ver == 998 or dsn_ver == 1002:
            new_file_path = new_file_path.format(dsn_ver)
            new_str_1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 2'

            new_str3 = 'InputFile1 "4 vmlinux.bin 1 {}"'.format(vmlinux_ver)
            new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
            new_str20 = ''
            new_str30 = ''
            new_str40 = ''

            new_str50 = 'USBOutputFile "./7414v-103/low_version/{}/UpgradeFile.bin"'.format(dsn_ver)
            new_str60 = 'OTAOutputFile "./7414v-103/low_version/{}/UpgradeFile.ts"'.format(dsn_ver)

            modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                                 new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                                 new_str40, old_str50, new_str50, old_str60, new_str60)
            new_file_path = "./ekt_loader_tool-s-l-app-{}.cfg"
        elif dsn_ver == 1000 or dsn_ver == 1003:
            new_file_path = new_file_path.format(dsn_ver)
            new_str_1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 2'

            new_str3 = 'InputFile1 "4 vmlinux.bin 1 {}"'.format(vmlinux_ver)
            new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
            new_str20 = ''
            new_str30 = ''
            new_str40 = ''

            new_str50 = 'USBOutputFile "./7414v-103/same_version_app/{}/UpgradeFile.bin"'.format(dsn_ver)
            new_str60 = 'OTAOutputFile "./7414v-103/same_version_app/{}/UpgradeFile.ts"'.format(dsn_ver)

            modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                                 new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                                 new_str40, old_str50, new_str50, old_str60, new_str60)
            new_file_path = "./ekt_loader_tool-s-l-app-{}.cfg"


def make_bootlogo_file():
    new_str_dict = {1001: 1001, 1002: 1002, 1003: 1003, 1004: 1004, 1005: 1005, 20000: 20000, 989: 989, 990: 1000}
    old_file_path = "./ekt_loader_tool.cfg"
    new_file_path = "./ekt_loader_tool-bootlogo-{}.cfg"
    old_str1 = "DSN 1000"
    old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
    old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
    old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
    old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'

    old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAOutputFile "UpgradeFile.ts"'

    for dsn_ver, bootlogo_ver in new_str_dict.items():
        # for new_str1 in new_str_list:
        new_file_path = new_file_path.format(dsn_ver)
        new_str_1 = "DSN {}".format(dsn_ver)
        new_str2 = 'InputFileNumber 1'

        new_str3 = 'InputFile1 "6 bootlogo.bin 1 {}"'.format(bootlogo_ver)
        new_str4 = ''
        new_str20 = ''
        new_str30 = ''
        new_str40 = ''

        new_str50 = 'USBOutputFile "./7414v-103/{}/UpgradeFile.bin"'.format(dsn_ver)
        new_str60 = 'OTAOutputFile "./7414v-103/{}/UpgradeFile.ts"'.format(dsn_ver)

        modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                             new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                             new_str40, old_str50, new_str50, old_str60, new_str60)
        new_file_path = "./ekt_loader_tool-bootlogo-{}.cfg"

    print "streantool file Generate complete"


def make_same_low_bootlogo_file():
    new_str_dict = {999: 1001, 1001: 999, 1000: 1001, 1002: 1000, 1102: 1102, 1103: 1103, 1100: 1100, 1101: 1101}
    old_file_path = "./ekt_loader_tool.cfg"
    new_file_path = "./ekt_loader_tool-s-l-bootlogo-{}.cfg"
    old_str1 = "DSN 1000"
    old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
    old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
    old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
    old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'

    old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAOutputFile "UpgradeFile.ts"'

    for dsn_ver, bootlogo_ver in new_str_dict.items():
        # for new_str1 in new_str_list:
        if dsn_ver == 999 or dsn_ver == 1001:
            new_file_path = new_file_path.format(dsn_ver)
            new_str_1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "6 bootlogo.bin 1 {}"'.format(bootlogo_ver)
            new_str4 = ''
            new_str20 = ''
            new_str30 = ''
            new_str40 = ''

            new_str50 = 'USBOutputFile "./7414v-103/low_version/{}/UpgradeFile.bin"'.format(dsn_ver)
            new_str60 = 'OTAOutputFile "./7414v-103/low_version/{}/UpgradeFile.ts"'.format(dsn_ver)

            modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                                 new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                                 new_str40, old_str50, new_str50, old_str60, new_str60)
            new_file_path = "./ekt_loader_tool-s-l-bootlogo-{}.cfg"
        elif dsn_ver == 1000 or dsn_ver == 1002:
            new_file_path = new_file_path.format(dsn_ver)
            new_str_1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "6 bootlogo.bin 1 {}"'.format(bootlogo_ver)
            new_str4 = ''
            new_str20 = ''
            new_str30 = ''
            new_str40 = ''

            new_str50 = 'USBOutputFile "./7414v-103/same_version_bootlogo/{}/UpgradeFile.bin"'.format(dsn_ver)
            new_str60 = 'OTAOutputFile "./7414v-103/same_version_bootlogo/{}/UpgradeFile.ts"'.format(dsn_ver)

            modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                                 new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                                 new_str40, old_str50, new_str50, old_str60, new_str60)
            new_file_path = "./ekt_loader_tool-s-l-bootlogo-{}.cfg"
        elif dsn_ver == 1102:
            new_file_path = new_file_path.format(dsn_ver)
            new_str_1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "6 bootlogo_black_no_progress.bin 1 {}"'.format(bootlogo_ver)
            new_str4 = ''
            new_str20 = ''
            new_str30 = ''
            new_str40 = ''

            new_str50 = 'USBOutputFile "./7414v-103/bootlogo_black_no_progress/UpgradeFile.bin"'
            new_str60 = 'OTAOutputFile "./7414v-103/bootlogo_black_no_progress/UpgradeFile.ts"'

            modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                                 new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                                 new_str40, old_str50, new_str50, old_str60, new_str60)
            new_file_path = "./ekt_loader_tool-s-l-bootlogo-{}.cfg"
        elif dsn_ver == 1103:
            new_file_path = new_file_path.format(dsn_ver)
            new_str_1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "6 bootlogo_white.bin 1 {}"'.format(bootlogo_ver)
            new_str4 = ''
            new_str20 = ''
            new_str30 = ''
            new_str40 = ''

            new_str50 = 'USBOutputFile "./7414v-103/bootlogo_white//UpgradeFile.bin"'
            new_str60 = 'OTAOutputFile "./7414v-103/bootlogo_white//UpgradeFile.ts"'

            modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                                 new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                                 new_str40, old_str50, new_str50, old_str60, new_str60)
            new_file_path = "./ekt_loader_tool-s-l-bootlogo-{}.cfg"
        elif dsn_ver == 1100:
            new_file_path = new_file_path.format(dsn_ver)
            new_str_1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "7 loader_resource_black.bin 1 {}"'.format(bootlogo_ver)
            new_str4 = ''
            new_str20 = ''
            new_str30 = ''
            new_str40 = ''

            new_str50 = 'USBOutputFile "./7414v-103/loader_resource_black//UpgradeFile.bin"'
            new_str60 = 'OTAOutputFile "./7414v-103/loader_resource_black//UpgradeFile.ts"'

            modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                                 new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                                 new_str40, old_str50, new_str50, old_str60, new_str60)
            new_file_path = "./ekt_loader_tool-s-l-bootlogo-{}.cfg"
        elif dsn_ver == 1101:
            new_file_path = new_file_path.format(dsn_ver)
            new_str_1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "7 loader_resource_white.bin 1 {}"'.format(bootlogo_ver)
            new_str4 = ''
            new_str20 = ''
            new_str30 = ''
            new_str40 = ''

            new_str50 = 'USBOutputFile "./7414v-103/loader_resource_white//UpgradeFile.bin"'
            new_str60 = 'OTAOutputFile "./7414v-103/loader_resource_white//UpgradeFile.ts"'

            modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                                 new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                                 new_str40, old_str50, new_str50, old_str60, new_str60)
            new_file_path = "./ekt_loader_tool-s-l-bootlogo-{}.cfg"

    print "streantool file Generate complete"


def make_app_bootlogo_file():
    new_str_dict = {1011: [1001, 1001, 1001], 1012: [1002, 1002, 1002], 1013: [1003, 1003, 1003],
                    1014: [1004, 1004, 1004], 1015: [1005, 1005, 1005], 997: [1000, 1000, 1000], 987: [987, 987, 987],
                    992: [1000, 1000, 1000]}
    old_file_path = "./ekt_loader_tool.cfg"
    new_file_path = "./ekt_loader_tool-app-bootlogo-{}.cfg"
    old_str1 = "DSN 1000"
    old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
    old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
    old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
    old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'

    old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAOutputFile "UpgradeFile.ts"'

    for dsn_ver, [vmlinux_ver, fsi_ver, bootlogo_ver] in new_str_dict.items():
        new_file_path = new_file_path.format(dsn_ver)
        new_str_1 = "DSN {}".format(dsn_ver)
        new_str2 = 'InputFileNumber 3'

        new_str3 = 'InputFile1 "4 vmlinux.bin 1 {}"'.format(vmlinux_ver)
        new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
        new_str20 = 'InputFile3 "6 bootlogo.bin 1 {}"'.format(bootlogo_ver)
        new_str30 = ''
        new_str40 = ''

        new_str50 = 'USBOutputFile "./7414v-103/{}/UpgradeFile.bin"'.format(dsn_ver)
        new_str60 = 'OTAOutputFile "./7414v-103/{}/UpgradeFile.ts"'.format(dsn_ver)

        modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                             new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                             new_str40, old_str50, new_str50, old_str60, new_str60)
        new_file_path = "./ekt_loader_tool-app-bootlogo-{}.cfg"


def make_same_low_app_bootlogo_file():
    new_str_dict = {997: [1003, 1003, 1003], 1003: [997, 997, 997], 1000: [1003, 1003, 1003], 1004: [1000, 1000, 1000]}
    old_file_path = "./ekt_loader_tool.cfg"
    new_file_path = "./ekt_loader_tool-s-l-app-bootlogo-{}.cfg"
    old_str1 = "DSN 1000"
    old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
    old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
    old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
    old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'

    old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAOutputFile "UpgradeFile.ts"'

    for dsn_ver, [vmlinux_ver, fsi_ver, bootlogo_ver] in new_str_dict.items():
        if dsn_ver == 997 or dsn_ver == 1003:
            new_file_path = new_file_path.format(dsn_ver)
            new_str_1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 3'

            new_str3 = 'InputFile1 "4 vmlinux.bin 1 {}"'.format(vmlinux_ver)
            new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
            new_str20 = 'InputFile3 "6 bootlogo.bin 1 {}"'.format(bootlogo_ver)
            new_str30 = ''
            new_str40 = ''

            new_str50 = 'USBOutputFile "./7414v-103/low_version/{}/UpgradeFile.bin"'.format(dsn_ver)
            new_str60 = 'OTAOutputFile "./7414v-103/low_version/{}/UpgradeFile.ts"'.format(dsn_ver)

            modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                                 new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                                 new_str40, old_str50, new_str50, old_str60, new_str60)
            new_file_path = "./ekt_loader_tool-s-l-app-bootlogo-{}.cfg"
        elif dsn_ver == 1000 or dsn_ver == 1004:
            new_file_path = new_file_path.format(dsn_ver)
            new_str_1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 3'

            new_str3 = 'InputFile1 "4 vmlinux.bin 1 {}"'.format(vmlinux_ver)
            new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
            new_str20 = 'InputFile3 "6 bootlogo.bin 1 {}"'.format(bootlogo_ver)
            new_str30 = ''
            new_str40 = ''

            new_str50 = 'USBOutputFile "./7414v-103/same_version_app_bootlogo/{}/UpgradeFile.bin"'.format(dsn_ver)
            new_str60 = 'OTAOutputFile "./7414v-103/same_version_app_bootlogo/{}/UpgradeFile.ts"'.format(dsn_ver)

            modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                                 new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                                 new_str40, old_str50, new_str50, old_str60, new_str60)
            new_file_path = "./ekt_loader_tool-s-l-app-bootlogo-{}.cfg"


def make_incorrect_hardversion_app():
    new_str_dict = {15000: [15000, 15000]}
    old_file_path = "./ekt_loader_tool.cfg"
    new_file_path = "./ekt_loader_tool-incorrect-hardver-app.cfg"
    old_str1 = "DSN 1000"
    old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
    old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
    old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
    old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'

    old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAOutputFile "UpgradeFile.ts"'
    old_str70 = 'HardWareNo 18'

    for dsn_ver, [vmlinux_ver, fsi_ver] in new_str_dict.items():
        new_str_1 = "DSN {}".format(dsn_ver)
        new_str2 = 'InputFileNumber 2'

        new_str3 = 'InputFile1 "4 vmlinux.bin 1 {}"'.format(vmlinux_ver)
        new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
        new_str20 = ''
        new_str30 = ''
        new_str40 = ''

        new_str50 = 'USBOutputFile "./7414v-103/incorrect_hardware_app/UpgradeFile.bin"'
        new_str60 = 'OTAOutputFile "./7414v-103/incorrect_hardware_app/UpgradeFile.ts"'
        new_str70 = 'HardWareNo 99'

        modify_file_version10(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                              new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                              new_str40, old_str50, new_str50, old_str60, new_str60, old_str70, new_str70)
        new_file_path = "./ekt_loader_tool-incorrect-hardver-app.cfg"

    print "streantool file Generate complete"


def make_incorrect_hardversion_bootlogo():
    new_str_dict = {15000: 15000}
    old_file_path = "./ekt_loader_tool.cfg"
    new_file_path = "./ekt_loader_tool-incorrect-hardver-bootlogo.cfg"
    old_str1 = "DSN 1000"
    old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
    old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
    old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
    old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'

    old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAOutputFile "UpgradeFile.ts"'
    old_str70 = 'HardWareNo 18'

    for dsn_ver, bootlogo_ver in new_str_dict.items():
        # for new_str1 in new_str_list:
        new_str_1 = "DSN {}".format(dsn_ver)
        new_str2 = 'InputFileNumber 1'

        new_str3 = 'InputFile1 "6 bootlogo.bin 1 {}"'.format(bootlogo_ver)
        new_str4 = ''
        new_str20 = ''
        new_str30 = ''
        new_str40 = ''

        new_str50 = 'USBOutputFile "./7414v-103/incorrect_hardware_bootlogo/UpgradeFile.bin"'
        new_str60 = 'OTAOutputFile "./7414v-103/incorrect_hardware_bootlogo/UpgradeFile.ts"'
        new_str70 = 'HardWareNo 99'

        modify_file_version10(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                              new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                              new_str40, old_str50, new_str50, old_str60, new_str60, old_str70, new_str70)
        new_file_path = "./ekt_loader_tool-incorrect-hardver-bootlogo.cfg"

    print "streantool file Generate complete"


def make_incorrect_oui_app():
    new_str_dict = {15000: [15000, 15000]}
    old_file_path = "./ekt_loader_tool.cfg"
    new_file_path = "./ekt_loader_tool-incorrect-oui-app.cfg"
    old_str1 = "DSN 1000"
    old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
    old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
    old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
    old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'

    old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAOutputFile "UpgradeFile.ts"'
    old_str70 = 'ManuCode 13416689'

    for dsn_ver, [vmlinux_ver, fsi_ver] in new_str_dict.items():
        new_str_1 = "DSN {}".format(dsn_ver)
        new_str2 = 'InputFileNumber 2'

        new_str3 = 'InputFile1 "4 vmlinux.bin 1 {}"'.format(vmlinux_ver)
        new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
        new_str20 = ''
        new_str30 = ''
        new_str40 = ''

        new_str50 = 'USBOutputFile "./7414v-103/incorrect_oui_app/UpgradeFile.bin"'
        new_str60 = 'OTAOutputFile "./7414v-103/incorrect_oui_app/UpgradeFile.ts"'
        new_str70 = 'ManuCode 99999999'

        modify_file_version10(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                              new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                              new_str40, old_str50, new_str50, old_str60, new_str60, old_str70, new_str70)
        new_file_path = "./ekt_loader_tool-incorrect-oui-app.cfg"

    print "streantool file Generate complete"


def make_incorrect_oui_bootlogo():
    new_str_dict = {15000: 15000}
    old_file_path = "./ekt_loader_tool.cfg"
    new_file_path = "./ekt_loader_tool-incorrect-oui-bootlogo.cfg"
    old_str1 = "DSN 1000"
    old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
    old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
    old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
    old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'

    old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAOutputFile "UpgradeFile.ts"'
    old_str70 = 'ManuCode 13416689'

    for dsn_ver, bootlogo_ver in new_str_dict.items():
        # for new_str1 in new_str_list:
        new_str_1 = "DSN {}".format(dsn_ver)
        new_str2 = 'InputFileNumber 1'

        new_str3 = 'InputFile1 "6 bootlogo.bin 1 {}"'.format(bootlogo_ver)
        new_str4 = ''
        new_str20 = ''
        new_str30 = ''
        new_str40 = ''

        new_str50 = 'USBOutputFile "./7414v-103/incorrect_oui_bootlogo/UpgradeFile.bin"'
        new_str60 = 'OTAOutputFile "./7414v-103/incorrect_oui_bootlogo/UpgradeFile.ts"'
        new_str70 = 'ManuCode 99999999'

        modify_file_version10(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                              new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                              new_str40, old_str50, new_str50, old_str60, new_str60, old_str70, new_str70)
        new_file_path = "./ekt_loader_tool-incorrect-oui-bootlogo.cfg"

    print "streantool file Generate complete"


def make_unsigend_app():
    old_file_path = "./streamtool.cfg"
    new_file_path = "./streamtool-unsigned-app.cfg"

    old_str1 = "SoftWareNo 1016"
    old_str20 = 'USBOutputFile "UpgradeFile.bin"'
    old_str30 = 'OTAOutputFile "UpgradeFile.ts"'

    new_str_1 = "SoftWareNo 15000"
    new_str20 = 'USBOutputFile "./7414-v2/unsigned_application/UpgradeFile.bin"'
    new_str30 = 'OTAOutputFile "./7414-v2/unsigned_application/UpgradeFile.ts"'

    modify_file_version1(old_file_path, new_file_path, old_str1, str(new_str_1), old_str20, new_str20, old_str30,
                         new_str30)


def make_wrong_sigend_app():
    new_str_dict = {15000: [15000, 15000]}
    old_file_path = "./ekt_loader_tool.cfg"
    new_file_path = "./ekt_loader_tool-wrong-signed-app.cfg"
    old_str1 = "DSN 1000"
    old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
    old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
    old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
    old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'

    old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAOutputFile "UpgradeFile.ts"'
    old_str70 = 'AppRSAPrivateKey "app_privatekey.bin"'

    for dsn_ver, [vmlinux_ver, fsi_ver] in new_str_dict.items():
        new_str_1 = "DSN {}".format(dsn_ver)
        new_str2 = 'InputFileNumber 2'

        new_str3 = 'InputFile1 "4 vmlinux.bin 1 {}"'.format(vmlinux_ver)
        new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
        new_str20 = ''
        new_str30 = ''
        new_str40 = ''

        new_str50 = 'USBOutputFile "./7414v-103/wrong_signed_application/UpgradeFile.bin"'
        new_str60 = 'OTAOutputFile "./7414v-103/wrong_signed_application/UpgradeFile.ts"'
        new_str70 = 'AppRSAPrivateKey "privatekey.bin"'

        modify_file_version10(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                              new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                              new_str40, old_str50, new_str50, old_str60, new_str60, old_str70, new_str70)
        new_file_path = "./ekt_loader_tool-wrong-signed-app.cfg"

    print "streantool file Generate complete"


def make_unsigned_app_bootlogo():
    old_file_path = "./streamtool.cfg"
    new_file_path = "./streamtool-unsigned-app_bootlogo.cfg"
    old_str1 = "SoftWareNo 1016"
    old_str2 = "LogoVer 0"
    old_str3 = 'InputFile1 "1 upgrade_image.bin"'
    old_str20 = 'USBOutputFile "UpgradeFile.bin"'
    old_str30 = 'OTAOutputFile "UpgradeFile.ts"'

    new_str_1 = "SoftWareNo 15000"
    new_str_2 = "LogoVer 15000"
    new_str_3 = 'InputFile1 "3 upgrade_image.bin"'
    new_str20 = 'USBOutputFile "./7414-v2/unisgned_application_bootlogo/UpgradeFile.bin"'
    new_str30 = 'OTAOutputFile "./7414-v2/unisgned_application_bootlogo/UpgradeFile.ts"'

    modify_file_version3(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str_2, old_str3,
                         new_str_3, old_str20, new_str20, old_str30, new_str30)

    print "streantool file Generate complete"


def make_incorrect_manufacturedes_app():
    new_str_dict = {15000: [15000, 15000]}
    old_file_path = "./ekt_loader_tool.cfg"
    new_file_path = "./ekt_loader_tool-incorrect-manufacturedes-app.cfg"
    old_str1 = "DSN 1000"
    old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
    old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
    old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
    old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'

    old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAOutputFile "UpgradeFile.ts"'
    old_str70 = 'ManufactureDes "EKT"'

    for dsn_ver, [vmlinux_ver, fsi_ver] in new_str_dict.items():
        new_str_1 = "DSN {}".format(dsn_ver)
        new_str2 = 'InputFileNumber 2'

        new_str3 = 'InputFile1 "4 vmlinux.bin 1 {}"'.format(vmlinux_ver)
        new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
        new_str20 = ''
        new_str30 = ''
        new_str40 = ''

        new_str50 = 'USBOutputFile "./7414v-103/incorrect_manuf_application/UpgradeFile.bin"'
        new_str60 = 'OTAOutputFile "./7414v-103/incorrect_manuf_application/UpgradeFile.ts"'
        new_str70 = 'ManufactureDes "KKK111"'

        modify_file_version10(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                              new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                              new_str40, old_str50, new_str50, old_str60, new_str60, old_str70, new_str70)
        new_file_path = "./ekt_loader_tool-incorrect-manufacturedes-app.cfg"

    print "streantool file Generate complete"


def make_incorrect_manufacturedes_bootlogo():
    new_str_dict = {15000: 15000}
    old_file_path = "./ekt_loader_tool.cfg"
    new_file_path = "./ekt_loader_tool-incorrect-manufacturedes-bootlogo.cfg"
    old_str1 = "DSN 1000"
    old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
    old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
    old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
    old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'

    old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAOutputFile "UpgradeFile.ts"'
    old_str70 = 'ManufactureDes "EKT"'

    for dsn_ver, bootlogo_ver in new_str_dict.items():
        # for new_str1 in new_str_list:
        new_str_1 = "DSN {}".format(dsn_ver)
        new_str2 = 'InputFileNumber 1'

        new_str3 = 'InputFile1 "6 bootlogo.bin 1 {}"'.format(bootlogo_ver)
        new_str4 = ''
        new_str20 = ''
        new_str30 = ''
        new_str40 = ''

        new_str50 = 'USBOutputFile "./7414v-103/incorrect_manufacturedes_bootlogo/UpgradeFile.bin"'
        new_str60 = 'OTAOutputFile "./7414v-103/incorrect_manufacturedes_bootlogo/UpgradeFile.ts"'
        new_str70 = 'ManufactureDes "KKK111"'

        modify_file_version10(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                              new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                              new_str40, old_str50, new_str50, old_str60, new_str60, old_str70, new_str70)
        new_file_path = "./ekt_loader_tool-incorrect-manufacturedes-bootlogo.cfg"

    print "streantool file Generate complete"


def make_incorrect_machinedes_app():
    new_str_dict = {15000: [15000, 15000]}
    old_file_path = "./ekt_loader_tool.cfg"
    new_file_path = "./ekt_loader_tool-incorrect-machinedes-app.cfg"
    old_str1 = "DSN 1000"
    old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
    old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
    old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
    old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'

    old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAOutputFile "UpgradeFile.ts"'
    old_str70 = 'ModelNo "DSN7414v"'

    for dsn_ver, [vmlinux_ver, fsi_ver] in new_str_dict.items():
        new_str_1 = "DSN {}".format(dsn_ver)
        new_str2 = 'InputFileNumber 2'

        new_str3 = 'InputFile1 "4 vmlinux.bin 1 {}"'.format(vmlinux_ver)
        new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
        new_str20 = ''
        new_str30 = ''
        new_str40 = ''

        new_str50 = 'USBOutputFile "./7414v-103/incorrect_machinedes_application/UpgradeFile.bin"'
        new_str60 = 'OTAOutputFile "./7414v-103/incorrect_machinedes_application/UpgradeFile.ts"'
        new_str70 = 'ModelNo "DSN7414v111"'

        modify_file_version10(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                              new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                              new_str40, old_str50, new_str50, old_str60, new_str60, old_str70, new_str70)
        new_file_path = "./ekt_loader_tool-incorrect-machinedes-app.cfg"

    print "streantool file Generate complete"


def make_incorrect_machinedes_bootlogo():
    new_str_dict = {15000: 15000}
    old_file_path = "./ekt_loader_tool.cfg"
    new_file_path = "./ekt_loader_tool-incorrect-machinedes-bootlogo.cfg"
    old_str1 = "DSN 1000"
    old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
    old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
    old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
    old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'

    old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAOutputFile "UpgradeFile.ts"'
    old_str70 = 'ModelNo "DSN7414v"'

    for dsn_ver, bootlogo_ver in new_str_dict.items():
        # for new_str1 in new_str_list:
        new_str_1 = "DSN {}".format(dsn_ver)
        new_str2 = 'InputFileNumber 1'

        new_str3 = 'InputFile1 "6 bootlogo.bin 1 {}"'.format(bootlogo_ver)
        new_str4 = ''
        new_str20 = ''
        new_str30 = ''
        new_str40 = ''

        new_str50 = 'USBOutputFile "./7414v-103/incorrect_machinedes_bootlogo/UpgradeFile.bin"'
        new_str60 = 'OTAOutputFile "./7414v-103/incorrect_machinedes_bootlogo/UpgradeFile.ts"'
        new_str70 = 'ModelNo "DSN7414v111"'

        modify_file_version10(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                              new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                              new_str40, old_str50, new_str50, old_str60, new_str60, old_str70, new_str70)
        new_file_path = "./ekt_loader_tool-incorrect-machinedes-bootlogo.cfg"

    print "streantool file Generate complete"


def make_downloadpid_1030_tableid_1_app():
    new_str_dict = {15000: [15000, 15000]}
    old_file_path = "./ekt_loader_tool.cfg"
    new_file_path = "./ekt_loader_tool-downloadpid-1030-tableid-1-app.cfg"
    old_str1 = "DSN 1000"
    old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
    old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
    old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
    old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'

    old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAOutputFile "UpgradeFile.ts"'
    old_str70 = 'DownloadPID 1026'
    old_str80 = 'TableID 0'

    for dsn_ver, [vmlinux_ver, fsi_ver] in new_str_dict.items():
        new_str_1 = "DSN {}".format(dsn_ver)
        new_str2 = 'InputFileNumber 2'

        new_str3 = 'InputFile1 "4 vmlinux.bin 1 {}"'.format(vmlinux_ver)
        new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
        new_str20 = ''
        new_str30 = ''
        new_str40 = ''

        new_str50 = 'USBOutputFile "./7414v-103/downloadpid_1030_tableid_1/UpgradeFile.bin"'
        new_str60 = 'OTAOutputFile "./7414v-103/downloadpid_1030_tableid_1/UpgradeFile.ts"'
        new_str70 = 'DownloadPID 1030'
        new_str80 = 'TableID 1'

        modify_file_version11(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                              new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                              new_str40, old_str50, new_str50, old_str60, new_str60, old_str70, new_str70, old_str80,
                              new_str80)
        new_file_path = "./ekt_loader_tool-downloadpid-1030-tableid-1-app.cfg"

    print "streantool file Generate complete"


def make_dsi_crc_app():
    new_str_dict = {15000: [15000, 15000]}
    old_file_path = "./ekt_loader_tool.cfg"
    new_file_path = "./ekt_loader_tool-dsi-crc-app.cfg"
    old_str1 = "DSN 1000"
    old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
    old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
    old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
    old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'

    old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAOutputFile "UpgradeFile.ts"'
    old_str70 = 'DSI_CRC_Error_Test_Flag 0'

    for dsn_ver, [vmlinux_ver, fsi_ver] in new_str_dict.items():
        new_str_1 = "DSN {}".format(dsn_ver)
        new_str2 = 'InputFileNumber 2'

        new_str3 = 'InputFile1 "4 vmlinux.bin 1 {}"'.format(vmlinux_ver)
        new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
        new_str20 = ''
        new_str30 = ''
        new_str40 = ''

        new_str50 = 'USBOutputFile "./7414v-103/dsi_crc/UpgradeFile.bin"'
        new_str60 = 'OTAOutputFile "./7414v-103/dsi_crc/UpgradeFile.ts"'
        new_str70 = 'DSI_CRC_Error_Test_Flag 1'

        modify_file_version10(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                              new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                              new_str40, old_str50, new_str50, old_str60, new_str60, old_str70, new_str70)
        new_file_path = "./ekt_loader_tool-dsi-crc-app.cfg"

    print "streantool file Generate complete"


def make_dii_crc_app():
    new_str_dict = {15000: [15000, 15000]}
    old_file_path = "./ekt_loader_tool.cfg"
    new_file_path = "./ekt_loader_tool-dii-crc-app.cfg"
    old_str1 = "DSN 1000"
    old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
    old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
    old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
    old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'

    old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAOutputFile "UpgradeFile.ts"'
    old_str70 = 'DII_CRC_Error_Test_Flag 0'

    for dsn_ver, [vmlinux_ver, fsi_ver] in new_str_dict.items():
        new_str_1 = "DSN {}".format(dsn_ver)
        new_str2 = 'InputFileNumber 2'

        new_str3 = 'InputFile1 "4 vmlinux.bin 1 {}"'.format(vmlinux_ver)
        new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
        new_str20 = ''
        new_str30 = ''
        new_str40 = ''

        new_str50 = 'USBOutputFile "./7414v-103/dii_crc/UpgradeFile.bin"'
        new_str60 = 'OTAOutputFile "./7414v-103/dii_crc/UpgradeFile.ts"'
        new_str70 = 'DII_CRC_Error_Test_Flag 1'

        modify_file_version10(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                              new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                              new_str40, old_str50, new_str50, old_str60, new_str60, old_str70, new_str70)
        new_file_path = "./ekt_loader_tool-dii-crc-app.cfg"

    print "streantool file Generate complete"


def make_ddb_crc_app():
    new_str_dict = {15000: [15000, 15000]}
    old_file_path = "./ekt_loader_tool.cfg"
    new_file_path = "./ekt_loader_tool-ddb-crc-app.cfg"
    old_str1 = "DSN 1000"
    old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
    old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
    old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
    old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'

    old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAOutputFile "UpgradeFile.ts"'
    old_str70 = 'DDB_CRC_Error_Test_Flag 0'

    for dsn_ver, [vmlinux_ver, fsi_ver] in new_str_dict.items():
        new_str_1 = "DSN {}".format(dsn_ver)
        new_str2 = 'InputFileNumber 2'

        new_str3 = 'InputFile1 "4 vmlinux.bin 1 {}"'.format(vmlinux_ver)
        new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
        new_str20 = ''
        new_str30 = ''
        new_str40 = ''

        new_str50 = 'USBOutputFile "./7414v-103/ddb_crc/UpgradeFile.bin"'
        new_str60 = 'OTAOutputFile "./7414v-103/ddb_crc/UpgradeFile.ts"'
        new_str70 = 'DDB_CRC_Error_Test_Flag 1'

        modify_file_version10(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                              new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                              new_str40, old_str50, new_str50, old_str60, new_str60, old_str70, new_str70)
        new_file_path = "./ekt_loader_tool-ddb-crc-app.cfg"

    print "streantool file Generate complete"


def make_downloadheader_crc_app():
    new_str_dict = {15000: [15000, 15000]}
    old_file_path = "./ekt_loader_tool.cfg"
    new_file_path = "./ekt_loader_tool-downloadheader-crc-app.cfg"
    old_str1 = "DSN 1000"
    old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
    old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
    old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
    old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'

    old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAOutputFile "UpgradeFile.ts"'
    old_str70 = 'DownloadHeader_CRC_Error_Test_Flag 0'

    for dsn_ver, [vmlinux_ver, fsi_ver] in new_str_dict.items():
        new_str_1 = "DSN {}".format(dsn_ver)
        new_str2 = 'InputFileNumber 2'

        new_str3 = 'InputFile1 "4 vmlinux.bin 1 {}"'.format(vmlinux_ver)
        new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
        new_str20 = ''
        new_str30 = ''
        new_str40 = ''

        new_str50 = 'USBOutputFile "./7414v-103/downloadheader_crc/UpgradeFile.bin"'
        new_str60 = 'OTAOutputFile "./7414v-103/downloadheader_crc/UpgradeFile.ts"'
        new_str70 = 'DownloadHeader_CRC_Error_Test_Flag 1'

        modify_file_version10(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                              new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                              new_str40, old_str50, new_str50, old_str60, new_str60, old_str70, new_str70)
        new_file_path = "./ekt_loader_tool-downloadheader-crc-app.cfg"

    print "streantool file Generate complete"


def make_big_file_app():
    new_str_dict = {10000: [10000, 10000]}
    old_file_path = "./ekt_loader_tool.cfg"
    new_file_path = "./ekt_loader_tool-big-app.cfg"
    old_str1 = "DSN 1000"
    old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
    old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
    old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
    old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'

    old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAOutputFile "UpgradeFile.ts"'

    for dsn_ver, [vmlinux_ver, fsi_ver] in new_str_dict.items():
        new_str_1 = "DSN {}".format(dsn_ver)
        new_str2 = 'InputFileNumber 2'

        new_str3 = 'InputFile1 "4 vmlinux.bin 1 {}"'.format(vmlinux_ver)
        new_str4 = 'InputFile2 "5 big_app_size.bin 1 {}"'.format(fsi_ver)
        new_str20 = ''
        new_str30 = ''
        new_str40 = ''

        new_str50 = 'USBOutputFile "./7414v-103/big_app_size/UpgradeFile.bin"'
        new_str60 = 'OTAOutputFile "./7414v-103/big_app_size/UpgradeFile.ts"'

        modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                             new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                             new_str40, old_str50, new_str50, old_str60, new_str60)
        new_file_path = "./ekt_loader_tool-big-app.cfg"
    print "streantool file Generate complete"


def make_excessive_big_file_app():
    new_str_dict = {10003: [10003, 10003]}
    old_file_path = "./ekt_loader_tool.cfg"
    new_file_path = "./ekt_loader_tool-excessive-big-app.cfg"
    old_str1 = "DSN 1000"
    old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
    old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
    old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
    old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'

    old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAOutputFile "UpgradeFile.ts"'

    for dsn_ver, [vmlinux_ver, fsi_ver] in new_str_dict.items():
        new_str_1 = "DSN {}".format(dsn_ver)
        new_str2 = 'InputFileNumber 2'

        new_str3 = 'InputFile1 "4 vmlinux.bin 1 {}"'.format(vmlinux_ver)
        new_str4 = 'InputFile2 "5 excessive_big_app_size.bin 1 {}"'.format(fsi_ver)
        new_str20 = ''
        new_str30 = ''
        new_str40 = ''

        new_str50 = 'USBOutputFile "./7414v-103/excessive_big_app_size/UpgradeFile.bin"'
        new_str60 = 'OTAOutputFile "./7414v-103/excessive_big_app_size/UpgradeFile.ts"'

        modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                             new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                             new_str40, old_str50, new_str50, old_str60, new_str60)
        new_file_path = "./ekt_loader_tool-excessive-big-app.cfg"
    print "streantool file Generate complete"


def make_big_bootlogo_file():
    new_str_dict = {10001: 10001}
    old_file_path = "./ekt_loader_tool.cfg"
    new_file_path = "./ekt_loader_tool-big-bootlogo.cfg"
    old_str1 = "DSN 1000"
    old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
    old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
    old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
    old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'

    old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAOutputFile "UpgradeFile.ts"'

    for dsn_ver, bootlogo_ver in new_str_dict.items():
        # for new_str1 in new_str_list:
        new_str_1 = "DSN {}".format(dsn_ver)
        new_str2 = 'InputFileNumber 1'

        new_str3 = 'InputFile1 "6 big_bootlogo_size.bin 1 {}"'.format(bootlogo_ver)
        new_str4 = ''
        new_str20 = ''
        new_str30 = ''
        new_str40 = ''

        new_str50 = 'USBOutputFile "./7414v-103/big_bootlogo_size/UpgradeFile.bin"'
        new_str60 = 'OTAOutputFile "./7414v-103/big_bootlogo_size/UpgradeFile.ts"'

        modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                             new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                             new_str40, old_str50, new_str50, old_str60, new_str60)
        new_file_path = "./ekt_loader_tool-big-bootlogo.cfg"

    print "streantool file Generate complete"


def make_excessive_big_bootlogo_file():
    new_str_dict = {10004: 10004}
    old_file_path = "./ekt_loader_tool.cfg"
    new_file_path = "./ekt_loader_tool-excessive-big-bootlogo.cfg"
    old_str1 = "DSN 1000"
    old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
    old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
    old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
    old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'

    old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAOutputFile "UpgradeFile.ts"'

    for dsn_ver, bootlogo_ver in new_str_dict.items():
        # for new_str1 in new_str_list:
        new_str_1 = "DSN {}".format(dsn_ver)
        new_str2 = 'InputFileNumber 1'

        new_str3 = 'InputFile1 "6 excessive_big_bootlogo_size.bin 1 {}"'.format(bootlogo_ver)
        new_str4 = ''
        new_str20 = ''
        new_str30 = ''
        new_str40 = ''

        new_str50 = 'USBOutputFile "./7414v-103/excessive_big_bootlogo_size/UpgradeFile.bin"'
        new_str60 = 'OTAOutputFile "./7414v-103/excessive_big_bootlogo_size/UpgradeFile.ts"'

        modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                             new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                             new_str40, old_str50, new_str50, old_str60, new_str60)
        new_file_path = "./ekt_loader_tool-excessive-big-bootlogo.cfg"

    print "streantool file Generate complete"


def make_big_app_bootlogo_size():
    new_str_dict = {10002: [10002, 10002, 10002]}
    old_file_path = "./ekt_loader_tool.cfg"
    new_file_path = "./ekt_loader_tool-big-app-bootlogo.cfg"
    old_str1 = "DSN 1000"
    old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
    old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
    old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
    old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'

    old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAOutputFile "UpgradeFile.ts"'

    for dsn_ver, [vmlinux_ver, fsi_ver, bootlogo_ver] in new_str_dict.items():
        new_str_1 = "DSN {}".format(dsn_ver)
        new_str2 = 'InputFileNumber 3'

        new_str3 = 'InputFile1 "4 vmlinux.bin 1 {}"'.format(vmlinux_ver)
        new_str4 = 'InputFile2 "5 big_app_size.bin 1 {}"'.format(fsi_ver)
        new_str20 = 'InputFile3 "6 big_bootlogo_size.bin 1 {}"'.format(bootlogo_ver)
        new_str30 = ''
        new_str40 = ''

        new_str50 = 'USBOutputFile "./7414v-103/big_app_bootlogo_size/UpgradeFile.bin"'
        new_str60 = 'OTAOutputFile "./7414v-103/big_app_bootlogo_size/UpgradeFile.ts"'

        modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                             new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                             new_str40, old_str50, new_str50, old_str60, new_str60)
        new_file_path = "./ekt_loader_tool-big-app-bootlogo.cfg"


def create_folder(folder_name):
    """
    base current floder, creat folder
    :param folder_name: folder name (str)
    :return: None
    """
    curPath = os.getcwd()
    tempPath = folder_name
    targetPath = curPath + os.path.sep + tempPath
    if not os.path.exists(targetPath):
        os.makedirs(targetPath)
    else:
        print "file already exists!"


if __name__ == '__main__':
    create_folder("./7414v-103")
    create_folder("./7414v-103/1001")
    create_folder("./7414v-103/1002")
    create_folder("./7414v-103/1003")
    create_folder("./7414v-103/1004")
    create_folder("./7414v-103/1005")
    create_folder("./7414v-103/20000")
    # create_folder("./7414v-103/999")
    create_folder("./7414v-103/1006")
    create_folder("./7414v-103/1007")
    create_folder("./7414v-103/1008")
    create_folder("./7414v-103/1009")
    create_folder("./7414v-103/1010")
    create_folder("./7414v-103/20001")
    # create_folder("./7414v-103/998")
    create_folder("./7414v-103/1011")
    create_folder("./7414v-103/1012")
    create_folder("./7414v-103/1013")
    create_folder("./7414v-103/1014")
    create_folder("./7414v-103/1015")
    create_folder("./7414v-103/989")
    create_folder("./7414v-103/990")
    create_folder("./7414v-103/988")
    create_folder("./7414v-103/991")
    create_folder("./7414v-103/987")
    create_folder("./7414v-103/992")
    # create_folder("./7414v-103/997")
    create_folder("./7414v-103/incorrect_hardware_app")
    create_folder("./7414v-103/incorrect_hardware_bootlogo")
    create_folder("./7414v-103/incorrect_oui_app")
    create_folder("./7414v-103/incorrect_oui_bootlogo")
    create_folder("./7414v-103/unisgned_application_bootlogo")
    create_folder("./7414v-103/unsigned_application")
    create_folder("./7414v-103/wrong_signed_application")
    create_folder("./7414v-103/incorrect_manuf_application")
    create_folder("./7414v-103/incorrect_manufacturedes_bootlogo")
    create_folder("./7414v-103/incorrect_machinedes_application")
    create_folder("./7414v-103/incorrect_machinedes_bootlogo")
    create_folder("./7414v-103/big_app_size")
    create_folder("./7414v-103/big_bootlogo_size")
    create_folder("./7414v-103/big_app_bootlogo_size")
    create_folder("./7414v-103/excessive_big_app_size")
    create_folder("./7414v-103/excessive_big_bootlogo_size")
    create_folder("./7414v-103/downloadpid_1030_tableid_1")
    create_folder("./7414v-103/dsi_crc")
    create_folder("./7414v-103/dii_crc")
    create_folder("./7414v-103/ddb_crc")
    create_folder("./7414v-103/downloadheader_crc")
    create_folder("./7414v-103/low_version")
    create_folder("./7414v-103/low_version/997")
    create_folder("./7414v-103/low_version/998")
    create_folder("./7414v-103/low_version/999")
    create_folder("./7414v-103/low_version/1001")
    create_folder("./7414v-103/low_version/1002")
    create_folder("./7414v-103/low_version/1003")
    create_folder("./7414v-103/same_version_bootlogo")
    create_folder("./7414v-103/same_version_bootlogo/1000")
    create_folder("./7414v-103/same_version_bootlogo/1002")
    create_folder("./7414v-103/same_version_app")
    create_folder("./7414v-103/same_version_app/1000")
    create_folder("./7414v-103/same_version_app/1003")
    create_folder("./7414v-103/same_version_app_bootlogo")
    create_folder("./7414v-103/same_version_app_bootlogo/1000")
    create_folder("./7414v-103/same_version_app_bootlogo/1004")
    create_folder("./7414v-103/loader_resource_black")
    create_folder("./7414v-103/loader_resource_white")
    create_folder("./7414v-103/bootlogo_black_no_progress")
    create_folder("./7414v-103/bootlogo_white")

    make_app_file()
    make_bootlogo_file()
    make_app_bootlogo_file()
    make_incorrect_hardversion_app()
    make_incorrect_hardversion_bootlogo()
    make_incorrect_oui_app()
    make_incorrect_oui_bootlogo()
    # make_unsigend_app()
    # make_unsigned_app_bootlogo()
    make_incorrect_manufacturedes_app()
    make_incorrect_manufacturedes_bootlogo()
    make_incorrect_machinedes_app()
    make_incorrect_machinedes_bootlogo()
    make_downloadpid_1030_tableid_1_app()
    make_dsi_crc_app()
    make_dii_crc_app()
    make_ddb_crc_app()
    make_downloadheader_crc_app()
    make_big_file_app()
    make_excessive_big_file_app()
    make_big_bootlogo_file()
    make_excessive_big_bootlogo_file()
    make_big_app_bootlogo_size()
    make_wrong_sigend_app()
    make_same_low_bootlogo_file()
    make_same_low_app_file()
    make_same_low_app_bootlogo_file()
