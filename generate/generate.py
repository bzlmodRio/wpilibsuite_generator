from python.runfiles import runfiles
import subprocess

def main():
    
    r = runfiles.Create()
    generators = [
        r.Rlocation("bzlmodrio-ni-gentool+/generate"),
        r.Rlocation("bzlmodrio-opencv-gentool+/generate"),
        # r.Rlocation("rules_bzlmodrio_toolchains-gentool+/generate"),
        # r.Rlocation("rules_bzlmodrio_jdk-gentool+/generate"),
    ]

    for gen in generators:
        print(gen)
        subprocess.check_call([gen])

if __name__ == "__main__":
    main()