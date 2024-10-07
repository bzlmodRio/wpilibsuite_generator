from bazelrio_gentool.deps.dependency_container import DependencyContainer


def _default_native_shared_platforms():
    return [
        "linuxarm32",
        "linuxarm64",
        "linuxx86-64",
        "osxarm64",
        "osxuniversal",
        "windowsx86-64",
        "windowsx86",
        "windowsarm64",
    ]


def _default_native_static_platforms():
    return [x + "static" for x in _default_native_shared_platforms()]


def _default_native_shared_debug_platforms():
    return [x + "debug" for x in _default_native_shared_platforms()]


def _default_native_static_debug_platforms():
    return [x + "staticdebug" for x in _default_native_shared_platforms()]


def _default_all_native_platforms():
    return (
        _default_native_shared_platforms()
        + _default_native_static_platforms()
        + _default_native_shared_debug_platforms()
        + _default_native_static_debug_platforms()
    )


def _default_all_platforms():
    return [
        "linuxathena",
        "linuxathenastatic",
        "linuxathenadebug",
        "linuxathenastaticdebug",
    ] + _default_all_native_platforms()


def get_opencv_dependencies():
    year = "2024"
    version = "4.8.0-4"
    patch = ".bcr1"

    group_id = f"edu.wpi.first.thirdparty.frc{year}.opencv"

    group = DependencyContainer(
        "bzlmodrio-opencv",
        version,
        year,
        "https://frcmaven.wpi.edu/release",
        patch=patch, organization="wpilibsuite",
    )
    group.create_cc_dependency(
        f"opencv-cpp",
        parent_folder="opencv",
        group_id=group_id,
        headers="headers",
        sources="sources",
        resources=_default_all_platforms(),
        has_jni=True,
        has_install_name_patches=False,
    )

    group.create_java_dependency(
        f"opencv-java",
        parent_folder="opencv",
        group_id=group_id,
        dependencies=["opencv-cpp"],
    )

    group.sanitized_version = year + "." + group.sanitized_version

    return group


if __name__ == "__main__":
    get_opencv_dependencies()
