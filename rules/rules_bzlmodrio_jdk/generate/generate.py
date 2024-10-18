from bazelrio_gentool.clean_existing_version import clean_existing_version
from bazelrio_gentool.generate_shared_files import (
    write_shared_root_files,
    write_shared_test_files,
)
from bazelrio_gentool.utils import (
    TEMPLATE_BASE_DIR,
    write_file,
    render_template,
    render_templates,
)
from bazelrio_gentool.generate_module_project_files import (
    create_default_mandatory_settings,
)
from bazelrio_gentool.generate_shared_files import get_bazel_dependencies
from bazelrio_gentool.cli import add_generic_cli, GenericCliArgs
from get_toolchain_dependencies import get_toolchain_dependencies
import argparse
import os


def main():
    SCRIPT_DIR = os.environ["BUILD_WORKSPACE_DIRECTORY"]
    REPO_DIR = os.path.join(SCRIPT_DIR, "..")

    parser = argparse.ArgumentParser()
    add_generic_cli(parser)
    args = parser.parse_args()

    group = get_toolchain_dependencies()

    mandatory_dependencies = create_default_mandatory_settings(GenericCliArgs(args))

    write_shared_root_files(REPO_DIR, group)
    write_shared_test_files(REPO_DIR, group)

    template_files = [
        "maven_deps.bzl",
        "WORKSPACE",
        "MODULE.bazel",
        "tests/WORKSPACE",
        "tests/MODULE.bazel",
    ]

    render_templates(
        template_files,
        REPO_DIR,
        os.path.join(SCRIPT_DIR, "templates"),
        bazel_dependencies=get_bazel_dependencies(),
        mandatory_dependencies=mandatory_dependencies,
        group=group,
    )


if __name__ == "__main__":
    """
    bazel run //:generate
    """
    main()
