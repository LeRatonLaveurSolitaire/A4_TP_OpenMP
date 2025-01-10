CC=gcc
CCFLAGS=-Wall -std=c99 -fopenmp -O3
LDFLAGS=-lm -fopenmp
SOURCES=$(wildcard *.c)
OBJECTS=$(SOURCES:.c=.o)
TARGET=ShiTomasi

CXX = gcc

exo1 :
	$(CXX) $(CFLAGS) exo1.c -o exo1

exo2 :
	$(CXX) $(CFLAGS) -lm exo2.c -o exo2

all: debug

debug: CCFLAGS += -DDEBUG -g
debug: $(TARGET)

release: CCFLAGS += -O2
release: $(TARGET)

benchmode: CCFLAGS += -O2 -DBENCHMARKMODE
benchmode: $(TARGET)

$(TARGET): $(OBJECTS) $(CXXOBJECTS)
	$(CC) -o $@ $^ $(LDFLAGS)

%.o: %.c %.h
	$(CC) $(CCFLAGS) -c $<

%.o: %.c
	$(CC) $(CCFLAGS) -c $<

clean:
	rm -f *.pgm *.o $(TARGET)