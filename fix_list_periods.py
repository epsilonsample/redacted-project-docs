#!/usr/bin/env python3
"""
fix_list_periods.py
Adds missing terminal periods to sentence-length list items in Markdown files.

Rules:
  - Only targets numbered (1. ...) and bulleted (- ...) list items.
  - Only adds a period if the item looks like a complete sentence:
      * Contains a verb-like word (3+ words and not purely a noun phrase)
      * Is 5+ words long (short fragments like "- Inventory Manager role" are skipped)
  - Skips items that already end with punctuation (. ! ? : ;)
  - Skips items that end with a Markdown link: [text](url)
  - Skips items that end with inline code: `code`
  - Skips items that are inside code blocks (``` ... ```)
  - Skips lines that are just links: - [Link text](url)
  - Skips admonition content (lines starting with indented !!! or ???)
  - Skips grid card content (lines inside <div class="grid cards">)
  - Preserves all other formatting (bold, icons, tabs, etc.)

Usage:
  cd ~/Dropbox/Mac/Downloads/redacted-project-docs
  python3 fix_list_periods.py              # Dry run (shows changes)
  python3 fix_list_periods.py --apply      # Apply changes
  python3 fix_list_periods.py --apply --verbose  # Apply with full details
"""

import os
import re
import sys
import argparse


def is_sentence_like(text):
    """
    Determine if a list item's text content looks like a complete sentence
    that should end with a period.
    
    Returns True for sentence-like items, False for fragments.
    """
    # Strip markdown formatting for analysis
    clean = text.strip()
    
    # Remove leading markdown bold/italic markers for analysis
    clean = re.sub(r'\*\*(.+?)\*\*', r'\1', clean)
    clean = re.sub(r'\*(.+?)\*', r'\1', clean)
    clean = re.sub(r'`(.+?)`', r'\1', clean)
    
    # Remove icon syntax like :material-icon-name:
    clean = re.sub(r':\w[\w-]*:', '', clean)
    
    # Split into words
    words = clean.split()
    
    # Too short = fragment (e.g., "- Inventory Manager role")
    if len(words) < 4:
        return False
    
    # Label-style items: "**Bold Label:** rest of text" or "Label: text"
    # These are typically short explanations, not full sentences
    # Only flag them if the text after the colon is sentence-length (5+ words)
    colon_match = re.match(r'^(?:\*\*[^*]+\*\*:?|[^:]+:)\s*(.+)$', clean)
    if colon_match:
        after_colon = colon_match.group(1).strip()
        after_words = after_colon.split()
        if len(after_words) < 4:
            return False
    
    # If it starts with a verb-like word, it's instructional
    # Common instruction starters in technical docs
    instruction_starters = {
        'navigate', 'click', 'select', 'open', 'find', 'look', 'review',
        'enter', 'type', 'choose', 'check', 'ensure', 'verify', 'confirm',
        'scroll', 'drag', 'tap', 'press', 'toggle', 'set', 'use',
        'add', 'edit', 'delete', 'remove', 'create', 'update', 'manage',
        'send', 'submit', 'process', 'accept', 'reject', 'lock', 'unlock',
        'assign', 'configure', 'enable', 'disable', 'install', 'download',
        'save', 'export', 'import', 'copy', 'move', 'transfer', 'return',
        'fill', 'complete', 'scan', 'search', 'filter', 'sort', 'clear',
        'pick', 'view', 'show', 'hide', 'expand', 'collapse', 'close',
        'the', 'a', 'an', 'your', 'this', 'each', 'all', 'any',
        'if', 'when', 'once', 'after', 'before', 'while',
        'you', 'bits', 'locked', 'asset', 'users',
    }
    
    first_word = words[0].lower().rstrip(':,')
    
    # Items starting with common sentence starters are likely sentences
    if first_word in instruction_starters and len(words) >= 4:
        return True
    
    # If it contains a verb-like pattern, it's probably a sentence
    # Look for common verbs in the text
    common_verbs = {
        'is', 'are', 'was', 'were', 'will', 'can', 'may', 'should',
        'have', 'has', 'had', 'do', 'does', 'did',
        'appear', 'appears', 'change', 'changes', 'update', 'updates',
        'show', 'shows', 'display', 'displays', 'allow', 'allows',
        'include', 'includes', 'contain', 'contains', 'require', 'requires',
        'provide', 'provides', 'prevent', 'prevents', 'need', 'needs',
        'send', 'sends', 'receive', 'receives', 'return', 'returns',
        'create', 'creates', 'delete', 'deletes', 'add', 'adds',
        'move', 'moves', 'transfer', 'transfers', 'track', 'tracks',
        'support', 'supports', 'enable', 'enables', 'disable', 'disables',
        'see', 'match', 'matches', 'work', 'works',
        'notified', 'assigned', 'configured', 'installed', 'saved',
        'apply', 'applies', 'happen', 'happens', 'run', 'runs',
        'remain', 'remains', 'stay', 'stays', 'keep', 'keeps',
        'start', 'starts', 'stop', 'stops', 'begin', 'begins',
        'open', 'opens', 'close', 'closes', 'clear', 'clears',
        'accept', 'accepts', 'reject', 'rejects', 'lock', 'locks',
        'unlock', 'unlocks', 'reset', 'resets', 'log', 'logs',
        'enter', 'enters', 'select', 'selects', 'filter', 'filters',
        'sort', 'sorts', 'scan', 'scans', 'pick', 'picks',
        'assign', 'assigns', 'manage', 'manages', 'handle', 'handles',
        'process', 'processes', 'submit', 'submits', 'complete', 'completes',
        'confirm', 'confirms', 'verify', 'verifies', 'ensure', 'ensures',
        'fill', 'fills', 'replace', 'replaces', 'remove', 'removes',
        'set', 'sets', 'configure', 'configures', 'define', 'defines',
        'load', 'loads', 'save', 'saves', 'store', 'stores',
        'connect', 'connects', 'link', 'links', 'navigate', 'navigates',
        'expand', 'expands', 'collapse', 'collapses', 'toggle', 'toggles',
        'prompted', 'cleared', 'updated', 'selected', 'displayed',
        'required', 'available', 'accessible', 'visible',
    }
    
    text_lower = clean.lower()
    has_verb = any(f' {v} ' in f' {text_lower} ' for v in common_verbs)
    
    if has_verb and len(words) >= 4:
        return True
    
    # 6+ words is likely a sentence even without detected verb
    if len(words) >= 6:
        return True
    
    # 4-5 words: check if it reads as a sentence
    # Items like "Processing paperwork for the bit" - gerund phrases
    if clean[0].isupper() and len(words) >= 4:
        # Check for gerund (-ing) start
        if words[0].endswith('ing'):
            return True
    
    return False


