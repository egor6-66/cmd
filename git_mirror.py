import os, stat, shutil

from_where = ''
to_where = ''
dir_name = from_where.split('/')[-1]


def remove_readonly(fn, path, _):
    try:
        os.chmod(path, stat.S_IWRITE)
        fn(path)
    except Exception as exc:
        print("Skipped:", path, "because:\n", exc)


def check_dir_and_delete(): 
    check_dir = os.path.isdir(dir_name)
    print(check_dir)
    if check_dir:
        shutil.rmtree(dir_name, onerror=remove_readonly)


check_dir_and_delete()
os.system("git clone --mirror " + from_where)
os.chdir(dir_name)
os.system("git remote add new " + to_where)
os.system("git push --mirror new")

os.chdir('..')
check_dir_and_delete()
