all: build

build:
	jekyll build

test:
	script/cibuild

resume:
	script/update-resume

clean:
	rm _site

.PHONY: build, test, resume, clean
