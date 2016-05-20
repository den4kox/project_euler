import os
import sys
import time


def writeResult(func):
    file_path = sys.argv[0]

    def wraper(*args, **kwargs):
        start = time.time()
        r = "## result: " + str(func(*args, **kwargs))
        time_result = ". Time: " + str(time.time() - start)
        with open(file_path) as f:
            content = f.readlines()
        if "## result:" in content[-1]:
            print("rewrite")
            content[-1] = r + str(time_result)

            with open(file_path, 'w') as file:
                file.writelines(content)
        else:
            print("Write")
            with open(file_path, "a") as myfile:
                myfile.write('\n' + r + str(time_result))

    return wraper
