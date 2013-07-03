# ECLIPSE_INSTALL

sudo cd /opt
sudo mkdir eclipse-installs
cd eclipse-installs

#eclipse-mobile
sudo mkdir /opt/eclipse-installs/mobile
cd /opt/eclipse-installs/mobile
sudo wget
http://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/juno/SR2/eclipse-mobile-juno-SR2-linux-gtk-x86_64.tar.gz&mirror_id=337
  eclipse-mobile-juno-SR2-linux-gtk-x86_64.tar.gz
#md5
1743f7a3c772a2c21393cba5c34847ff
tar -zxvf eclipse-mobile-juno-SR2-linux-gtk-x86_64.tar.gz

#eclipse-cdt
sudo mkdir /opt/eclipse-installs/cdt
cd /opt/eclipse-installs/cdt
sudo wget http://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/juno/SR2/eclipse-cpp-juno-SR2-linux-gtk-x86_64.tar.gz&mirror_id=272

#http://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/juno/SR2/eclipse-mobile-juno-SR2-linux-gtk-x86_64.tar.gz&mirror_id=1065

 eclipse-cpp-juno-SR2-linux-gtk-x86_64.tar.gz
#md5
f91f412bc322f67d60d1b6e1130a88aa 
tar -zxvf eclipse-cpp-juno-SR2-linux-gtk-x86_64.tar.gz

# eclipse-web
sudo mkdir /opt/eclipse-installs/web
cd /opt/eclipse-installs/web
sudo wget http://www.eclipse.org/downloads/download.php?file=/eclipse/downloads/drops4/R-4.2.2-201302041200/eclipse-SDK-4.2.2-linux-gtk-x86_64.tar.gz&mirror_id=346
# wait
sudo mv *.tar.gz eclipse-web.tar.gz
sudo tar -zxvf eclipse-web.tar.gz

#adt
#http://developer.android.com/sdk/index.html#download also has a guard preventing wget
sudo mkdir /opt/eclipse-installs/adt
sudo unzip .zipfile
sudo chown -R kesten:kesten .
sudo find /opt/eclipse-installs/adt/ -type d -exec chmod 755 {} \;
sudo find /opt/eclipse-installs/adt/ -type f -exec chmod 644 {} \;
cd /opt/eclipse-installs/adt/adt-bundle-linux-x86_64-20130522/sdk/platform-tools$
chmod ug+x adb fastboot
cd /opt/eclipse-installs/adt/adt-bundle-linux-x86_64-20130522/sdk/tools 
chmod ug+x *
# brittle.  remove executable flag from text files
chmod ug-x *.*
cd /opt/eclipse-installs/adt/adt-bundle-linux-x86_64-20130522/sdk/build-tools/android-4.2.2
chmod ug+x *
chmod ug-x *.*
sudo apt-get install ia32-libs

# add to .bashrc      ADT
ECLIPSE_ADT_HOME=/opt/eclipse-installs/adt/adt-bundle-linux-x86_64-20130522/eclipse
ANDROID_SDK_HOME=/opt/eclipse-installs/adt/adt-bundle-linux-x86_64-20130522/sdk
export PATH=${ECLIPSE_ADT_HOME}:$PATH
export PATH=${ANDROID_SDK_HOME}/platform-tools:$PATH
export PATH=${ANDROID_SDK_HOME}/tools:$PATH
export SDK_HOME=${ANDROID_SDK_HOME}
export ECLIPSE_HOME=${ECLIPSE_ADT_HOME}


#eclipse maven from marketplace, plus m2-subclipse adapter and subclipse
sudo add-apt-repository ppa:dominik-stadler/subversion-1.7
sudo apt-get update
sudo apt-get install libsvn-java
# add -Djava.library.path=/usr/lib/x86_64-linux-gnu/jni bewlow -vmargs in eclipse.ini



