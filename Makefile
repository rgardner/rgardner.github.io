all: build

setup:
	gem install bundler
	bundle install

build:
	bundle exec jekyll build

serve:
	bundle exec jekyll serve --watch

test:
	script/cibuild

new:
	script/new-post

update-depencies:
	bundle update

clean:
	-rm -r _site

.PHONY: all setup build serve test new  update-depdencies clean
