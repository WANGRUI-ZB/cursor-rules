from setuptools import setup, find_packages
import switch_rules.cursor_rules as cursor_rules

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='cursor_rules',
    version=cursor_rules.__version__,
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'switch-rules=switch_rules.cursor_rules:main_switch_rule',
            'find-rules=switch_rules.cursor_rules:main_find_rules'
        ],
    },
    author='wangrui',
    author_email='wangrui950328@163.com',
    description='一个用于快速切换Cursor规则文件的库',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url='https://github.com/WANGRUI-ZB/cursor-rules',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
