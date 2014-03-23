.PHONY: default clean related_test related_all

default: generate

generate: generate.cpp
	clang++ -g -Ofast -march=native -std=c++11 -o generate generate.cpp

related_all: generate
	./generate `find ../posts/ -iname "*.wp"`
	./generate `find ../posts/ -iname "*.md"`

related_test: generate
	./generate ../posts/2014/02/budgetwarrior-0-3-0-objective-wish-management.wp

clean:
	rm -rf generate
