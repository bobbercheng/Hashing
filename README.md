Why I write this python module?

I try to do some experience in python but I cannot find SHA256 libary equivalent to Guava - Google Core Libraries for Java, refer to https://github.com/google/guava/blob/master/guava/src/com/google/common/hash/Hashing.java. So I decided to write my own SHA256 libary.

How to use it?
```
pip install git+https://github.com/bobbercheng/Hashing.git
```

```
from hashing import Hashing
hash_int = Hashing.sha256_int("Hello, World!")
```
