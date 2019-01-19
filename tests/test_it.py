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
                             out='', ncomp=2, skip=0, pcadim=20,
                             perplex=50, niter=1000, init="pca")
  assert(kld > 0.99)

if __name__ == '__main__':
  pytest.main([__file__])



