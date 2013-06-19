from setuptools import setup, find_packages

version = '1.1.dev0'

setup(name='policy.ces',
      version=version,
      description="policy of ces site",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='https://github.com/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['policy'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'Products.LinguaPlone',
          'cirb.zopemonitoring',
          # -*- Extra requirements: -*-
          'collective.easyslider',
          'Products.Collage',
          'collective.collage.portlets',
          'qi.portlet.TagClouds',
          'quintagroup.analytics',
          'plone.app.ldap',
          'Products.CMFSquidTool',
          'plonetheme.ces',

      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
