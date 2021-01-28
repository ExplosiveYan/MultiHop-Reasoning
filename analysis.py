import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pickle

file_path = 'data/FB15K-237/raw.csv'
dev_file = 'data/FB15K-237/dev.triples'
test_file = 'data/FB15K-237/test.triples'
train_file = 'data/FB15K-237/train.triples'


dev_pd = pd.read_csv(dev_file, header=None)
test_pd = pd.read_csv(test_file, header=None)
train_pd = pd.read_csv(train_file, header=None)


"""

f = open('data/FB15K-237/adj_list.pkl','rb')
print(pickle.load(f, encoding='bytes'))


with open(train_file) as f:
    entity_list = []
    for line in f:
        # print(line.split( )[0])
        entity_list.append(line.split()[0])
entity_list_set = set(entity_list)
print(type(entity_list_set))
entity_list_set_num = []
for entity in entity_list_set:
    entity_list_set_num.append(entity_list.count(entity))

entity_list_set_num.sort(reverse=True)
print(entity_list_set_num)
number_list = list(range(len(entity_list_set)))

fig = plt.figure(figsize=(15, 10))
plt.bar(number_list, entity_list_set_num)

plt.savefig('Graph/entity_num.png', dpi=800)
plt.show()

"""

"""
# 画图 每条关系的三元组数量
with open(train_file) as f:
    relation_list = []
    for line in f:
        # print(line.split( )[0])
        relation_list.append(line.split()[2])
relation_list_set = set(relation_list)
print(type(relation_list_set))
relation_list_set_num = []
for relation in relation_list_set:
    relation_list_set_num.append(relation_list.count(relation))

relation_list_set_num.sort(reverse=True)
print(relation_list_set_num)
number_list = list(range(237))

fig = plt.figure(figsize=(15, 10))
plt.bar(number_list, relation_list_set_num)

plt.savefig('Graph/relation_num.png', dpi=800)
plt.show()
"""


"""
# 画图KG
GraphFile = pd.read_csv(file_path, header=None)
head_entities_list = GraphFile[0].tolist()
tail_entities_list = GraphFile[2].tolist()
pairs_list = []
for head, tail in zip(head_entities_list, tail_entities_list):
    pairs_list.append((head, tail))

Graph = nx.Graph()
Graph.add_edges_from(pairs_list[0: 10000])
print(Graph.number_of_nodes())
nx.draw(Graph, node_size=6, linewidths = 0.2)

plt.savefig("graph.png", dpi=600)
plt.show()
"""

# print(pairs_list)
