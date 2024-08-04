# shutil 包

- `copyfile(src, dst, *, follow_symlinks=True) -> _StrOrBytePathT`: 将文件从src复制到dst。如果dst已经存在，则会被覆盖。
- `copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False)  -> Any`: 将整个目录树从src复制到dst。如果dst已经存在，则会被覆盖。
