# python-selenium

## Test Scenario
https://www.online-calculator.com/full-screen-calculator/

## Folder Structure
```
.
├── main.py
├── test_listener.py
    └── before suite
    └── after suite
    └── before test
    └── after test
└── elements
└── internal
└── testsuites
└── testcases
└── reports
```

## Prerequisite
- Python3
- Pip3

## Run
- `python3 -m pip install -r requirements.txt`
- `python3 main.py`

## Parameter
| Key  | Value  | Default  |  Mandatory |   |
|---|---|---|---|---|
|  --test-suite-path |  path |  testsuites |  :x: |   |

## Next Feature
- Decorator
    - This feature will added flag to testcase & test listener function
- Parallel
    - Will add parameter to run testcases parallel with configurable worker
- HTML
    - Will generate Report in HTML
- Browser Selection
    - Will add another browser and can run headless
- Dockerization
    - Will Dockerfile to make easier to run with Docker
