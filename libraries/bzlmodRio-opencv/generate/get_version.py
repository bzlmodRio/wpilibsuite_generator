from get_opencv_dependencies import get_opencv_dependencies


def main():
    group = get_opencv_dependencies()
    print(group.year + "." + group.version)


if __name__ == "__main__":
    main()
