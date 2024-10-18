from get_toolchain_dependencies import get_toolchain_dependencies


def main():
    print(get_toolchain_dependencies().sanitized_version)


if __name__ == "__main__":
    main()
