#1
# Hàm tính tổng hai ma trận A và B
def mPlus(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Hàm tính hiệu hai ma trận A và B
def mMinus(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Hàm tính tích của hai ma trận A và B
def mMultiply(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Hàm tính ma trận chuyển vị của A
def mTranspose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

# Ma trận ví dụ để kiểm tra
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Kiểm tra các hàm
print("A + B =", mPlus(A, B))  # 1a. Tính tổng hai ma trận
print("A - B =", mMinus(A, B))  # 1b. Tính hiệu hai ma trận
print("A * B =", mMultiply(A, B))  # 1c. Tính tích hai ma trận
print("Transpose of A =", mTranspose(A))  # 1d. Tính ma trận chuyển vị

# Ma trận thêm để kiểm tra hàm nhân và chuyển vị
A_new = [[1, 2, 3], [4, 5, 6]]
B_new = [[7, 8], [9, 10], [11, 12]]

print("A_new * B_new =", mMultiply(A_new, B_new))  # 1e. Kiểm tra hàm nhân với A và B mới
print("Transpose of A_new =", mTranspose(A_new))  # 1e. Kiểm tra hàm chuyển vị với A mới

#-----------------------------------------------------------------------------------------------
#2
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Tạo đồ thị và thêm cạnh cùng với trọng số
G = nx.DiGraph()

# Thêm cạnh cùng với trọng số cho đồ thị
edges = [("A", "C", 5), ("A", "D", 3), ("B", "C", 3), ("B", "D", 2), ("C", "D", 1), ("C", "E", 3)]
G.add_weighted_edges_from(edges)

# Tính ma trận trọng số (trong trường hợp này là ma trận kề với trọng số)
# Lưu ý: networkx sử dụng scipy.sparse matrix để lưu trữ ma trận trọng số
weight_matrix = nx.adjacency_matrix(G).todense()
print("Ma trận trọng số của đồ thị:")
print(weight_matrix)

# Vẽ đồ thị
pos = nx.spring_layout(G)  # Tạo vị trí cho các nút dựa trên thuật toán spring layout
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='k', linewidths=1, font_size=15, arrows=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)}, font_color='red')
plt.show()


#-----------------------------------------------------------------------------------------------

#3
def create_weighted_matrix(edges, nodes):
    """Tạo ma trận kề có trọng số từ danh sách cạnh."""
    matrix = np.zeros((len(nodes), len(nodes)))
    for edge in edges:
        i, j, weight = nodes.index(edge[0]), nodes.index(edge[1]), edge[2]
        matrix[i][j] = weight
        matrix[j][i] = weight  # Đối với đồ thị vô hướng
    return matrix

def plot_graph(edges, nodes):
    """Vẽ đồ thị từ danh sách cạnh."""
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    pos = nx.spring_layout(G)  # vị trí cho tất cả các nút
    nx.draw(G, pos, with_labels=True, node_size=700)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

# Danh sách nút
nodes = ['A', 'B', 'C', 'D', 'E', 'F']

# Cạnh cho phần (a) và (b)
edges_a = [('A', 'C', 5), ('A', 'D', 3), ('B', 'C', 3), ('B', 'D', 2), ('C', 'D', 1), ('C', 'E', 3), ('D', 'E', 1), ('D', 'F', 3), ('E', 'F', 4)]
edges_b = [('A', 'C', 2), ('A', 'D', 3), ('A', 'E', 3), ('B', 'C', 3), ('B', 'D', 2), ('C', 'D', 2), ('C', 'E', 8), ('C', 'F', 6), ('D', 'F', 5), ('E', 'F', 3)]

# Tạo và in ra ma trận có trọng số
matrix_a = create_weighted_matrix(edges_a, nodes)
matrix_b = create_weighted_matrix(edges_b, nodes)
print("Ma trận có trọng số cho Phần (a):\n", matrix_a)
print("Ma trận có trọng số cho Phần (b):\n", matrix_b)

# Vẽ đồ thị
print("Đồ thị cho Phần (a):")
plot_graph(edges_a, nodes)
print("Đồ thị cho Phần (b):")
plot_graph(edges_b, nodes)


#-----------------------------------------------------------------------------------------------

#4
def toLoE(A):
    edges = []
    n = len(A)  
    for i in range(n):
        for j in range(i + 1, n): 
            if A[i][j] != 0:  
                edges.append((i, j, A[i][j]))
    return edges

# Example usage:
A = np.array([
    [0, 2, 3, 0, 0],
    [0, 0, 0, 4, 0],
    [0, 0, 0, 5, 6],
    [0, 0, 0, 0, 7],
    [0, 0, 0, 0, 0]
])

edges = toLoE(A)
print("List of Edges:", edges)

#-----------------------------------------------------------------------------------------------

#5
G = nx.DiGraph()

G.add_edges_from([
    ('Monkeys', 'Primates'), ('Apes', 'Primates'), ('Gorillas', 'Primates'),
    ('Mice', 'Rodents'), ('Squirrels', 'Rodents'), ('Beavers', 'Rodents'),
    ('Crocodiles', 'Reptiles'), ('Komodo dragons', 'Reptiles'), ('Lizards', 'Reptiles'),
    ('Coconut trees', 'Plants'), ('Grasses', 'Plants'), ('Oaks', 'Plants'),
    ('Mushrooms', 'Fungi'), ('Molds', 'Fungi'), ('Yeasts', 'Unicellular organisms'),
    # the more general categories
    ('Primates', 'Mammals'), ('Rodents', 'Mammals'),
    ('Mammals', 'Animals'), ('Reptiles', 'Animals'),
    ('Animals', 'Multicellular organisms'), ('Plants', 'Multicellular organisms'),
    ('Fungi', 'Multicellular organisms'), ('Molds', 'Multicellular organisms')
])

# Draw the graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold", arrows=True)
plt.show()