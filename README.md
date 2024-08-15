# biomassbay

Bayesian inference of biomass coefficients of a Flux Balance Analysis problem.

This repository includes a [jupyter notebook](https://jupyter.org/) to run the inference on _Clostridium
autoethanogenum_, used to reproduce the methods section "Bayesian model of the
biomass objective function" for my PhD thesis.

Installation requires [cloning this repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) and installation
of the virtual environment used in [rye](https://rye.astral.sh/):

```bash
git clone https://github.com/carrascomj/biomassbay.git
cd biomassbay
# setup virtual environment and install dependencies 
rye sync
```

> Alternatively, `pip install --requirements requirements.lock` works just as fine, but virtual environment must set up manually.

This will set up a python environment. To use the jupyter notebook, create a
jupyter kernel and add it to jupyterlab.

```bash
# activate environment
source .venv/bin/activate
# install ipykernel
rye add --dev ipykernel  # or pip install ipykernel
python -m ipykernel install --user --name=biomassbay
```

> Alternatively, install everything on the python environment containing your jupyterlab, proceed on your on risk!

Finally, open the notebook on jupyterlab:

```bash
jupyterlab notebooks/bayesian_biomass_story.ipynb
```
