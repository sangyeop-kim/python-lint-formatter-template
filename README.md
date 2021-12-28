  <br>

## formatter

we use **black**

```shell
pip install black
```

<br>
  
## linter
we use **pylint**
```shell
pip install pylint
```
configure file
- .pylintrc

<br>

## type checker

https://stackoverflow.com/questions/17493159/should-i-force-python-type-checking
https://stackoverflow.com/questions/44783872/how-to-force-static-typing-in-python

Although it is not recommended to enforce the type in python, we decided to recommend writing the type for code modification and sharing.<br>
<br>
we use<br>

**mypy**

```shell
pip install mypy
```

configure file

- mypy.ini

<br>

**pylance**

If you use pylance, one of the vscode extensions, you can prevent warnings from mypy test in advance.
