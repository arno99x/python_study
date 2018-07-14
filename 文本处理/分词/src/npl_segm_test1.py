# coding=utf-8
import jieba
seg_list = jieba.cut("杭州西湖风景很好，是旅游胜地！",
                     cut_all=False)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式
