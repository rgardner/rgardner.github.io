# bob-gardner.com

![Jekyll CI status](https://github.com/rgardner/rgardner.github.io/workflows/Jekyll/badge.svg)

This is the [Jekyll](https://jekyllrb.com/) source of my personal website, <https://www.bob-gardner.com>.

## Development

This project can be built via Docker.

### Setup

Install dependencies:

```sh
pip install invoke
```

### Working with Jekyll

Serve the website on localhost and rebuild after changes:

```sh
invoke serve
```

### Testing

Check Jekyll configuration, links, DNS configuration issues:

```sh
invoke test
```

### Miscellaneous Build Tasks

```sh
# list all build tasks
invoke --list
# create a new post
invoke new-post
# update dependencies
invoke update-dependencies
```
