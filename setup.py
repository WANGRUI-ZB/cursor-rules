from setuptools import setup, find_packages

setup(
    name='cursor_rules',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'switch-rules=switch_rules:switch_rule',  # 使 switch_rule 函数可通过命令行调用
            'find-rules=switch_rules:find_rule_by_tags'  # 使 find_rule_by_tags 函数可通过命令行调用
        ],
    },
    author='wangrui',
    author_email='wangrui950328@163.com',
    description='一个用于快速切换Cursor规则文件的库',
    url='你的项目网址',  # 替换为你的项目网址
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # 替换为你的许可证
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
