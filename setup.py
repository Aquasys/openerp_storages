from setuptools import setup, find_packages
from glob import glob


MODULE_NAME = 'openerp_storages'

#REQUIRES = ['-e git+ssh://aquasys/lettuce_terrain@v0.1.4#egg=lettuce_terrain']

META_DATA = dict(
    name='openerp_storages',
    version='0.0,.0',
    description='Storages module for OpenERP',
    author='Aquasys G.K.',

    keywords='openerp storages',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    #install_requires=REQUIRES,
    packages=['external_storage_openerp'],
    include_package_data=True,
    zip_safe=False,
    scripts = []
)

if __name__ == '__main__':
    setup(**META_DATA)
