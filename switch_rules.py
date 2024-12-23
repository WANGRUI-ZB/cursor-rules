import os
import json

__version__ = '1.0'

def switch_rule(rule_name):
    rules_dir = 'rules'
    target_file = '.cursorrules'
    
    # 构建源文件路径
    source_file = os.path.join(rules_dir, rule_name)
    
    # 检查源文件是否存在
    if not os.path.isfile(source_file):
        print(f"规则文件 {rule_name} 不存在。")
        return
    
    # 读取规则文件内容
    with open(source_file, 'r', encoding='utf-8') as file:
        rule = json.load(file)
        content = rule.get('content', '')

    # 将内容写入目标文件
    with open(target_file, 'w', encoding='utf-8') as target:
        target.write(content)
    
    print(f"已将规则文件 {rule_name} 的内容复制到 {target_file}。")

def find_rule_by_tags(tags):
    rules_dir = 'rules'
    matching_rules = []

    # 遍历规则文件
    for filename in os.listdir(rules_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(rules_dir, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                rule = json.load(file)
                rule_tags = rule.get('tags', [])
                # 检查是否有任何标签匹配
                if any(tag in rule_tags for tag in tags):
                    matching_rules.append({'filename': filename, 'tags': rule_tags})

    return matching_rules

# 示例用法
if __name__ == "__main__":
    # 这里可以替换为用户输入的规则文件名
    switch_rule('example_rule.json')
    
    # 查找标签为 'tag1' 或 'tag2' 的规则文件
    rules = find_rule_by_tags(['tag1', 'tag2'])
    print(f"找到的规则文件: {rules}")