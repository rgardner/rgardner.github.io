all: build

build:
	bundle exec jekyll build

serve:
	bundle exec jekyll serve

test:
	script/cibuild

new:
	script/new-post

update-resume:
	script/update-resume

clean:
	-rm -r _site

.PHONY: all build serve test new update-resume clean
