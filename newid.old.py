import hashlib
import datetime
import subprocess


def newid():
    now = datetime.datetime.now()
    timestamp = now.strftime('%Y%m%d%H%M%S')
    md5 = hashlib.md5(timestamp.encode('utf-8')).hexdigest()
    return md5


def main():
    id = newid()
    cmd = "npx qiita new %s" % id

    result = subprocess.run(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print(result.returncode)
    print(result.stdout)


if __name__ == "__main__":
    main()
