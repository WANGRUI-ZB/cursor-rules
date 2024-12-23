# Rule Switcher

一个用于快速切换Cursor规则文件的 Python 库。该库支持通过标签查找规则文件，并将选定规则的内容复制到.cursorrules文件。

## 目录结构
cursor-rules/
│
├── rules/ # 存放规则文件的目录
│ ├── example_rule.json # 示例规则文件
│ └── ...
│
├── switch_rules.py # 主程序文件
├── setup.py # 包配置文件
└── LICENSE # 许可证文件


## 安装

1. 克隆这个仓库：

   ```bash
   git clone https://github.com/your_username/your_project.git
   cd your_project
   ```

2. 创建并激活虚拟环境（可选）：

   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. 安装依赖：

   ```bash
   pip install .
   ```

## 使用

### 切换规则

使用 `switch_rule` 函数将指定规则文件的内容复制到 `.cursorrules` 文件中。

   ```python
   from switch_rules import switch_rule
   switch_rule('example_rule.json')
   ```

### 查找规则

使用 `find_rule_by_tags` 函数根据标签查找规则文件。


   ```python
   from switch_rules import find_rule_by_tags
   rules = find_rule_by_tags(['tag1', 'tag2'])
   print(f"找到的规则文件: {rules}")
   ```

## 规则文件格式

规则文件应为 JSON 格式，包含 `tags` 和 `content` 字段。例如：

   ```json
   {
   "tags": ["tag1", "tag2"],
   "content": "这是规则的内容。"
   }
   ```


## 版本

当前版本：`1.0`

## 许可证

本项目采用 MIT 许可证，详细信息请查看 [LICENSE](LICENSE) 文件。