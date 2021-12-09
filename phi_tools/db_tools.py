# -*- ecoding: utf-8 -*-
# @ModuleName: db_tool.py
# @Function: 一些工具方法
# @Author: ctx_phi
# @Craete Time: 2021/12/29 10:37

import json
import os
from loguru import logger
import bson
from bson import json_util

class BsontoJson:
    def __init__(self):
        return None

    def convert_many(self, dir_path, output_folder):
        file_list = os.listdir(dir_path)
        for file in file_list:
            matched_file = re.findall(".*\.bson", file)
            if matched_file:
                # 处理文件名称为中文
                renamed_file = unquote(matched_file[0]).replace('bson', 'json')
                print(renamed_file)
                self.convert_one(matched_file[0], output_folder + '/' +renamed_file)
        

    def convert_one(self, file_name, output_path):
        with open(file_name, "rb") as f:
            data = bson.decode_all(f.read())
#         logger.debug(data)
        print(type(data))
        if type(data) == list:
#             print(data)
            with open(output_path, 'w') as f:
                f.write(json_util.dumps(data))
        else:
            logger.error("数据类型错误，不是list")



if __name__ == "__main__":
    # print(os.listdir())
    with open("./phi_tools/zhihu_hot.bson", "rb") as f:
        data = bson.decode_all(f.read())
        # print(type(data)) 
    d = json_util.dumps(data)
    # logger.info(type(d))
    with open("./phi_tools/convert_data.json", "w") as f:
        f.writelines(d)
    print('finish')
    