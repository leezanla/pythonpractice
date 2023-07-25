
# 第一种方式：导入自定义包中的模块，并使用
import my_package.my_module1
import my_package.my_module2
my_package.my_module1.module1_test()
my_package.my_module2.module2_test()

# 第二种方式
from my_package import my_module1
from my_package import my_module2
my_module1.module1_test()
my_module2.module2_test()

# 第三种方式
from my_package.my_module1 import module1_test
from my_package.my_module2 import module2_test
module1_test()
module2_test()
















