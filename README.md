# Python environment with Pipfile / Pipfile.lock

This is a mybinder.org, [BinderHub](https://binderhub.readthedocs.io), and
[repo2docker](https://repo2docker.readthedocs.io) compatible git repository to
automatically get the Python dependencies found within `Pipfile` /
`Pipfile.lock` installed by [`pipenv`](https://pipenv.readthedocs.io) and
runnable on a BinderHub such as mybinder.org.

It is meant to showcase how you can make your own git repository compatible as
well, allowing visitors to click a button and start running your code!

## Imagine...

Imagine someone expecting to run code within a git repository, after simply
clicking a button link like this one, because someone suggested that
possibility...

[![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/binder-examples/pipfile?urlpath=/lab/tree/index.ipynb)

This person would end up mybinder.org and see a loading bar - what is going on?

mybinder.org runs a *BinderHub* hosted on multiple *clouds*. BinderHub will with
the help of *repo2docker* both construct a *Dockerfile* and *build* the
Dockerfile into an Docker *image*. This image can with the help of a
[JupyterHub, also on the
cloud](https://github.com/jupyterhub/zero-to-jupyterhub-k8s), be launched into a
Docker *container*. This container can be considered a virtual computer that
mybinder.org dedicates to the visitor. This virtual computer was, within the
link to mybinder.org, asked to be accessed from [Jupyter
Lab](https://jupyterlab.readthedocs.io). From Jupyter Lab, the visitor could
then experiment with the code found in the git repository.

## Notes

The `Pipfile.lock`, or `Pipfile` if there is no lock file, should list all
Python libraries that your code depend on. They will be installed directly into
the main Python environment using the `--system` flag of `pipenv`. Also note
that the `--dev` flag will be used to install also the development dependencies.

When both `Pipfile` and `Pipfile.lock` are found, `--ignore-pipfile` will be
passed to `pipenv` to make the `Pipfile.lock` get prioritized as seemed
reasonable for better reproducibility, so make sure to use run `pipfile lock` to
update your `Pipifile.lock` in the git repository if you add a dependency to a
`Pipfile`.

If you run this repo on mybinder.org, you can verify that the `--dev`
dependencies were installed by running `pytest` directly from a terminal, and by
doing so you also verify that the packages was installed in the main Python
environment.

### Get started using `pipenv` and Pipfile's

You can install Python dependencies with `pipenv` like this:

```bash
pip install pipenv
pipenv install --dev pytest
pipenv install numpy
```

And use them like this:

```bash
pipenv run python -c 'import numpy; print("Hi numpy version {}".format(numpy.__version__))'
```

And also use them like this:

```bash
pipenv shell
python -c 'import numpy; print("Hi numpy version {}".format(numpy.__version__))'
```

### References

- [pipenv's documentation](https://pipenv.readthedocs.io)
- [repo2docker's Pipfile
  reference](https://repo2docker.readthedocs.io/en/latest/config_files.html?highlight=pipfile#pipfile-and-or-pipfile-lock-install-a-python-environment)
