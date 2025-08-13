# Template python project

## Poetry venvs

### VSCode

First, open a terminal (that's not integrated with VSCode, or it'll probably default to the last one you used) and navigate to the project. Then run poetry lock or something to create a venv.

You may need to manually specify the env file after poetry creates it. It's probably easier to have it stored locally in {project_root}/.venv, because VSCode doesn't usually find it otherwise. Even if it does, you'll probably need to select it from the drop-down menu; if it's local, it should be an option. If it's not there, click browse and select the python executable, likely at `C:\.venvs\folder_name\Scripts\python.exe`.

## Running the code (without ImportErrors or ModuleNotFoundErrors)

*project root*: what it sounds like.
*working directory*: where the actual `python` command in run. This should usually be the project root. Be careful if you're using integrated tools or pytest; the working directory isn't always what you'd expect.

There are three methods of running python code:

- *running a file*  to run using `python my_file.py` (targets a file)
- *running a module*: to run using `python -m module_name` (targets a (module) folder) (and its `__main__.py`)
- *running a poetry script*: running an entry in  (no prefix needed) (ex. `$ myscript`)

I distinguish between two types of python files: a *script file* and a *source file*. (`__whatever__.py` files are their own category.)

A *script file* is a python file that **IS NOT** in a module. They can only be run directly and should be in the working directory. They can import each other if all of them are in the [???working or same???] directory, but you'll run into trouble if you put one in a subfolder. If modules are involved, script files usually can't be imported, and so they are usually only used as pure entry points.

A *source file* is a python file that **IS** in a module. It should not be run directly (its imports might break). Instead, either add a `__main__.py` file to the module and run the module, or create an entrypoint script outside the module and run the script.

## Flat layout vs src layout

A flat layout doesn't mean no modules; it just means module folder is `./module1` (i.e. the working directory) rather than `./src/module1`. (Tests are still in `./tests/module1` though.) The src layout is generally preferred. If you run into issues, make sure pyproject.toml has `[tool.poetry]` rather than `[project]` and a `packages` list. If you have any poetry scripts (from the `[tool.poetry.scripts]` list), you will need to run poetry install each time there's a change (or if you get a "missing file" error when you run the script, try `pip install -e .` instead of poetry install--this seems to be an issue with mingw and bash on Windows).
