import typer
from ssg.site import Site

def main(source = "content", dest = "dist"):
    config = {}
    config.update({"source": source, "dest": dest})
    site = Site(**config).build()

typer.run(main)