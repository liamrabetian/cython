from datetime import datetime

import run_python
import run_cython

number = 1000000

start = datetime.now()
run_python.test(number)
end = datetime.now()

python_time = (end - start).total_seconds()

start = datetime.now()
run_cython.test(number)
end = datetime.now()

cython_time = (end - start).total_seconds()

print(f'python took {python_time} seconds')
print('-----------------------------------')
print(f'cython took {cython_time} seconds')
