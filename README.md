# Rad registry

Radicle is a p2p code collaboration stack. It doesn't yet have a registry - a
place where people can list their projects. Thankfully it's easy to add your
own functionality, so let's do that!

The idea is that this repository can server as a tutorial for how to build your
own machines.

A "machine", in the Radicle terminology, is not a physical computer, but a
little program that anyone can interact with. A little like a REPL, but
collaborative. A little like a server, but p2p.

## Layout

`registry.rad` is a file written in the Radicle language that defines our
machine.

`registry.py` is a Python program that provides a CLI tool for the basic
registry operations - adding a project to the registry, and staring a project.
We could have used any other language besides Python here (including Radicle).

## Using

Install [Radicle](https://radicle.xyz/docs/index.html#installation-setup).
Make sure the Radicle daemons are running. If you installed from source, that's:

```
rad daemon-ipfs
rad daemon-radicle
```

Then run `./registry.py --help` for usage.
