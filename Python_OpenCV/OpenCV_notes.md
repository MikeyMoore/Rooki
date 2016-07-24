##OpenCV process

* in terminal: brew update
* in terminal: brew install python
* Go into your ~/.bash_profile and change Homebrew's export path to: export PATH=/usr/local/bin:$PATH
* Reload your bash profile with: source ~/.bash_profile
* Sanity check: type "which python" into your terminal, if you did it right it should say /usr/local/bin/python
* in terminal: pip install virtualenv virtualenvwrapper
* Append this line to that same spot in your homebrew bash profile: "source /usr/local/bin/virtualenvwrapper.sh", then reload your bash profile
* in terminal: mkvirtualenv cv
* in terminal: pip install numpy
* in terminal: brew install cmake pkg-config
* in terminal: brew install jpeg libpng libtiff openexr
* in terminal: brew install eigen tbb
* in terminal: cd ~
* in terminal: git clone https://github.com/Itseez/opencv.git
* in terminal: cd opencv
* in terminal: git checkout 3.1.0
* in terminal: cd ~
* in terminal: git clone https://github.com/Itseez/opencv_contrib
* in terminal: cd opencv_contrib
* in terminal: git checkout 3.1.0
* in terminal: cd ~/opencv
* in terminal: mkdir build
* in terminal: cd build
* in terminal: cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local \
	-D PYTHON2_PACKAGES_PATH=~/.virtualenvs/cv/lib/python2.7/site-packages \
	-D PYTHON2_LIBRARY=/usr/local/Cellar/python/2.7.10/Frameworks/Python.framework/Versions/2.7/bin \
	-D PYTHON2_INCLUDE_DIR=/usr/local/Frameworks/Python.framework/Headers \
	-D INSTALL_C_EXAMPLES=OFF -D INSTALL_PYTHON_EXAMPLES=ON \
	-D BUILD_EXAMPLES=ON \
	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules ..
* in terminal: make -j4
* in terminal: make install
* If the last step doesn't work (privilege error), do: sudo make install
* Sanity check: in terminal, do: cd ~/.virtualenvs/cv/lib/python2.7/site-packages/
then: ls -l cv2.so 
and something like this should appear: -rwxr-xr-x  1 root  staff   2.2M Jul 22 11:51 cv2.so


* in terminal: pip install imutils
* in terminal: pip install image
