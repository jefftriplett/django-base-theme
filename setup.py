import os
from setuptools import setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='base_theme',
    version='1.0',
    packages=['base_theme'],
    package_data={'base_theme': [
        'templates/*.html',
        'templates/your_app/*.html',
        'static/base_theme/bootstrap_css/*.css',
        'static/base_theme/fonts/*.*',
        'static/base_theme/fonts/fa/*.*',
        'static/base_theme/fonts/*.min.*',
        'static/base_theme/fonts/bask/*.*',
        'static/base_theme/fonts/lato/*.*',
        'static/base_theme/fonts/lus/*.*',
        'static/base_theme/fonts/mont/*.*',
        'static/base_theme/img/bg/*.*',
        'static/base_theme/img/footer/*.png',
        'static/base_theme/img/logo/*.png',
        'static/base_theme/img/social/*.png',
        'static/base_theme/js/*.js',
        'static/base_theme/js/vendor/*.js',
        'static/base_theme/scss/compiled_css/*.css',
        'static/base_theme/scss/scss/*.scss',
        'static/base_theme/scss/scss/base/*.scss',
        'static/base_theme/scss/scss/components/*.scss',
        'static/base_theme/scss/scss/helpers/*.scss',
        'static/base_theme/scss/scss/layout/*.scss',
        'static/base_theme/scss/scss/layout/header/*.scss',
        'static/base_theme/*.*',
        'static/base_theme/scss/config.rb',
    ]},
    include_package_data=True,
    license='BSD License',
    description="A responsive base theme for Wharton Django applications.",
    url='https://github.com/wharton/django-base-theme/',
    author='Chad Whitman, the Wharton School',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
