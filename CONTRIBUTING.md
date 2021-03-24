# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs, Request Features or Submit Feedback

Report bugs as a [GitHub issue](https://github.com/uwhackweek/jupyterbook-template/issues).

Look through the (https://github.com/executablebooks/cookiecutter-jupyter-book/issues) for bugs, feature requests, etc and feel free to contribute!

## Get Started

Ready to contribute? Here's how to set up `jupyterbook-template` for local development.

1. Fork the `jupyterbook-template` repo on GitHub.
2. Clone your fork locally and install requirements:

```sh
git clone git@github.com:your_name_here/jupyterbook-template.git
conda create -n jupyterbook-template python=3.7
conda activate jupyterbook-template
pip install -r requirements.txt
```

3. Create a branch for local development:

```sh
git checkout -b name-of-your-bugfix-or-feature
```

4. Make your desired changes, run tests, and push your branch to GitHub when you're ready:

```sh
pytest
black ./ --check
git add .
git commit -m "Your detailed description of your changes."
git push origin name-of-your-bugfix-or-feature
```

5. Open a pull request through the GitHub website.
