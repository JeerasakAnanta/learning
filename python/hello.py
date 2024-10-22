import subprocess as process
import time


def main():
    print("------------- start --------------------")

    process.run(["ls", "-al"])

    print("sleep  ")
    time.sleep(1)

    process.run("htop")

    time.sleep(1)
    # heloworld ;)

    print("------------- Done --------------------")

    for i in range(100):
        print(i)


if __name__ == "__main__":
    main()
