from bazelrio_gentool.deps.sha256_helper import get_hash


def get_toolchain_dependencies():
    class PlatformConfig:
        def __init__(
            self, repo_os, repo_cpu, platforms_os, platforms_cpu, strip_prefix, suffix
        ):
            self.repo_os = repo_os
            self.repo_cpu = repo_cpu
            self.platforms_os = platforms_os
            self.platforms_cpu = platforms_cpu
            self.strip_prefix = strip_prefix
            self.suffix = suffix

        def get_sha256(self):
            return get_hash(self.get_url(), fail_on_miss=True)

        def get_url(self):
            return f"https://github.com/adoptium/temurin17-binaries/releases/download/jdk-{escaped_version}/OpenJDK17U-jdk_{self.repo_cpu}_{self.repo_os}_hotspot_{underscore_version}.{self.suffix}"

    class JavaToolchainConfig:
        def __init__(
            self,
            repo_name,
            platforms,
            jdk_version,
            escaped_version,
            underscore_version,
            jre_version,
            patch="",
        ):
            self.repo_name = repo_name
            self.platforms = platforms
            self.jdk_version = jdk_version
            self.escaped_version = escaped_version
            self.underscore_version = underscore_version
            self.jre_version = jre_version
            self.version = jdk_version
            self.sanitized_version = self.version.replace("+", "-")
            self.patch = patch
            self.year = "2024"

    platforms = []

    jdk_version = "17.0.8.1+1"
    underscore_version = jdk_version.replace("+", "_")
    escaped_version = jdk_version.replace("+", "%2B")

    platforms.append(
        PlatformConfig(
            repo_os="linux",
            repo_cpu="x64",
            platforms_os="linux",
            platforms_cpu="x86_64",
            strip_prefix="jdk-" + jdk_version,
            suffix="tar.gz",
        )
    )
    platforms.append(
        PlatformConfig(
            repo_os="linux",
            repo_cpu="aarch64",
            platforms_os="linux",
            platforms_cpu="armv7",
            strip_prefix="jdk-" + jdk_version,
            suffix="tar.gz",
        )
    )
    platforms.append(
        PlatformConfig(
            repo_os="mac",
            repo_cpu="x64",
            platforms_os="macos",
            platforms_cpu="x86_64",
            strip_prefix="jdk-" + jdk_version + "/Contents/Home",
            suffix="tar.gz",
        )
    )
    platforms.append(
        PlatformConfig(
            repo_os="mac",
            repo_cpu="aarch64",
            platforms_os="macos",
            platforms_cpu="aarch64",
            strip_prefix="jdk-" + jdk_version + "/Contents/Home",
            suffix="tar.gz",
        )
    )
    platforms.append(
        PlatformConfig(
            repo_os="windows",
            repo_cpu="x64",
            platforms_os="windows",
            platforms_cpu=None,
            strip_prefix="jdk-" + jdk_version,
            suffix="zip",
        )
    )

    output = JavaToolchainConfig(
        repo_name="rules_bzlmodrio_jdk",
        platforms=platforms,
        jdk_version=jdk_version,
        escaped_version=escaped_version,
        underscore_version=underscore_version,
        jre_version=17,
    )

    return output
