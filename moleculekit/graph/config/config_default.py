"""
Configuration file
"""



conf = {}

######################################################################################################################
# Settings for experimental setup
##    'model' chooses model from 'ml2' and 'ml3': ml2 is the proposed hierachical message passing model; ml3 is the model without subgraph-level representations, compared to ml2.
##    'task_type': 'regression' or 'classification'.
##    'metric' is the evaluation method: 'mae', 'rmse', 'prc', 'roc'
##    'num_tasks' denotes how many tasks we have in choosed dataset.
##    'graph_level_feature': if it is true, we combine the 200-d feature extracted by rkdit with the representation output by network together, and the use the combined representation to do property prediction.
######################################################################################################################
conf['model'] = 'ml2'
conf['task_type'] = 'regression'
conf['metric'] = 'mae'
conf['num_tasks'] = 12
conf['graph_level_feature'] = True


######################################################################################################################
# Settings for training
##    'epochs': maximum training epochs
##    'early_stopping': patience used to stop training
##    'lr': starting learning rate
##    'lr_decay_factor': learning rate decay factor
##    'lr_decay_step_size': step size of learning rate decay 
##    'dropout': dropout rate
##    'weight_decay': l2 regularizer term
##    'depth': number of layers
##    'batch_size': training batch_size
######################################################################################################################
conf['epochs'] = 400
conf['early_stopping'] = 200
conf['lr'] = 0.0005   ### [0.0001, 0.001]
conf['lr_decay_factor'] = 0.8 ### {0.5, 0.8}
conf['lr_decay_step_size'] = 50 ### {50, 80}
conf['dropout'] = 0 ### [0, 0.5]
conf['weight_decay'] = 0 ### [0, 0.0005]
conf['depth'] = 3  ### {3, 6}
conf['hidden'] = 256 ### {64, 128, 256}
conf['batch_size'] = 64  ### [64, 1024]


######################################################################################################################
# Settings for val/test
##    'vt_batch_size': val/test batch_size
######################################################################################################################
conf['vt_batch_size'] = 1000