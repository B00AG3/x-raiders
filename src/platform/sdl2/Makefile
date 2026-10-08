SRCS=main.cpp \
     ../../libs/stb_vorbis/stb_vorbis.c \
     ../../libs/minimp3/minimp3.cpp \
     ../../libs/tinf/tinflate.c
CC=g++

SDL_CFLAGS := $(shell sdl2-config --cflags)
SDL_LDFLAGS := $(shell sdl2-config --libs)

CFLAGS+=-DSDL2_GLES -D_GAPI_GLES2 -std=c++11 -O3 -fno-exceptions -fno-rtti -ffunction-sections -fdata-sections -Wl,--gc-sections -D__SDL2__ $(SDL_CFLAGS) -Wall
LDFLAGS+=-lGLESv2 -lEGL -lm -lrt -lpthread -lasound -ludev $(SDL_LDFLAGS)

INCLUDES+=-I../../

x-raiders :
	$(CC) $(INCLUDES) $(CFLAGS) $(LDFLAGS) $(SRCS) -o $@

install : x-raiders
	install -d $(DESTDIR)$(PREFIX)/bin/
	install x-raiders $(DESTDIR)$(PREFIX)/bin/X-Raiders

uninstall :
	rm -f $(DESTDIR)$(PREFIX)/bin/X-Raiders

clean:
	rm -f X-Raiders

