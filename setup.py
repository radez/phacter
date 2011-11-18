#!/usr/bin/env python
"""
Standard build script.
"""

__docformat__ = 'restructuredtext'


import os
import sys

from setuptools import Command, setup#, find_packages, findall

sys.path.insert(0, 'src')

from phacter import __version__, __license__, __author__


class SetupBuildCommand(Command):
    """
    Master setup build command to subclass from.
    """

    user_options = []

    def initialize_options(self):
        """
        Setup the current dir.
        """
        self._dir = os.getcwd()

    def finalize_options(self):
        """
        No clue ... but it's required.
        """
        pass


try:
    from sphinx import setup_command

    class SphinxCommand(setup_command.BuildDoc):
        """
        Wrapper for the sphinx setup command.
        """

        def __init__(self, dist):
            """
            Overrides some settings before run.
            """
            setup_command.BuildDoc.__init__(self, dist)
            if not os.path.exists('dist'):
                os.mkdir('dist')
            if not os.path.exists(os.path.join('dist', 'html')):
                os.mkdir(os.path.join('dist', 'html'))
            self.source_dir = 'docs'
            self.build_dir = os.path.join('dist', 'html')

except ImportError, ie:

    class SphinxCommand(SetupBuildCommand):
        """
        Dummy 'you don't have sphinx' command/
        """

        def __init__(self, dist):
            """
            Prints out the error info and exits.
            """
            sys.stderr.write("You don't seem to have the following which\n")
            sys.stderr.write("are required to make documentation:\n\n")
            sys.stderr.write("\tsphinx.setup_command\n")
            raise SystemExit(1)


class RPMBuildCommand(SetupBuildCommand):
    """
    Creates an RPM based off spec files.
    """

    description = "Build an rpm based off of the top level spec file(s)"

    def run(self):
        """
        Run the RPMBuildCommand.
        """
        try:
            if os.system('./setup.py sdist'):
                raise Exception("Couldn't call ./setup.py sdist!")
                sys.exit(1)
            if not os.access('dist/rpms/', os.F_OK):
                os.mkdir('dist/rpms/')
            dist_dir = os.path.join(os.getcwd(), 'dist')
            rpm_cmd = 'rpmbuild -ba --clean \
                                    --define "_rpmdir %s/rpms/" \
                                    --define "_srcrpmdir %s/rpms/" \
                                    --define "_sourcedir %s" *spec' % (
                      dist_dir, dist_dir, dist_dir)
            if os.system(rpm_cmd):
                raise Exception("Could not create the rpms!")
        except Exception, ex:
            sys.stderr.write(str(ex))


class TestCommand(SetupBuildCommand):
    """
    executes the unit tests
    """

    description = "run the unit tests"

    def run(self):
        pass


class ViewDocCommand(SetupBuildCommand):
    """
    Quick command to view generated docs.
    """

    def run(self):
        """
        Opens a webbrowser on docs/html/index.html
        """
        import webbrowser

        print("NOTE: If you have not created the docs first this will not be "
              "helpful. If you don't see any documentation in your browser "
              "run ./setup.py doc first.")
        if not webbrowser.open('docs/html/index.html'):
            sys.stderr.write("Could not open on your webbrowser.\n")


def get_sources(map_list):
    """
    Simple function to make it easy to get everything under a directory as
    a source list.

    :Parameters:
       - `src`: the location on the file system to use as a root.
       - `dst`: the target location to use as a root.
       - `recursive`: include subdirs.
    """
    file_list = []
    for map in map_list:
        dst, src, recursive = map
        for afile in os.listdir(src):
            this_dir_list = []
            full_path = os.path.join(src, afile)
            if os.path.isfile(full_path):
                this_dir_list.append(full_path)
            else:
                if recursive:
                    file_list.extend(
                        get_sources([
                            (os.path.join(dst, afile), full_path, recursive)]))
            file_list.append((dst, this_dir_list))
    return file_list


setup(
    name="python-phacter",
    version=__version__,
    description="A system facts tool",
    long_description="system facts toolon",
    author=__author__,
    author_email='dradez@redhat.com',
    #TODO: fix the url
    url="https://github.com/radez/phacter",
    platforms=['linux','darwin', 'windows'],

    license=__license__,

    classifiers=[
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python'],
    package_dir={'': 'src'},
    packages=['phacter', 'phacter.utils'],
    scripts=['bin/phacter'],
    #data_files=get_sources(
    #    [('lib/phacter', os.path.join('src', 'phacter'), True)]),
    zip_safe=False,
    cmdclass={'rpm': RPMBuildCommand,
              'doc': SphinxCommand,
              'viewdoc': ViewDocCommand,
              'test': TestCommand})
