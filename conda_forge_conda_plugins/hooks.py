from conda.plugins import hookimpl, CondaSubcommand


@hookimpl
def conda_subcommands():
    def hello_conda(args):
        print("Hello conda!")

    yield CondaSubcommand(
        name="hello",
        action=hello_conda,
        summary="Command that prints \"Hello conda!\""
    )
