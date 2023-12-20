import datetime
import subprocess


def newid():
    now = datetime.datetime.now()
    timestamp = now.strftime('%Y%m%d%H%M%S')

    return '{:x}'.format(int(timestamp))


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
