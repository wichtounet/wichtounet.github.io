.PHONY: default clean related_test related_all

default: generate

generate: generate.cpp
	clang++ -g -Ofast -march=native -std=c++11 -o generate generate.cpp

related_all: generate
	./generate `find ../posts/ -iname "*.wp"`
	./generate `find ../posts/ -iname "*.md"`

clean:
	rm -rf generate
