source "https://rubygems.org"

# Hello! This is where you manage which Jekyll version is used to run.
# When you want to use a different version, change it below, save the
# file and run `bundle install`. Run Jekyll with `bundle exec`, like so:
#
#     bundle exec jekyll serve
#
# This will help ensure the proper Jekyll version is running.
# Happy Jekylling!

gem "github-pages", group: :jekyll_plugins

# If you want to use Jekyll native, uncomment the line below.
# To upgrade, run `bundle update`.

# gem "jekyll"

# Temporarily disabled: wdm fails to build its native extension on this
# Windows setup and is only needed for file watching (jekyll serve --watch /
# --livereload). Build and `serve --no-watch` work without it.
# gem "wdm", "~> 0.1.0" if Gem.win_platform?

# Windows has no built-in tzinfo source; required to resolve the site
# timezone setting in _config.yml on Windows dev machines.
gem "tzinfo-data", platforms: [:mingw, :x64_mingw, :mswin, :jruby]

# If you have any plugins, put them here!
group :jekyll_plugins do
  # gem "jekyll-archives"
  gem "jekyll-feed"
  gem 'jekyll-sitemap'
  # Temporarily disabled: hawkins (livereload) depends on eventmachine, whose
  # prebuilt Windows binary does not support Ruby 3.4 on this machine.
  # Re-enable if livereload is needed and eventmachine builds cleanly.
  # gem 'hawkins'
  gem "webrick", "~> 1.8"
end
