import pandas as pd
import numpy as np
from pprint import pprint
data = pd.read_csv("ml_assi2_dataset.csv")
# data = pd.DataFrame({"toothed":["True","True","True","False","True","True","True","True","True","False"],
#                      "hair":["True","True","False","True","True","True","False","False","True","False"],
#                      "breathes":["True","True","True","True","True","True","False","True","True","True"],
#                      "legs":["True","True","False","True","True","True","False","False","True","True"],
#                      "species":["Mammal","Mammal","Reptile","Mammal","Mammal","Mammal","Reptile","Reptile","Mammal","Reptile"]}, 
#                     columns=["toothed","hair","breathes","legs","species"])
# features = data[["toothed","hair","breathes","legs"]]
# target = data["species"]
data
def entropy(target_col):
    elements,counts = np.unique(target_col,return_counts = True)
    for i in range(len(elements)):
        entropy = np.sum( (-counts[i]/np.sum(counts)) * np.log2(counts[i]/np.sum(counts)) ) 
    return entropy
def InfoGain(data,split_attribute_name,target_name="class"):
    #Calculate the entropy of the total dataset
    total_entropy = entropy(data[target_name])
    
    ##Calculate the entropy of the dataset
    
    #Calculate the values and the corresponding counts for the split attribute 
    vals,counts= np.unique(data[split_attribute_name],return_counts=True)
    
    #Calculate the weighted entropy
    arr = []
    for i in range(len(vals)) :
        arr.append( (counts[i]/np.sum(counts)) * entropy(data.where(data[split_attribute_name]==vals[i]).dropna()[target_name]) )    
    Weighted_Entropy = np.sum(arr)
    
    #Calculate the information gain
    Information_Gain = total_entropy - Weighted_Entropy
    return Information_Gain
def ID3(data,originaldata,features,target_attribute_name="class",parent_node_class = None):
    #Define the stopping criteria --> If one of this is satisfied, we want to return a leaf node#
    
    #If all target_values have the same value, return this value
    if len(np.unique(data[target_attribute_name])) <= 1:
#         print("one")
        return np.unique(data[target_attribute_name])[0]
        
    
    #If the dataset is empty, return the mode target feature value in the original dataset
    elif len(data)==0:
#         return parent_node_class
#         print("two")
        return np.unique(originaldata[target_attribute_name])[np.argmax(np.unique(originaldata[target_attribute_name],return_counts=True)[1])]
    
    #If the feature space is empty, return the mode target feature value of the direct parent node --> Note that
    #the direct parent node is that node which has called the current run of the ID3 algorithm and hence
    #the mode target feature value is stored in the parent_node_class variable.
    
    elif len(features) ==0:
#         print("three")
        return parent_node_class
    
    #If none of the above holds true, grow the tree!
    
    else:
        #Set the default value for this node --> The mode(max count) target feature value of the current node
        index = np.argmax(np.unique(data[target_attribute_name],return_counts=True)[1])
        parent_node_class = np.unique(data[target_attribute_name])[index]
        
        #Select the feature which best splits the dataset
        item_values = [InfoGain(data,feature,target_attribute_name) for feature in features] #Return the information gain values for the features in the dataset
        best_feature_index = np.argmax(item_values)
        best_feature = features[best_feature_index]
        
        #Create the tree structure. The root gets the name of the feature (best_feature) with the maximum information
        #gain in the first run
        tree = {best_feature:{}}
#         print(tree)
        
        #Remove the feature with the best inforamtion gain from the feature space
        features = [i for i in features if i != best_feature]
        
        #Grow a branch under the root node for each possible value of the root node feature
        
        for value in np.unique(data[best_feature]):
            #Split the dataset along the value of the feature with the largest information gain and therwith create sub_datasets
            sub_data = data.where(data[best_feature] == value).dropna()
            
            #Call the ID3 algorithm for each of those sub_datasets with the new parameters --> Here the recursion comes in!
            subtree = ID3(sub_data,data,features,target_attribute_name,parent_node_class)
            
            #Add the sub tree, grown from the sub_dataset to the tree under the root node
            tree[best_feature][value] = subtree
            
        return(tree)    

# data.iloc[:,1:6].columns[:-1]  ---- all features without dependent variable    
tree = ID3(data.iloc[:,1:6],data.iloc[:,1:6],data.iloc[:,1:6].columns[:-1],"Buys")
pprint(tree)