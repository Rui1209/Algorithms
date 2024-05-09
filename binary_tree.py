class TreeNode:
    def __init__(self, name):
        self.name = name
        # 初始化子節點
        self.children_indices = []
    # 判斷走訪遞迴方向
    def postorder_traversal(self, tree, back=False):
        # 後序走訪(Postorder Traversal)
        if not back:
            for child_index in self.children_indices:
                # 使用isinstance，判斷兩個類型是否相同，有繼承關係
                # 如果節點為list，代表該節點有多個子節點
                if isinstance(child_index, list):
                    # 針對內部子節點進行後序走訪 (左->右->根)
                    for index in child_index:
                        tree[index].postorder_traversal(tree)
                else:
                    # 如果節點非list，直接進行後序走訪
                    tree[child_index].postorder_traversal(tree)
            # 輸出當前節點名稱
            print(self.name)
        
        # 逆後序走訪 
        else:
            #首先輸出當前節點
            print(self.name)
            # 運用reversed對子節點進行反轉
            for child_index in reversed(self.children_indices):
                if isinstance(child_index, list):
                    # 針對內部子節點進行逆後序走訪 (根->右->左)
                    for index in child_index:
                        tree[index].postorder_traversal(tree, back=True)
                else:
                    # 如果節點非list，直接進行逆後序走訪
                    tree[child_index].postorder_traversal(tree, back=True)
    
    # 顯示樹狀結構
    def display_tree_structure(self, tree, depth=0):
        # 輸出節點名稱，並根據深度縮排
        print("  " * depth + self.name)
        for child_index in self.children_indices:
        # 如果節點為list，代表該節點有多個子節點
            if isinstance(child_index, list):
                for index in child_index:
                    tree[index].display_tree_structure(tree, depth + 1)
            else:
                tree[child_index].display_tree_structure(tree, depth + 1)


#創建節點
tree = [
    TreeNode("car_model"),
    TreeNode("car_body"),   # 1
    TreeNode("car_wheel_1"),# 2
    TreeNode("car_wheel_2"),# 3
    TreeNode("car_hold"),   # 4
    TreeNode("bearing"),    # 5
    TreeNode("fixed"),      # 6
    TreeNode("hold") ,      # 7
    TreeNode("motor"),      # 8
    TreeNode("wheel"),      # 9
    TreeNode("long"),       #10
    TreeNode("support-11"), #11
    TreeNode("screw")       #12
]
# 建立父子關係
tree[0].children_indices.extend([1,2,3,4])
tree[1].children_indices.extend([5,6,6,7,6,6,6,6])
tree[2].children_indices.extend([8,10,9,12])
tree[3].children_indices.extend([8,10,9,12])
tree[4].children_indices.extend([11,6,6])


# 打印樹狀結構樣貌
print("display_tree_structure")
tree[0].display_tree_structure(tree)
print("\n")
# 後序走訪
print("postorder_traversal")
tree[0].postorder_traversal(tree)
print("\n")
# 反向後序走訪
print("postorder_traversal_back")
tree[0].postorder_traversal(tree, back=True)
