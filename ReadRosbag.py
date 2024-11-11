#!/usr/bin/env python
import rosbag
import os

def read_rosbag(bag_path):
    try:
        # 打开bag文件
        bag = rosbag.Bag(bag_path)
        
        # 获取bag信息
        info = bag.get_type_and_topic_info()
        print("话题列表:")
        for topic in info.topics.keys():
            print(f"- {topic}")
            
        # 读取每个话题的消息
        for topic, msg, t in bag.read_messages():
            # 打印时间戳和话题名称
            print(f"时间戳: {t}")
            print(f"话题: {topic}")
            print(f"消息: {msg}")
            print("---")
            
        # 关闭bag文件
        bag.close()
        
    except Exception as e:
        print(f"读取bag文件时发生错误: {str(e)}")

if __name__ == "__main__":
    # 设置bag文件路径
    my_path = "your_bag_file.bag"  # 替换为实际的bag文件路径
    
    # 检查文件是否存在
    if os.path.exists(my_path):
        read_rosbag(my_path)
    else:
        print(f"找不到bag文件: {my_path}")
