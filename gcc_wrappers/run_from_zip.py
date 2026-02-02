from cookiecutter.main import cookiecutter
import importlib.resources


def run_lite_from_zip():
    resource = importlib.resources.files("gcc_wrappers.zip_templates").joinpath(
        "gcc_manual.zip"
    )
    with importlib.resources.as_file(resource) as path:
        cookiecutter(template=str(path))


##
# issue with python created zip file is the folder is not recognised
# need to fix it to automate the work but works as a poc

if __name__ == "__main__":
    run_lite_from_zip()
