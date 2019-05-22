## First attempt to run the blast example using cwl and charliecloud
 This example is a serial workflow, will need to explore using scatter or some other
 way of parallellizing the workflow.

### To set up environment named cwl (you can choose any name you wish):

```sh
module load anaconda/Anaconda2
conda create -n cwl python=2.7 pip
source activate cwl
pip install cwlref-runner
pip install cwltool
```
### Also need to have NodeJS in your path:

```sh
cd $HOME/src # locations where you want NodeJS
wget https://nodejs.org/dist/v10.15.1/node-v10.15.1-linux-x64.tar.xz
tar xf node-v10.15.1-linux-x64.tar.xz
export NODEJS_HOME=$HOME/src/tmp/node-v10.15.1-linux-x64/bin
export PATH=$NODEJS_HOME:$PATH
node --version
```
### To use the environment in another session:
Note: don't run on front end

```sh
LANG=C salloc -p galton # (LANG=C prevents warnings from blast cat)
module load anaconda/Anaconda2 charliecloud
source activate cwl
export NODEJS_HOME=$HOME/src/node-v10.15.1-linux-x64/bin #use your location
export PATH=$NODEJS_HOME:$PATH
```

### To run the workflow:

```sh
cwl-runner blast-cc-flow.cwl cc-blast.yml
```
### To deactivate the environment when finished:

```sh
source deactivate
```

