<p align="center">
<img src="https://github.com/divelab/MoleculeX/blob/master/imgs/MX-logo.jpg" width="500" class="center" alt="logo"/>
    <br/>
</p>

------

# Advanced Graph and Sequence Neural Networks for Molecular Property Prediction and Drug Discovery
[[Paper]](https://arxiv.org/abs/2012.01981)[[Supplementary]](https://documentcloud.adobe.com/link/track?uri=urn:aaid:scds:US:d0ca85d1-c6f9-428b-ae2b-c3bf3257196d#pageNum=1)

## Overview

Properties of molecules are indicative of their functions and thus are useful in many applications. As a cost-effective alternative to experimental approaches, computational methods for predicting molecular properties are gaining increasing momentum and success. However, there lacks a comprehensive collection of tools and methods for this task currently. Here we develop the MoleculeX, a suite of comprehensive machine learning tools spanning different computational models and molecular representations for molecular property prediction and drug discovery. Specifically, MoleculeX represents molecules as both graphs and sequences. Built on these representations, MoleculeX includes both deep learning and traditional machine learning methods for graph and sequence data. Noticeably, we propose and develop novel deep models for learning from molecular graphs and sequences. Therefore, MoleculeX not only serves as a comprehensive tool, but also contributes towards developing novel and advanced graph and sequence learning methodologies. Results on both online and offline antibiotics discovery and molecular property prediction tasks show that MoleculeX achieves consistent improvements over prior methods.

MoleculeX is unique in three aspects:

* MoleculeX consists of a suite of comprehensive machine learning methods across different data types and method types. We expect them to provide complementary information for molecular property prediction and yield better performance. 
* An effective graph-based deep learning method named multi-level message passing neural network (ML-MPNN) is proposed to make full use of richly informative molecular graphs.
* A new sequence-based deep learning method named contrastive-BERT, pretrained by a novel self-supervised task via contrastive learning, is incorporated.

<p align="center">
<img src="https://github.com/divelab/MoleculeX/blob/master/imgs/overview.png" width="1000" class="center" alt="overview"/>
    <br/>
</p>

## Usage

MoleculeX has four modules covering deep and non-deep methods based on both molecular graphs and SMILES sequence:
* [ML-MPNN](https://github.com/divelab/MoleculeX/tree/master/moleculex/graph)
* [Weisfeiler-Lehman subtree kernel](https://github.com/divelab/MoleculeX/tree/master/moleculex/kernels)
* [contrastive-BERT](https://github.com/divelab/MoleculeX/tree/master/moleculex/sequence)
* [subsequence kernel](https://github.com/divelab/MoleculeX/tree/master/moleculex/kernels)

The use of MoleculeX requires the running of above four models with four output results. The four output results are then ensembled as the final prediction. Users of MoleculeX are also given the freedom of employing fewer modules.

The environment requirements for these models might have conflict and we hence recommend create individual environments for each of them. To get started with MoleculeX, access the above links for your desired modules.

## Reference
```
@article{wang2020advanced,
  title={Advanced Graph and Sequence Neural Networks for Molecular Property Prediction and Drug Discovery},
  author={Wang, Zhengyang and Liu, Meng and Luo, Youzhi and Xu, Zhao and Xie, Yaochen and Wang, Limei and Cai, Lei and Ji, Shuiwang},
  journal={arXiv preprint arXiv:2012.01981},
  year={2020}
}
```
