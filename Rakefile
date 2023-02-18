# frozen_string_literal: true

require 'rake/clean'
require 'rubocop/rake_task'

CLEAN << '_site'

task default: %w[serve]

RuboCop::RakeTask.new do |task|
  task.requires << 'rubocop-rake'
end

desc 'Build site'
task :build do
  sh 'bundle exec jekyll build'
end

desc 'Run tests'
task test: %i[build rubocop] do
  sh 'script/htmlproofer && script/github-pages-health-check'
end

desc 'Run site'
task :serve do
  sh 'bundle exec jekyll serve --drafts --incremental'
end

desc 'Update dependencies'
task :update do
  sh 'bundle update'
end

desc 'Create a new post'
task :new do
  sh 'script/new-post'
end

desc 'Run CI tests'
task ci: [:test]
