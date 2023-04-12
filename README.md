# dummypiplinereturnbug
Minimal example showing that pip install -e git+... changes line returns in both text and binary files at some point in the unpacking process on Windows OSes

See the GitHub Action cibuil-downstream.yml and run it, it should fail in the `windows-latest` OS, but not in others.

You may try to reproduce on your machine (although I was not successful - maybe it only fails on windows-2019?) with the following commands:

```
pip install --upgrade --editable git+https://github.com/lrq3000/dummypiplinereturnbug.git#egg=dummypiplinereturnbug[test] --verbose
pytest src/dummypiplinereturnbug
```

Tested with pip v23.0.1

## LICENSE
MIT License
