import argparse
import sys
import os

DEFAULT_JAVA_VERSION = 8
DEFAULT_FILE_NAME = "Dockerfile"

def abort_script(reason):
    print reason
    sys.exit()

def process_args():
    # Initialize all of the argument parser logic
    parser = argparse.ArgumentParser()
    parser.add_argument("--jar", help="JAR file we are creating the docker image for. Required to provide this", type=str)
    parser.add_argument("--port", help="Host machine port the docker image will be exposed on. Required to provide this", type=int)
    parser.add_argument("--java-version", help="Version of java to use for the docker image", type=int)
    parser.add_argument("--output", help="Output directory to write the resulting file to", type=str)
    args = parser.parse_args()

    port = args.port
    jar = args.jar
    java_version = args.java_version if args.java_version is not None else DEFAULT_JAVA_VERSION
    output = args.output

    # Validate the various inputs
    if port is None or (port > 65536 or port < 1):
        abort_script("Must provide a valid port in order to generate the final docker file")

    if jar is None or not jar.endswith(".jar"):
        abort_script("Must provide the JAR file to use for generating the final docker file")

    # Create the docker file
    create_file(jar, port, java_version, output)

def create_file(jar, port, java_version, output=""):
    with open(DEFAULT_FILE_NAME, "w") as file:

        # clear file contents (in case file already existed?)
        file.seek(0)
        file.truncate()

        # write new contents to file
        file.write("FROM java:" + str(java_version) + "\n")
        file.write("VOLUME /tmp\n")
        file.write("ADD " + jar + " app.jar\n")
        file.write("RUN bash -c 'touch /app.jar'\n")
        file.write("EXPOSE " + str(port) + "\n")
        file.write("ENTRYPOINT [\"java\",\"-Djava.security.egd=file:/dev/./urandom\",\"-jar\",\"/app.jar\"]\n")

        file.close()

    if output is not None:
        os.rename(DEFAULT_FILE_NAME, output + "/" + DEFAULT_FILE_NAME)

# Entry point for the application script
if __name__ == "__main__":
    process_args()