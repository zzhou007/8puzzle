CFLAGS = -Wall -Werror -ansi -pedantic -o

all:
	mkdir bin; \
    cd src; \
    g++ $(CFLAGS) puzzle 8puzzle.cpp; \
    cd -; \

puzzle: src/8puzzle.cpp
	cd src; \
    g++ $(CFLAGS) puzzle 8puzzle.cpp; \
    cd -; \

clean:
	rm -rf bin
