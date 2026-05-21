This repository contains my personal academic website. It is based on the [Academic Pages Theme](https://github.com/academicpages/academicpages.github.io), which was forked from [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/).

The site has two separate workflows:

- The Jekyll website lives at the repository root and is what you preview locally.
- The CV source lives under `cv/` and is generated separately from the website.

## Setup

1. Clone the repository.
1. Install Ruby, Bundler, and Node.js if they are not already available.
1. Install the Ruby dependencies from the repo root with `bundle install`.
1. If you plan to edit the CV source, install the Python dependencies under `cv/` with `python3 -m venv cv/.venv`, `source cv/.venv/bin/activate`, and `pip install -r cv/requirements.txt`.

## Preview The Website

Run the local Jekyll server from the repository root:

`bundle exec jekyll serve --livereload --host 127.0.0.1 --port 4000`

Then open http://127.0.0.1:4000. Jekyll will rebuild automatically when you edit pages, posts, data files, or assets.

## Edit Content

- Edit site pages in `_pages/` and `_posts/`.
- Edit navigation, author info, and shared site data in `_data/`.
- Put downloadable files in `files/` and images in `images/` or `assets/images/`.
- If you change publication metadata from BibTeX, regenerate the site data with `python scripts/bib2csl.py` from the repository root.

## Edit The CV

The CV is generated from the files under `cv/`.

- Update the CV data in `cv/cv.yaml`.
- Update publication sources in `cv/publications/*.bib`.
- Update layout and rendering logic in `cv/templates/` if the output structure needs to change.
- Regenerate the publication data that the website uses with `python scripts/bib2csl.py`.
- Regenerate the CV source with `cd cv && python generate.py cv.yaml -l`.

If you want the CV PDF, you also need a LaTeX toolchain with `latexmk` and `biber`, then build from `cv/` using `make`.

## Notes

- Do not edit the generated `_site/` output directly; Jekyll rewrites it on the next build.
- The `cv/` generator tree is excluded from Jekyll so local preview stays focused on the website.
- The site is intentionally minimal and keeps the CV in the navigation bar.
