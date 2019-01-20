# Loading necessary libraries
libnames = [('mdtraj', 'md'), ('numpy', 'np'), ('argparse', 'arg'), ('datetime', 'dt'), ('sys', 'sys')]

for (name, short) in libnames:
  try:
    lib = __import__(name)
  except:
    print("Library %s is not installed, exiting" % name)
    exit(0)
  else:
    globals()[short] = lib
try:
  import sklearn.manifold as sk
except:
  print("Library sklearn.manifold is not installed, exiting")
  exit(0)
try:
  import sklearn.decomposition as skd
except:
  print("Library sklearn.decomposition is not installed, exiting")
  exit(0)

  
def domdtsne(infilename, intopname, out='tsne.txt', ncomp=2, skip=1, pcadim=30,
             perplex=30.0, niter=1000, init='random', rate=250.0, min_grad_norm=1e-7,
             metric="euclidean", method="barnes_hut", early_exaggeration=12.0,
             n_iter_without_progress=300, angle=0.5):
  # Loading trajectory
  try:
    print("Loading trajectory")
    refpdb = md.load_pdb(intopname)
    traj = md.load(infilename, top=intopname)
    print("Fitting trajectory")
    traj.superpose(refpdb)
  except:
    print("Cannot load %s or %s, exiting." % (infilename, intopname))
    exit(0)
  else:
    print("%s succesfully loaded and fitted" % traj)
  print("")
  trajsize = traj.xyz.shape
  traj2 = np.zeros((int(float(trajsize[0])/float(skip)), trajsize[1]*3))
  for i in range(trajsize[1]):
    traj2[:,3*i]   = traj.xyz[:,i*skip,0]
    traj2[:,3*i+1] = traj.xyz[:,i*skip,1]
    traj2[:,3*i+2] = traj.xyz[:,i*skip,2]
    
  # Runing preliminary PCA
  if pcadim>0:
    if pcadim<trajsize[1]:
      print "Runing preliminary PCA"
      pca = skd.PCA(n_components=pcadim, svd_solver='randomized', random_state=None)
      traj2 = pca.fit_transform(traj2).astype(np.float32, copy=False)
    else:
      print("WARNING: There is no point in doing PCA because the pcadim > 3 x number of atoms")
      print("         Skipping PCA.")
  
  # Calculating t-SNE
  print "Caclulating t-SNE"
  tsnemodel = sk.TSNE(n_components=ncomp, perplexity=perplex, early_exaggeration=early_exaggeration,
                      learning_rate=rate, n_iter=niter, n_iter_without_progress=n_iter_without_progress,
                      min_grad_norm=min_grad_norm, metric=metric, init="random", method=method,
                      angle=angle, verbose=1).fit(traj2)
  embeddings = tsnemodel.embedding_
  kldivedgence = tsnemodel.kl_divergence_
  from sklearn.manifold.t_sne import _joint_probabilities
  from sklearn.metrics import pairwise_distances
  if metric == "euclidean":
    distances = pairwise_distances(traj2, metric=metric, squared=True)
  P = _joint_probabilities(distances,perplex,0)
  pps = open("pps.txt", "w")
  for pp in P:
    pps.write("%25.20f\n" % pp)
  pps.close()

  # Writing t-SNE embeddings
  print("Writing t-SNE embeddings into %s" % out)
  print("")
  if out[-3:]=="xvg":
    ofile = open(out, "w")
    ofile.write("# This file was created on %s\n" % dt.datetime.now().isoformat())
    ofile.write("# Created by: mdtsne\n")
    sysargv = ""
    for item in sys.argv:
      sysargv = sysargv+item+" "
    ofile.write("# Command line: %s\n" % sysargv)
    ofile.write("@TYPE xy\n")
    ofile.write("@ title \"t-SNE embeddings of trajectory\"\n")
    for j in range(ncomp):
      ofile.write("@ xaxis  label \"low-dimensional embedding %i\"\n" % (j+1))
    for i in range(trajsize[0]):
      for j in range(ncomp):
        ofile.write("%f " % embeddings[i,j])
      ofile.write("\n")
    ofile.close()
  else:
    ofile = open(out, "w")
    for i in range(trajsize[0]):
      for j in range(ncomp):
        ofile.write("%f " % embeddings[i,j])
      ofile.write("\n")
    ofile.close()

  return embeddings, kldivedgence

