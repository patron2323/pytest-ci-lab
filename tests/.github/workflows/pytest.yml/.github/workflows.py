name: Python Test Automation

on:
  push:
    branches: [ main ]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Reponun içeriğini al
      uses: actions/checkout@v3

    - name: Python kurulumu
      uses: actions/setup-python@v4
      with:
        python-version: "3.10"

    - name: pytest yükle
      run: pip install pytest

    - name: Testleri çalıştır
      run: pytest
