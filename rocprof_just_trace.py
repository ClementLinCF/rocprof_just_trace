import os
import random
import subprocess
import shutil

def main():
    temp_dir = os.path.join(os.getcwd(), "temp_" + str(random.randint(1000000000, 9999999999)))

    os.makedirs(temp_dir, exist_ok=True)

    shutil.copy("omp_stream", os.path.join(temp_dir, "omp_stream"))
    
    os.chdir(temp_dir)

    subprocess.run(["rocprof", "--sys-trace", "--hip-trace", "-d", temp_dir, "-o", "results.csv", "--timestamp", "on", "--obj-tracking", "on", "./omp_stream"])

    subprocess.run(["git", "clone", "https://github.com/chun-wan/ROCPROF_FILTER"])

    os.chdir("ROCPROF_FILTER")

    shutil.copy("../results.json", ".")

    subprocess.run(["python3", "hsa.py"])

    shutil.copy("combine.json", "../../")

    shutil.rmtree(temp_dir)

if __name__ == "__main__":
    main()


