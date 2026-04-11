#!/usr/bin/env bash
git filter-branch --index-filter 'git rm -r -q --cached --ignore-unmatch '$1'' --prune-empty --tag-name-filter cat -- --all

rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --prune=now
git gc --aggressive --prune=now
