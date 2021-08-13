A modified Github Pages template for academic websites. This was forked (then detached) by [Nathan Lawrence](https://github.com/NPLawrence) from the [Academic Pages Theme](https://github.com/academicpages/academicpages.github.io), which was forked (then detached) by [Stuart Geiger](https://github.com/staeiou) from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/), which is © 2016 Michael Rose and released under the MIT License. See LICENSE.md.

[This](https://www.aleksandrhovhannisyan.com/blog/getting-started-with-jekyll-and-github-pages/) is the best blog post I found for getting started with Jekyll and GitHub Pages.

See the linked themes above for their corresponding documentation and instructions. Here are the basic instruction and changes I made.

# Instructions

1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by clicking the "fork" button in the top right. 
1. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
1. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section
1. (Optional) Use the Jupyter notebooks or python scripts in the `markdown_generator` folder to generate markdown files for publications and talks from a TSV file.

See more info at https://academicpages.github.io/

## To run locally (not on GitHub Pages, to serve on your own computer)

1. Clone the repository and made updates as detailed above
1. Make sure you have ruby-dev, bundler, and nodejs installed: `sudo apt install ruby-dev ruby-bundler nodejs`
1. Run `bundle clean` to clean up the directory (no need to run `--force`)
1. Run `bundle install` to install ruby dependencies. If you get errors, delete Gemfile.lock and try again.
1. Run `bundle exec jekyll liveserve` to generate the HTML and serve it from `localhost:4000` the local server will automatically rebuild and refresh the pages on change.

# Changes to [Academic Pages Theme](https://github.com/academicpages/academicpages.github.io)

- Code snippets and styling inspiration from [DAIS lab website](https://github.com/daisubc/daisubc.github.io) and [Markdown-CV](https://github.com/elipapa/markdown-cv).
- I created a custom format for displaying publications.
  - Publications are sorted based on type (journal, conference, etc). 
  - Add notes and extra links (like arXiv or code) to publication entries.
  - Optionally, one may display only recent publications, for example, on the homepage.
- I created a custom format for the CV inspired by [Markdown-CV](https://github.com/elipapa/markdown-cv).
  - It is consistent with the academic pages format.
  - All the CV data is in .yaml files, which is accompanied by an `include` function for generating the CV.
- My website is minimal with only a CV in the navigation bar. All the original features (like blogging) of the Academic Pages Theme still exists.
