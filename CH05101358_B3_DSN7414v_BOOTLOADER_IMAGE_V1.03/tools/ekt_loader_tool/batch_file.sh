#!/usr/bin/env bash
python generate_file_streamtool.py
cd ./make_big_file/
python ./generate_file_cut_size.py
cd ../
./ekt_loader_tool ekt_loader_tool-999-999.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-999-1000.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-999-1001.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-1000-999.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-1000-1000.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-1000-1001.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-1001-999.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-1001-1000.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-1001-1001.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-65535-65535.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-20000-20000.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-30000-30000.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-40000-40000.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-big.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-ddb-crc.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-dii-crc.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-downloadheader-crc.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-downloadpid-1030-tableid-1.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-dsi-crc.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-excessive-big.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-incorrect-hardver.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-incorrect-machinedes.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-incorrect-manufacturedes.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-incorrect-oui.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-specil-1100.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-specil-1101.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-specil-1102.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-specil-1103.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-specil-1104.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-specil-1200.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-specil-1201.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-specil-1202.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-specil-1203.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-specil-1204.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-specil-1205.cfg  << EOF
1
EOF
./ekt_loader_tool ekt_loader_tool-wrong-signed.cfg  << EOF
1
EOF