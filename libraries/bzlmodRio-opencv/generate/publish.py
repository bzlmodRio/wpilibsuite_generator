import os
from get_opencv_dependencies import get_opencv_dependencies
from bazelrio_gentool.publish_module import publish_module
from bazelrio_gentool.utils import TEMPLATE_BASE_DIR


def main():
    SCRIPT_DIR = os.environ["BUILD_WORKSPACE_DIRECTORY"]
    registry_location = os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..", "bazel-central-registry"
    )

    group = get_opencv_dependencies()

    module_template = os.path.join(
        TEMPLATE_BASE_DIR, "library_wrapper", "MODULE.bazel.jinja2"
    )

    os.chdir(SCRIPT_DIR)
    publish_module(
        registry_location,
        group,
        module_json_template=None,
        module_template=module_template,
    )


if __name__ == "__main__":
    """
    bazel run //:publish
    """
    main()
