# following http://wiki.blender.org/index.php/Dev:2.5/Doc/Building_Blender/Git

#still need svn installed on the system even to do a git checkout
sudo apt-get install subversion build-essential
#help also creates an empty ~/.subversion dir and config files on first call 
svn help
sudo apt-get install git-core git-svn


# to avoid first time certificate warning
# this will need to be done per user
echo ssl-trust-default-ca = no >> ~/.subversion

#setup directory structure in version controlled projects vcp
BLENDER_ROOT=~/vcp/git/blender/blender-trunk
mkdir -p $BLENDER_ROOT
cd $BLENDER_ROOT

# get a git clone of the svn repo starting at rev 57064
#TODO fix this to be for the last 5 revisions
git svn clone -r57064 https://svn.blender.org/svnroot/bf-blender/trunk/blender/
#y 
git svn rebase

./blender/build_files/build_environment/install_deps.sh --with-osl

#install cmake
sudo apt-get install cmake cmake-curses-gui

cd $BLENDER_ROOT/blender
make
cd ../build_linux
make install

# get some svn externals that git can't reach to release/scripts/addons
#git svn clone -r4550 https://svn.blender.org/svnroot/bf-extensions/trunk/py/scripts/
# clone (only back to revision 4550) into an svn directory tree separate from the git
BF_EXTENSIONS_SCRIPTS_ROOT = ~/vcp/svn/blender/bf-extensions/trunk/py
mkdir -p  $BF_EXTENSIONS_SCRIPTS_ROOT
cd $BF_EXTENSIONS_SCRIPTS_ROOT
svn co -r4550 https://svn.blender.org/svnroot/bf-extensions/trunk/py/scripts/
cd scripts 
svn up

# make a symlink so the files are in the expected main tree
ln -s $BF_EXTENSIONS_SCRIPTS_ROOT/scripts $BLENDER_ROOT/blender/bf-extensions/trunk/py/scripts

# same with locale for internationalization
BR_TRANSLATIONS_ROOT=~/vcp/svn/blender/bf-translations
mkdir -p $BF_TRANSLATIONS_ROOT
cd $BF_TRANSLATIONS
git svn clone -r1940 https://svn.blender.org/svnroot/bf-translations/trunk/
ln -s $BF_TRANSLATIONS_ROOT/locale ~/vcp/git/blender/blender-trunk/blender/release/datafiles/locale 

# to get the latest
cd $BENDER_ROOT/blender
git svn fetch