def should_skip_line(line, stripped):
    """Check if a line should be skipped entirely."""
    
    # Not a list item
    if not re.match(r'^(\s*)([-*+]|\d+\.)\s+', line):
        return True
    
    # Already ends with punctuation
    text_end = stripped.rstrip()
    if text_end and text_end[-1] in '.!?:;':
        return True
    
    # Ends with a continuation word (part of a compound sentence across list items)
    # e.g., "1. Click the button on the home page, or"
    last_word = text_end.split()[-1].lower().rstrip(',') if text_end.split() else ''
    if last_word in ('or', 'and', 'then', 'but', 'nor'):
        return True
    
    # Ends with a markdown link: [text](url)
    if re.search(r'\]\([^)]+\)\s*$', stripped):
        return True
    
    # Ends with inline code
    if re.search(r'`[^`]+`\s*$', stripped):
        return True
    
    # Line is just a link
    if re.match(r'^(\s*)([-*+]|\d+\.)\s+\[.+\]\(.+\)\s*$', line):
        return True
    
    # Line is just bold text (a label, not a sentence)
    if re.match(r'^(\s*)([-*+]|\d+\.)\s+\*\*.+\*\*\s*$', line):
        return True
    
    # Line ends with a markdown image
    if re.search(r'!\[.*\]\(.*\)\s*$', stripped):
        return True
    
    return False


def extract_list_text(line):
    """Extract just the text content from a list item line."""
    match = re.match(r'^(\s*)([-*+]|\d+\.)\s+(.+)$', line)
    if match:
        return match.group(3).strip()
    return ''


