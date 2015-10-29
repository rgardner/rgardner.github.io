all: build

build:
	bundle exec jekyll build

serve:
	bundle exec jekyll serve

test:
	script/cibuild

new:
	@script/new-post

resume:
	script/update-resume

clean:
	-rm -r _site

.PHONY: build test new resume clean
