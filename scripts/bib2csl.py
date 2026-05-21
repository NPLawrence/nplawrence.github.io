#!/usr/bin/env python3
"""Convert cv/publications/*.bib to _data/publications.yaml (CSL-JSON format).

Run from the repo root: python scripts/bib2csl.py
"""

import os
import re
import yaml
import bibtexparser.customization as bc
from bibtexparser.bparser import BibTexParser

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLICATIONS_DIR = os.path.join(REPO_ROOT, 'cv', 'publications')
OUTPUT_FILE = os.path.join(REPO_ROOT, '_data', 'publications.yaml')

# Map BibTeX source file → CSL type (file takes priority over @entry type)
BIB_FILE_TYPES = {
    'in_progress.bib': 'manuscript',
    'journal.bib': 'article-journal',
    'conference.bib': 'paper-conference',
    'patent.bib': 'patent',
    'thesis.bib': 'thesis',
}


def clean_latex(text):
    """Strip LaTeX markup for plain-text display."""
    if not isinstance(text, str):
        return text
    # Strip nested braces iteratively
    prev = None
    while prev != text:
        prev = text
        text = re.sub(r'\{([^{}]*)\}', r'\1', text)
    # Common LaTeX special characters
    for old, new in [
        (r'\"o', 'ö'), (r'\"u', 'ü'), (r'\"a', 'ä'),
        (r'\"O', 'Ö'), (r'\"U', 'Ü'), (r'\"A', 'Ä'),
        (r"\'e", 'é'), (r"\'a", 'á'), (r"\'o", 'ó'),
        (r'\\&', '&'), (r'\\%', '%'), (r'\\$', '$'),
        ('---', '—'), ('--', '–'),
    ]:
        text = text.replace(old, new)
    # Remove remaining LaTeX commands like \textit{...}
    text = re.sub(r'\\[a-zA-Z]+\{([^{}]*)\}', r'\1', text)
    return text.strip()


def parse_authors(author_list):
    """Convert bibtexparser author list ('Last, First') to CSL [{family, given}]."""
    result = []
    for author in author_list:
        parts = author.split(', ', 1)
        if len(parts) == 2:
            family, given = parts[0].strip(), parts[1].strip()
        else:
            words = parts[0].split()
            family = words[-1] if words else parts[0]
            given = ' '.join(words[:-1]) if len(words) > 1 else ''
        result.append({'family': clean_latex(family), 'given': clean_latex(given)})
    return result


def entry_to_csl(entry, csl_type):
    """Convert a bibtexparser entry dict to a CSL-JSON dict."""
    csl = {'id': entry['ID'], 'type': csl_type}

    if 'title' in entry:
        csl['title'] = clean_latex(entry['title'])

    if 'year' in entry:
        csl['year'] = entry['year']

    if 'author' in entry:
        csl['author'] = parse_authors(entry['author'])

    # Venue: _venue takes priority over journal/booktitle
    venue = clean_latex(entry.get('_venue', '') or entry.get('journal', '') or entry.get('booktitle', ''))
    if venue:
        if csl_type == 'paper-conference':
            csl['event-title'] = venue
        else:
            csl['container-title'] = venue

    # DOI — normalize to bare DOI (without URL prefix)
    doi = entry.get('doi', '').strip()
    if doi:
        doi = re.sub(r'^https?://doi\.org/', '', doi)
        csl['DOI'] = doi
        csl['URL'] = f'https://doi.org/{doi}'

    # URL: arxiv links → archive; others → URL (don't override DOI-based URL)
    url = entry.get('url', '').strip()
    if url:
        if 'arxiv.org' in url.lower():
            csl['archive'] = url
        elif 'URL' not in csl:
            csl['URL'] = url

    # Note (e.g. "Spotlight", "Keynote")
    note = entry.get('_note', '').strip()
    if not note:
        note = entry.get('note', '').strip()
    if note:
        csl['note'] = clean_latex(note)

    # Code link
    if 'codeurl' in entry and entry['codeurl']:
        csl['code'] = entry['codeurl']

    # Volume and pages
    if 'volume' in entry and entry['volume']:
        csl['volume'] = entry['volume']
    if 'pages' in entry and entry['pages']:
        csl['page'] = entry['pages']

    return csl


def parse_bib_file(filepath, csl_type):
    """Parse a BibTeX file and return list of CSL dicts."""
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    parser = BibTexParser()
    parser.customization = bc.author
    parser.ignore_nonstandard_types = False
    db = parser.parse(text)
    return [entry_to_csl(e, csl_type) for e in db.entries]


def main():
    all_entries = []
    for bib_file, csl_type in BIB_FILE_TYPES.items():
        filepath = os.path.join(PUBLICATIONS_DIR, bib_file)
        if not os.path.exists(filepath):
            print(f'Warning: {bib_file} not found, skipping')
            continue
        entries = parse_bib_file(filepath, csl_type)
        print(f'{bib_file}: {len(entries)} entries → type={csl_type}')
        all_entries.extend(entries)

    output = {'references': all_entries}

    header = '# Auto-generated from cv/publications/*.bib — edit the .bib files, not this file\n'
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(header)
        yaml.dump(output, f, default_flow_style=False, allow_unicode=True,
                  sort_keys=False)

    print(f'\nWrote {len(all_entries)} publications to _data/publications.yaml')


if __name__ == '__main__':
    main()
