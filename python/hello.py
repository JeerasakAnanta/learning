import subprocess as process
import time


def main():
    print("------------- start --------------------")

    process.run(["ls", "-al"])

    print("sleep  ")
    time.sleep(1)

    process.run("htop")

    time.sleep(1)
    print("------------- Done --------------------")


if __name__ == "__main__":
    main()
