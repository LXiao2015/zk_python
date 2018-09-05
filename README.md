Make sure that you have installed zookeeper for c.
First download from the official website https://mirrors.tuna.tsinghua.edu.cn/apache/zookeeper/.
Then install it.
```
cd src/c
./configure
make
make install
```

Then install zkpython.
```
wget --no-check-certificate http://pypi.python.org/packages/source/z/zkpython/zkpython-0.4.tar.gz
tar -zxvf zkpython-0.4.tar.gz
cd zkpython-0.4
sudo python setup.py install
```
Error may occurs noting that it can't find 'zookeeper.h',
you can modify the path wrritten in 'setup.py' to your zookeeper installation path.
```
include_dirs=["/usr/local/include/zookeeper"]
```
