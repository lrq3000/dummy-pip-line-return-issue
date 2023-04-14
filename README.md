# dummypiplinereturnbug
Minimal example showing that pip install -e git+... changes line returns in both text and binary files at some point in the unpacking process on Windows OSes

See the GitHub Action cibuil-downstream.yml and run it, it should fail in the `windows-latest` OS, but not in others.

You may try to reproduce on your machine (although I was not successful - maybe it only fails on windows-2019?) with the following commands:

```
pip install --upgrade --editable git+https://github.com/lrq3000/dummypiplinereturnbug/tree/9a6df3d9b2975c894b017543e8195cc46e013093[test] --verbose
pytest src/dummypiplinereturnbug
```

Tested with pip v23.0.1

See this pip issue: https://github.com/pypa/pip/issues/11952

The issue stems from git's default automatic crlf conversion/normalization settings.

The solution is to create a `.gitattributes` file at the root of the git repository, and set inside: `* -text`, which forces git to consider all files in the repository as binary and hence avoid converting line returns, they are kept as-is.

## LICENSE
MIT License
