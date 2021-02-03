
# OCTID: One-Class learning-based tool for Tumor Image Detection

OCTID is a Python package, which utilizes a pre-trained CNN model, UMAP, and one-class SVM for tumor image detection based on the partially annotated dataset. OCTID can capture patterns from the available normal WSIs to identify and remove normal tiles from thetraining dataset. By using OCTID, researchers without pathology knowledge can select the tumor images based on the readily available data. Utilizing the power of machine learning, OCTID can conduct image pre-processing easily on the large-scale dataset.

## Getting started

Install OCTID from PyPI

```bash
$ pip install octid
```

to run your first example

```python
from octid import octid
# initialize the classify model with the requiered parameters
classify_model = octid.octid(model = 'GoogleNet',customised_model = False, feature_dimension = 3, outlier_fraction_of_SVM = 0.03, 
                              templates_path = 'templates_path', val_path = 'val_path', unlabeled_path='unlabeled_path')

# run the classify model
classify_model()
```

### Parameters

1. model: If you set the "custom_model" to False, you can use [pretrained torchvision models](https://pytorch.org/docs/stable/torchvision/models.html) by calling the model name such as 'GoogleNet'.

2. customised_model: If you want to use your own custom model, you can set this parameters to Ture and input your model to the "model" parameters. The default value is False.

3. feature_dimension: feature dimension after using Umap, the default value is 3

4. outlier_fraction_of_SVM, : we are using the rbf kernel for SVM. This parameter is an upper bound on the fraction of training errors and a lower bound of the fraction of support vectors. Should be in the interval (0, 1]. By default 0.03 will be taken.

5. templates_path: the path of your template dataset folder, which should only contain the positive(cancerous) images.

6. val_path: the path of your validation dataset folder, which should contain both positive and negative images.

7. unlabeled_path: the path of the dataset that you want to classify, which will be divided into two categories and placed in two folders after running our classify model

8. Dataset folders notes: since we are using the [torchvision.datasets.ImageFolder](https://pytorch.org/docs/stable/torchvision/datasets.html#imagefolder) to label the image, please follow the way to create your image folders. And the image should be cut down to small images such as 500 by 500, not the original medical micro image.

