# Usage

1. Open workspace

```bash
code vscode-workspace-dbt-sample.code-workspace
```

2. Install python extension

```bash
cd dbt_sample
poetry install
poetry shell # <-- check your shell interpreter name
```

3. select python interpreter for each folder
    1. `Cmd + Shift + P` shortcut
    2. Select `Python: Select Interpreter`
    3. Select `dbt_sample` folder
    3. Select the virtual environment created when the poetry shell was created.
