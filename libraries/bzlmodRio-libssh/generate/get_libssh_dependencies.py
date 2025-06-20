from bazelrio_gentool.deps.dependency_container import DependencyContainer


def _default_native_static_platforms():
    platforms = [
        "linuxarm32",
        "linuxarm64",
        "linuxx86-64",
        "osxuniversal",
        "windowsx86-64",
        "windowsx86",
        "windowsarm64",
    ]
    return [x + "static" for x in platforms] + [x + "staticdebug" for x in platforms]


def get_libssh_dependencies():
    year = "2024"
    version = "0.105-1"

    group_id = f"edu.wpi.first.thirdparty.frc{year}"

    group = DependencyContainer(
        "bzlmodrio-libssh", version, year, "https://frcmaven.wpi.edu/release"
    )
    group.create_cc_dependency(
        f"libssh",
        parent_folder="libssh",
        group_id=group_id,
        headers="headers",
        sources="sources",
        resources=_default_native_static_platforms(),
        has_jni=False,
    )
    group.sanitized_version = year + "." + group.sanitized_version

    return group


if __name__ == "__main__":
    get_opencv_dependencies()
