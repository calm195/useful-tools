# os 包

常用方法：

- `os.getCmd() -> str`: 获取当前目录
- `os.listdir(path: str) -> List[str]`: 获取目录下所有文件和文件夹，如果 path 为空，则获取当前目录下所有文件和文件夹
- `os.walk(path: str) -> Iterator[Tuple[str, List[str], List[str]]`: 遍历目录下所有文件和文件夹，返回一个迭代器，每次迭代返回一个元组，元组的第一个元素是当前目录，第二个元素是当前目录下所有文件夹，第三个元素是当前目录下所有文件
- `os.path.exists(path: str) -> bool`: 判断文件或目录是否存在
- `os.mkdir(path: str, exist_ok: bool = False) -> None`: 创建单层目录，如果文件夹已经存在则会报错，如果 exist_ok 为 True，则不会抛出异常
- `os.makedirs(path: str, exist_ok: bool = False) -> None`: 递归创建目录，如果文件夹已经存在则会报错，如果 exist_ok 为 True，则不会抛出异常
- `os.rmdir(path: str) -> None`: 删除目录，只能删除空文件夹，非空会报错
- `os.path.join(*paths: str) -> str`: 拼接路径，将两个路径拼接在一起
- `os.path.split(path: str) -> Tuple[str, str]`: 分割路径，返回一个元组，第一个元素是目录，第二个元素是文件名
- `os.path.dirname(path: str) -> str`: 获取绝对路径，不含文件名
- `os.path.basename(path: str) -> str`: 获取文件名，不含路径
- `os.path.isfile(path: str) -> bool`: 判断是否是文件
- `os.path.isdir(path: str) -> bool`: 判断是否是目录
- `os.path.getsize(path: str) -> int`: 获取文件大小
- `os.sep -> str`: 获取当前系统的路径分隔符
