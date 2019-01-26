# rgardner.github.io

[![Build
Status](https://travis-ci.org/rgardner/rgardner.github.io.svg?branch=master)](https://travis-ci.org/rgardner/rgardner.github.io)

This is the [Jekyll](https://jekyllrb.com/) source of my personal website.

## Development

This project can be built either locally or via Docker.

### Setup

Install dependencies:

```sh
make setup
```

### Working with Jekyll

Serve the website on localhost and rebuild after changes:

```sh
# locally
make serve
# via Docker
make image-serve
```

### Testing

Check Jekyll configuration, links, DNS configuration issues:

```sh
# locally
make test
# via Docker
make image-test
```
