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
    pct = 0.5
    n_tot = Node.get("recordCount")
    n_predict = next(  x.get( 'recordCount' ) for x in Node if etree.QName(x).localname == 'ScoreDistribution' and  x.get('value') == predict )
    
    #Through childs:
    while True:
        
        try:        
                    
            fill = next( e for e in Node 
                         if etree.QName(e).localname == 'Node' and
                            unicode(values[ e[0].get('field') ]) == e[0].get('value')  )

            try:
                Node = fill
                predict = Node.get("score")
                n_tot = Node.get("recordCount")
                n_predict = max(  x.get( 'recordCount' ) for x in Node if etree.QName(x).localname == 'ScoreDistribution' and  x.get('value') == predict )
            except IndexError:
                break
            
            try:
                pct = float(n_predict) / float(n_tot)
            except:
                pct = 0.5
        except StopIteration:
            break
        
        
    return  predict, pct





    