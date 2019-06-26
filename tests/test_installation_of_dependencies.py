def test_dependencies_are_installed():
    import numpy
    import seaborn
    print("Wieee!")

def test_pipfile_specified_python_version():
    import sys
    assert sys.version_info[:2] == (3, 6)
