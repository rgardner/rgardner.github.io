---
layout: post
title: Web Scraping with Jupyter Notebooks
tags: [python]
---

Last year I worked on a web scraper to automatically download [Creative
Market](https://creativemarket.com/)'s Free Goods of the Week. Each week,
Creative Market sends an email to subscribers to download these 6 free
assets. Subscribers then log in, go to
<https://creativemarket.com/free-goods>, and then click one or both of the
"Sync to Dropbox" or "Free Download" buttons. My partner was manually doing
this each day and when I was looking for a software project to work on, this
seemed like a good candidate for automation that would remove a small, but
minor inconvenience of hers.

<!-- more -->

The GitHub repo is here: <https://github.com/rgardner/design-asset-utils>. It
has been archived because Creative Market has since disabled scrapers from
accessing their site. Their whole website (not just the log in page), now
requires passing a Google reCAPTCHA test if it suspects an automated system
is being used. For what it's worth, their [terms of
service](https://creativemarket.com/terms) seem to allow automated systems as
long as they are using the service fairly (e.g. no resharing assets, use rate
limiting, and no malware). But I knew they could break web scraping anyways.
c'est la vie. While this project is dead, I thought the technique could be
valuable to others, hence the blog post.

## Web Scraping

I chose Python and Jupyter Notebooks because I wanted an interactive
development experience when working on the web scraper. I had worked on web
scrapers in the past (e.g. <https://github.com/rgardner/citi-bike-notifier>)
and I found the development experience painful.

First, when the website UI changes, you need to be able to see the contents
of the new page to be able to diagnose and fix the scraping code. For
example, an error like `selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"id","selector":"input-username"}` doesn't tell you if the element
has simply been renamed or if you've been redirected to a completely
different page.

Second, to reduce the dev inner loop, you want to be able to cache the state
of the website to avoid re-logging in every time, or slowly clicking buttons
in the correct order. So you run the script under a debugger, make the fix,
and then re-run the script from the beginning. But with Jupyter Notebooks,
you can edit and continue, edit the same cell repeatedly, or execute the
cells out of order. Jupyter Notebooks can also display images inline, which
makes it easy to take and display a screenshot when a scraping exception
occurs.

My Jupyter notebook is here:
[downloader.ipynb](https://github.com/rgardner/design-asset-utils/blob/master/creative-market/downloader.ipynb).
It uses environment variables to receive input (following the [12 Factor
Methodology](https://12factor.net/)), enables verbose logging to `stdout`,
which displays after each cell in the notebook, and defines a function
`log_error` to display a screenshot.

```python3
def log_error(driver):
    display(Image(driver.get_screenshot_as_png()))
```

I use it like this:

```python3
try:
    driver.login(CREATIVE_MARKET_USERNAME, CREATIVE_MARKET_PASSWORD)
except WebDriverException:
    log_error(driver)
    raise
```

Note the screenshot does not display when running from the command line like so:

```sh
jupyter nbconvert --execute --stdout downloader.ipynb
```

For this project, I put some web scraping code that I intended to share with
a [test
script](https://github.com/rgardner/design-asset-utils/blob/ea1ebd330c07a2a1fcadf12181bb2b2695e04bc3/creative-market/checker.py)
into a common Python module called
[creative_market.py](https://github.com/rgardner/design-asset-utils/blob/ea1ebd330c07a2a1fcadf12181bb2b2695e04bc3/creative-market/creative_market.py).

## Putting it all together

To run the notebook non-interactively, use:

```python3
jupyter nbconvert --execute --stdout downloader.ipynb
```

This app was deployed to Heroku and only needs to run once per week. Heroku
doesn't have an easy way of scheduling jobs, so I wrote a module called
[clock.py](https://github.com/rgardner/design-asset-utils/blob/ea1ebd330c07a2a1fcadf12181bb2b2695e04bc3/creative-market/clock.py)
which uses [APScheduler](https://apscheduler.readthedocs.io/en/stable/) to
schedule the downloader to run every Monday:

```python3
import subprocess

from apscheduler.schedulers.blocking import BlockingScheduler

SCHEDULER = BlockingScheduler()


@SCHEDULER.scheduled_job('cron', day_of_week='mon', hour=17)
def scheduled_download():
    print('Scheduling downloader...')
    return subprocess.run(
        ['jupyter', 'nbconvert', '--execute', '--stdout', 'downloader.ipynb'])
```

I also wrote a [test
script](https://github.com/rgardner/design-asset-utils/blob/ea1ebd330c07a2a1fcadf12181bb2b2695e04bc3/creative-market/checker.py)
to scrape Creative Market and confirm that the links were successfully
clicked, if not, notifying me via email. That is scheduled to run a few
minutes after.

## Conclusion

The full project is here: <https://github.com/rgardner/design-asset-utils>. I
hope you find it useful!
