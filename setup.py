"""
Package setup for the minirhizpreprocessing module.
"""
import os
import textwrap

from setuptools import find_packages, setup


def node_and_dirty_tag_scheme(version):
	"""Keep the hash when distance with the dirty tag local scheme."""
	if version.exact or version.node is None:
		return version.format_choice('', '+dirty')

	return version.format_choice('+{node}', '+{node}.dirty')

def parse_git_describe_string(_root, config=None):
	"""
	Return a setuptools_scm parsed version from a Git describe string found in the environment
	variable GIT_DESCRIBE_STRING.

	:param str _root: Relative path to cwd, used for finding the scm root.
	:param setuptools_scm.config.Configuration config: Configuration instance.
	:return: Parsed version or ``None``.
	:rtype: setuptools_scm.version.ScmVersion
	"""
	# pylint: disable=import-error
	# Those imports are only available at install time
	from setuptools_scm.git import _git_parse_describe
	from setuptools_scm.version import meta

	git_describe = os.environ.get('GIT_DESCRIBE_STRING')
	if not git_describe:
		return None

	tag, number, node, dirty = _git_parse_describe(git_describe)
	kwargs = {'distance': number} if number else {}
	return meta(tag, dirty=dirty, node=node, config=config, **kwargs)


VERSION_CONFIG = {
	'fallback_version': '0.0.0+scm.missing',
	'local_scheme': node_and_dirty_tag_scheme,
	'write_to': 'src/minirhizpreprocessing/version.py',
	'write_to_template': textwrap.dedent('''\
		"""
		File generated by setuptools_scm.
		Do not track in version control.
		"""
		__version__ = {version!r}
		''')
	}
# Add a custom function to parse the result of a git describe command from an environment
# variable, this is useful when the git history is not available at build time.
if 'GIT_DESCRIBE_STRING' in os.environ:
	VERSION_CONFIG['parse'] = parse_git_describe_string

# Main package setup configuration
# See also setup.cfg
SETUP_PARAMS = dict(
	use_scm_version=VERSION_CONFIG,
	packages=find_packages('src'),
	package_dir={'': 'src'}
	)


if __name__ == '__main__':
	setup(**SETUP_PARAMS)
