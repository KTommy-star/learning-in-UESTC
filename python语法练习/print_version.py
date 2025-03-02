import pandas as pd
from sklearn.svm._libsvm import predict


# ... (省略未修改的函数)

def get_best_feature(data):
    pass


def get_most_label(data):
    pass


def create_tree(data):
    data_label = data.iloc[:, -1]
    if len(data_label.unique()) == 1:  # 所有样本标签相同
        return data_label.iloc[0]
    if data.iloc[:, :-1].nunique().sum() == 0:  # 所有特征值相同
        return get_most_label(data)

    best_feature = get_best_feature(data)
    Tree = {best_feature: {}}
    exist_vals = pd.unique(data[best_feature])

    for val in exist_vals:
        sub_data = data[data[best_feature] == val].drop([best_feature], axis=1)
        subtree = create_tree(sub_data)
        Tree[best_feature][val] = subtree

    return Tree


# ... (省略未修改的函数)

if __name__ == '__main__':
    data = pd.read_csv('西瓜数据集2.0.csv')
    decision_Tree = create_tree(data)
    print(decision_Tree)

    test_data_1 = {'色泽': '青绿', '根蒂': '蜷缩', '敲声': '浊响', '纹理': '稍糊', '脐部': '凹陷', '触感': '硬滑'}
    test_data_2 = {'色泽': '乌黑', '根蒂': '稍蜷', '敲声': '浊响', '纹理': '清晰', '脐部': '凹陷', '触感': '硬滑'}
    result = predict(decision_Tree, test_data_2)
    print('分类结果为' + ('好瓜' if result == 1 else '坏瓜'))