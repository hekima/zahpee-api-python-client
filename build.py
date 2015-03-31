from pybuilder.core import init, use_plugin, task, depends, description


# Core build plugins
use_plugin("python.core")
use_plugin("python.distutils")
use_plugin("python.install_dependencies")
use_plugin("exec")

# Testing plugins
use_plugin("python.unittest")
use_plugin("python.integrationtest")
use_plugin("python.coverage")
use_plugin("python.pytddmon")

# Linting plugins
use_plugin("python.frosted")
use_plugin("python.flake8")
# use_plugin("python.pychecker")
# use_plugin("python.pylint")

# IDE plugins
use_plugin("python.pydev")
use_plugin("python.pycharm")

default_task = "publish"


@init
def initialize(project):
    project.name = 'zahpeeapi'
    project.version = '0.0.14'
    project.summary = 'The Zahpee API Python client'
    project.description = 'The Zahpee API Python client'
    project.url= 'https://github.com/zahpee/zahpee-api-python-client'

    # Build dependencies
    project.build_depends_on('pytest')
    project.build_depends_on('mockito-without-hardcoded-distribute-version')

    # Core Configuration
    project.set_property('dir_dist', '$dir_target/dist/zahpeeapi')

    # Flake8 Configuration
    project.set_property('flake8_break_build', True)
    project.set_property('flake8_include_test_sources', True)
    project.set_property('flake8_max_line_length', 120)

    project.set_property('coverage_break_build', False)

    # flake8_include_test_source Integration test Configuration
    project.set_property('integrationtest_additional_commandline', '--with-xunit')
    project.set_property('integrationtest_parallel', True)

    project.set_property('clean_propagate_stdout', True)
    project.set_property('clean_propagate_stderr', True)

    project.set_property('coverage_threshold_warn', 80)