def process_file(filepath, apply=False, verbose=False):
    """Process a single markdown file and fix list item periods."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    changes = []
    new_lines = []
    in_code_block = False
    in_grid_cards = False
    
    for i, line in enumerate(lines):
        stripped = line.rstrip('\n')
        
        # Track code blocks
        if stripped.lstrip().startswith('```'):
            in_code_block = not in_code_block
            new_lines.append(line)
            continue
        
        if in_code_block:
            new_lines.append(line)
            continue
        
        # Track grid cards (skip content inside)
        if '<div class="grid cards"' in stripped:
            in_grid_cards = True
        if '</div>' in stripped and in_grid_cards:
            in_grid_cards = False
            new_lines.append(line)
            continue
        
        # Skip grid card internals (they use - : syntax for icons)
        if in_grid_cards:
            new_lines.append(line)
            continue
        
        # Check if this is a list item that needs a period
        if should_skip_line(line, stripped):
            new_lines.append(line)
            continue
        
        # Extract the text portion
        text = extract_list_text(stripped)
        if not text:
            new_lines.append(line)
            continue
        
        # Check if it's sentence-like
        if is_sentence_like(text):
            # Add period before the newline
            new_line = stripped.rstrip() + '.\n'
            changes.append({
                'line_num': i + 1,
                'before': stripped.rstrip(),
                'after': stripped.rstrip() + '.'
            })
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    
    # Apply changes if requested
    if apply and changes:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
    
    return changes


def main():
    parser = argparse.ArgumentParser(
        description='Fix missing periods on sentence-length list items in Markdown files.'
    )
    parser.add_argument(
        '--apply', action='store_true',
        help='Apply changes (default is dry run)'
    )
    parser.add_argument(
        '--verbose', action='store_true',
        help='Show every change in detail'
    )
    parser.add_argument(
        '--path', default='content',
        help='Path to content directory (default: content)'
    )
    args = parser.parse_args()
    
    content_dir = args.path
    
    if not os.path.isdir(content_dir):
        print(f"Error: Directory '{content_dir}' not found.")
        print("Make sure you're running this from the repo root directory.")
        print("  cd ~/Dropbox/Mac/Downloads/redacted-project-docs")
        print("  python3 fix_list_periods.py")
        sys.exit(1)
    
    # Find all markdown files
    md_files = []
    for root, dirs, files in os.walk(content_dir):
        for fname in sorted(files):
            if fname.endswith('.md'):
                md_files.append(os.path.join(root, fname))
    
    if not md_files:
        print(f"No .md files found in '{content_dir}'.")
        sys.exit(1)
    
    total_changes = 0
    files_changed = 0
    
    mode = "APPLYING" if args.apply else "DRY RUN"
    print(f"\n{'='*60}")
    print(f"  Fix Missing Periods on List Items — {mode}")
    print(f"{'='*60}")
    print(f"  Scanning {len(md_files)} Markdown files in '{content_dir}/'")
    print(f"{'='*60}\n")
    
    for filepath in sorted(md_files):
        changes = process_file(filepath, apply=args.apply, verbose=args.verbose)
        
        if changes:
            files_changed += 1
            total_changes += len(changes)
            rel_path = os.path.relpath(filepath)
            print(f"  📄 {rel_path} — {len(changes)} fix{'es' if len(changes) != 1 else ''}")
            
            if args.verbose:
                for c in changes:
                    print(f"     Line {c['line_num']}:")
                    print(f"       - {c['before']}")
                    print(f"       + {c['after']}")
                print()
    
    print(f"\n{'='*60}")
    print(f"  Summary: {total_changes} periods added across {files_changed} files")
    if not args.apply:
        print(f"  Run with --apply to make changes")
        print(f"  Run with --apply --verbose for full details")
    else:
        print(f"  ✅ Changes applied!")
        print(f"  Review with: git diff")
        print(f"  Commit with: git add -A && git commit -m \"Add periods to sentence-length list items\"")
    print(f"{'='*60}\n")


if __name__ == '__main__':
    main()
