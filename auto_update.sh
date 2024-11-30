
PROJECTS=(
    "libraries/bzlmodRio-ni"
    "libraries/bzlmodRio-opencv"
    
    "rules/rules_bzlmodrio_toolchains"
    "rules/rules_bzlmodrio_jdk"
)

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )


for project in "${PROJECTS[@]}"; do   
    GENERATION_DIR=$SCRIPT_DIR/$project/generate
    echo "Generating $project"
    cd $GENERATION_DIR
    bazel run //:auto_update
    bazel shutdown
done