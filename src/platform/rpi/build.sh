set -e
clang++ -std=c++11 -Os -s -g -fno-exceptions -fno-rtti -ffunction-sections -fdata-sections -Wl,--gc-sections -Wno-invalid-source-encoding -DNDEBUG -D__RPI__ main.cpp ../../libs/stb_vorbis/stb_vorbis.c ../../libs/minimp3/minimp3.cpp ../../libs/tinf/tinflate.c -I/opt/vc/include -I../../ -o../../../bin/X-Raiders -L/opt/vc/lib/ -lbrcmGLESv2 -lbrcmEGL -lm -lrt -lpthread -lasound -lbcm_host -ludev
strip ../../../bin/X-Raiders --strip-all --remove-section=.comment --remove-section=.note
