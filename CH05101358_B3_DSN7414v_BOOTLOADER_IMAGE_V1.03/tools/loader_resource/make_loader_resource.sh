###################################################################
#command format：AddConfig Iframe_name SW_Version Search_Type Language Loader_Style
#
#Search_Type:1=DVBC   2=DVBT  3=DVBS
#
#Language:
#English=0;Polish =1;Russian=2;German=3;French=4;Spanish=5;
#Italian=6;Portuguese=7;Turkish=8;Arabic=9;Persian=10;Thai=11;
#Serbin=12;Czech=13;Slovak=14;Montenegrin=15;Albanian=16;Croatian=17;
#
#Loader_Style:0=Unified; 1=Black
#
###################################################################
./AddConfig ekt_logo.m2v 100 3 0 1
./AddMac image_config.bin
mv image_Mac.bin loader_resource.bin
rm image_config.bin