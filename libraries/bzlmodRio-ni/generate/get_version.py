from get_ni_dependencies import get_ni_dependencies


def main():
    group = get_ni_dependencies()
    print(group.version)


if __name__ == "__main__":
    main()
