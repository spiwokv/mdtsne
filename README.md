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

For other options see `mdtsne -h`.


