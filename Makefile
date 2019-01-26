all: build

setup:
	script/install

build:
	bundle exec jekyll build

serve:
	bundle exec jekyll serve --watch

test:
	script/run-tests

new:
	script/new-post

update-depencies:
	bundle update

clean:
	-rm -r _site

image-serve:
	docker run \
	--rm \
	-v=${PWD}:/srv/jekyll \
	-p 4000:4000 \
	jekyll/jekyll \
	jekyll serve

image-test:
	docker run \
	--rm \
	-v=${PWD}:/srv/jekyll \
	-p 4000:4000 \
	jekyll/jekyll \
	/bin/bash -c "script/install && script/run-tests"

.PHONY:
	all setup build serve test new  update-depdencies clean
	image-serve image-test
