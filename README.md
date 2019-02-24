[![Build Status](https://travis-ci.org/spiwokv/mdtsne.svg?branch=master)](https://travis-ci.org/spiwokv/mdtsne)
[![codecov](https://codecov.io/gh/spiwokv/mdtsne/branch/master/graph/badge.svg)](https://codecov.io/gh/spiwokv/mdtsne/)


# mdtsne

The package `mdtsne` provides Barnes-Hut t-Distributed Stochastic Neighbor Embedding (t-SNE)
for analysis of molecular dynamics trajectories.

## Instalation
```
git clone https://github.com/spiwokv/mdtsne.git
cd mdtsne
sudo pip install .
```

## Requirements
Required Python libraries:
- mdtraj
- sklearn
- numpy
- datetime

## Usage
```
mdtsne -i traj.xtc -p beforemd.pdb -o tsne.txt
```
The trajectory and the topology:
 - must contain only atoms intended for analysis
 - PBC issues must be avoided

For other options see `mdtsne -h`:
```
usage: mdtsne [-h] [-i INFILE] [-p INTOP] [-o OUT] [-outtype OUTTYPE]
              [-n NCOMP] [-skip SKIP] [-pcadim PCADIM] [-perplex PERPLEX]
              [-niter NITER] [-init INIT] [-lr RATE]
              [-min_grad_norm MIN_GRAD_NORM] [-metric METRIC] [-method METHOD]
              [-early_exaggeration EARLY_EXAGGERATION]
              [-n_iter_without_progress N_ITER_WITHOUT_PROGRESS]
              [-angle ANGLE] [-skree SKREE]

Barnes-Hut t-Distributed Stochastic Neighbor Embedding (t-SNE) for analysis of
molecular dynamics trajectories

optional arguments:
  -h, --help            show this help message and exit
  -i INFILE             Input trajectory in pdb, xtc, trr, dcd, netcdf or
                        mdcrd (default "traj.xtc"), WARNING: the trajectory
                        must contain only atoms to be analysed! All PBC issues
                        must be fixed!
  -p INTOP              Input topology in pdb (default "top.pdb"), WARNING:
                        the structure must contain only atoms to be analysed!
  -o OUT                Output file name (default "output.txt").
  -outtype OUTTYPE      Output file type ("txt" or "xvg", default "txt").
  -n NCOMP              Dimension of the embedded space (default 2).
  -skip SKIP            Use every i-th frame (1 - whole trajectory, default).
  -pcadim PCADIM        Dimension of the space preliminary reduced by PCA (0 -
                        no PCA, default 30).
  -perplex PERPLEX      Perplexity tunes the balance between global and local
                        features of your data. It should be 5-50 (default 30).
  -niter NITER          Maximum number of iterations (default 1000)
  -init INIT            Initialization (either "random" or "pca", default
                        "random").
  -lr RATE              Learning rate. Should be 10.0-1000.0 (default 200).
  -min_grad_norm MIN_GRAD_NORM
                        Minimal gradient norm. The optimization will be
                        stopped bellow this threshold (default 1e-7).
  -metric METRIC        Distance metric. Must be available in
                        scipy.spatial.distance.pdist (default "euclidean").
  -method METHOD        Type of t-SNE. Can be "Barnes-Hut" (default) or
                        "exact" (slower).
  -early_exaggeration EARLY_EXAGGERATION
                        Parameter early_exaggeration (default 12.0).
  -n_iter_without_progress N_ITER_WITHOUT_PROGRESS
                        Parameter n_iter_without_progress (default 300).
  -angle ANGLE          Parameter angle (default 0.5).
  -skree SKREE          Name of file to store KL-divergences for 1, 2, ... n
                        dimensions, where n is set by -n (SLOW!)

```

