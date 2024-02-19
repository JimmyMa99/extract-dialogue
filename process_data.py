import json
import argparse 

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--raw_data', type=str, default='tools/get_data/extract-dialogue/output/西游记白话文.json', help='input file')
    parser.add_argument('--save_path', type=str, default='tools/get_data/extract-dialogue/output/swk.jsonl', help='output file')
    parser.add_argument('--role', type=str, default='孙悟空', help='role name')
    return parser.parse_args()

def run(args):
    
    # 读取JSON数据
    with open(args.raw_data, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 转换数据格式
    converted_data = []
    for entry in data:
        conversation_entry = {
            "conversation": [
                {
                    "system": args.role,
                    "input": entry["instruction"],
                    "output": entry["output"]
                }
            ]
        }
        converted_data.append(conversation_entry)

    # 打印转换后的数据
    print(json.dumps(converted_data, ensure_ascii=False, indent=4))
    with open(args.save_path, 'w', encoding='utf-8') as f:
        for item in converted_data:
            json_item = json.dumps(item, ensure_ascii=False)  # 同上
            f.write(json_item + "\n")  # 同上
    # 保存数据    

if __name__ == '__main__':
    args=get_args()
    run(args)