# This Python file uses the following encoding: utf-8
'''
Created on Mar 24, 2013

@author: dani
'''
from lxml import etree

def predict( model, values ):
    tree = etree.parse(model)
    root = tree.getroot()

    #TODO: check values into DataDictionary
    if 'TreeModel' in [ etree.QName(e).localname for e in root ]:
        return predictTreeModel( model, values )
    
    raise Exception("Only TreeModel suported at this time. Be free to contribute!")   

def predictTreeModel( model, values ):
    predict = None
    tree = etree.parse(model)
    root = tree.getroot()
    TreeModel = root.find( '{http://www.dmg.org/PMML-4_1}TreeModel' ) 

    #TODO: check values into MiningField
    
    #Node root de TreeModel. Predicció global
    Node = TreeModel.find( '{http://www.dmg.org/PMML-4_1}Node' )
    predict = Node.get("score")
    
    #Si node root té fills cal baixar pels fills.
    while True:
        fill = [ e for e in Node 
                 if etree.QName(e).localname == 'Node' and
                    values[ e[0].get('field') ] == e[0].get('value')  ]
        if fill:
            Node = fill[0]
            predict = Node.get("score")
        else:
            break
        
    return predict







    