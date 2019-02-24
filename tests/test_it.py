import pytest
import mdtraj as md
import numpy as np
import argparse as arg
import datetime as dt
import sys
import os

import mdtsne

def test_it():
  myinfilename = os.path.join(os.path.dirname(__file__), 'traj_fit.xtc')
  myintopname = os.path.join(os.path.dirname(__file__), 'reference.pdb')
  mycolvarname = os.path.join(os.path.dirname(__file__), 'results_isomap')
  emb, kld = mdtsne.domdtsne(infilename=myinfilename,
                             intopname=myintopname,
                             out='test1.txt', ncomp=3, skip=1, pcadim=20,
                             perplex=50, niter=10000, init="random",
                             rate=250.0, min_grad_norm=1e-7,
                             metric="euclidean", method="barnes_hut", early_exaggeration=12.0,
                             n_iter_without_progress=300, angle=0.5)
  assert(kld > 1.28 and kld < 1.30)

if __name__ == '__main__':
  pytest.main([__file__])



