# pypi_test
Packaging Python Projects tutorial 

# [learning sourse](https://packaging.python.org/tutorials/packaging-projects/?tdsourcetag=s_pctim_aiomsg)

# 1. install the necessary build/install package / 安装需要编译的包
```
    $　python3 -m pip install --user --upgrade setuptools wheel
```
# 2. build the package /构建程序包
```
    $ python3 setup.py sdist bdist_wheel
```
# 3.enter into the root of project and run the follow command to install this project into your local python environment / 本地安装,可以全局使用
```
    $ pip install -e .

```
# 4 useing for 2 way
- command way:
    ```
     $ test1
    ```
    You can enter the command interactive mode to use as in python interactive mode
- python Module
    ```
        >>> import pypi_test
        >>> pypi_test.name
        'tes2234'
    ```