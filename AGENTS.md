# Repository Guidelines

## Project Structure & Module Organization
- `index.html`, `about.md`, `news.md`, `projects.md`, `resources.md`: top-level pages for the site.
- `_posts/`: dated blog posts named `YYYY-MM-DD-title.md` with YAML front matter; drafts live in `_drafts/` (created via `script/new-post`).
- `_projects/`, `_resources/`: collections rendered with corresponding layouts under `_layouts/`.
- `_layouts/` and `_includes/`: shared HTML templates; `_config.yml` drives site metadata and collection settings.
- `assets/` and `css/`: images and global styles (`css/main.css`).
- `script/`: helper scripts for new posts and site checks; `Rakefile` defines all tasks.

## Build, Test, and Development Commands
- `bundle install`: install Ruby/Jekyll dependencies.
- `rake` or `rake serve`: run `bundle exec jekyll serve --drafts --incremental` for local preview.
- `rake build`: generate the site into `_site/`.
- `rake test`: build, run RuboCop, then `script/htmlproofer` and `script/github-pages-health-check`.
- `rake rubocop` (or `rubocop:autocorrect[_all]`): lint/format Ruby and Rake files.
- `rake new`: create a dated draft post stub in `_drafts/`.
- `rake update`: update all Ruby gems (`bundle update`); run this in dedicated PRs.

## Coding Style & Naming Conventions
- Ruby/Rake: 2-space indentation, `# frozen_string_literal: true` on new files, prefer single quotes unless interpolation is needed.
- Markdown/HTML: include minimal front matter (`layout`, `title`, optional `tags`); keep headings sentence case and filenames lowercase with hyphens.
- CSS: follow existing patterns in `css/main.css`; group related rules and prefer existing variables/utilities.
- Jekyll data: avoid inline HTML where Markdown suffices; use includes/layouts for repeated structures.

## Testing Guidelines
- Run `rake test` before pushing to ensure build, lint, and link checks all pass.
- For links, `script/htmlproofer` ignores some external URLs; still validate new outbound links manually.
- When editing layouts or templates, spot-check generated pages in `_site/` for regressions and run `bundle exec jekyll build` if unsure.

## Commit & Pull Request Guidelines
- Commit messages are short, capitalized summaries (e.g., `Update dependencies (#75)`); keep scope focused and prefer present tense.
- Reference issues/PR numbers when relevant, and group dependency bumps separately.
- PRs should describe the change, note any content additions (new posts/resources), and include screenshots for visual/layout updates.
- Confirm `rake test` passes and mention any skipped checks; note manual verifications (e.g., link targets or responsive layout) in the PR description.
