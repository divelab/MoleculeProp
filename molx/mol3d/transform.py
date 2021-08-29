import torch
from rdkit import Chem
from torch_geometric.data import Data, Batch

class TransformPred3D(torch.nn.Module):
    """ Converting :obj:`torch_geometric.data.Data` objects into 3d versions
    using 3d prediction models.
    """
    def __init__(self, model3d, target_id=0, device=None):
        super(TransformPred3D, self).__init__()
        self.model3d = model3d
        self.device = device
        self.target_id = target_id
        
    def forward(self, data):
        in_device = data.x.device
        batch_data = Batch.from_data_list([data])
        if device is not None:
            batch_data.to(self.device)
            self.model3d.to(self.device)
            
        pred, _, _ = self.model3d(batch_data)
        dist_index = torch.nonzero(pred, as_tuple=False)
        dist_weight = pred[torch.nonzero(pred, as_tuple=True)]
        
        transformed = data.clone()
        transformed.__delitem__('props')
        transformed.__setitem__('dist_index', dist_index.to(in_device))
        transformed.__setitem__('dist_weight', dist_weight.to(in_device))
        transformed.__setitem__('y', data.props[self.target_id])
        return transformed
    
    
class TransformGT3D():
    """ Converting datasets containing 3d groundtruths into accepted format
    by downstream 3D networks.
    """
    def __init__(self, target_id=0):
        self.target_id = target_id
        
    def __call__(self, data):
        transformed = data.clone()
        transformed.__delitem__('props')
        transformed.__setitem__('y', data.props[self.target_id])
        return transformed
    

class TransformRDKit3D():
    """ Converting :obj:`torch_geometric.data.Data` objects containing SMILES 
    attribute into 3d versions using RDKit.
    """
    def __init__(self, target_id=0, conf_id=-1):
        self.target_id = target_id
        self.conf_id = conf_id
    
    def __call__(self, data):
        mol = Chem.MolFromSmiles(data.smiles)
        coords = mol.GetConformer(self.conf_id).GetPositions()
        xyz = torch.tensor(coords, dtype=torch.float32)
        
        transformed = data.clone()
        transformed.__setitem__('xyz', data.__getitem__(orig_key))
        transformed.__setitem__('y', data.props[self.target_id])
        transformed.__delitem__('props')
        return transformed