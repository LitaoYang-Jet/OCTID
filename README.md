
# OCTID: One-Class learning-based tool for Tumor Image Detection

OCTID is an one-class learning-based python package for tumor tile detection. OCTID can capture patterns from the available normal WSIs to identify and remove normal tiles from the training dataset. By using OCTID, researchers without pathology expertise can select the tumor images based on the readily available data. Utilizing the power of machine learning, OCTID can conduct image pre-processing easily on the large-scale dataset.

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
                              training_dataset = 'training_dataset_path', validation_dataset = 'validation_dataset_path', unlabelled_dataset='unlabelled_dataset_path')

# run the classify model
classify_model()
```

### Parameters

1. model: The default value is "GoogleNet". The pre-defined models from [pretrained torchvision models](https://pytorch.org/docs/stable/torchvision/models.html) can be loaded when customised_model is set to "False". Customised models can also be accepted when customised_model is set to "False".

2. customised_model (Boolean): The default value is False. If you want to use your own customised model, you can set this parameter to "Ture" and load your model and pass it to the "model" parameter.

3. feature_dimension (Int): the feature dimension after using Umap, and the default value is 3

4. outlier_fraction_of_SVM (Float) : we are using the rbf kernel for SVM. This parameter is an upper bound on the fraction of training errors and a lower bound of the fraction of support vectors. Should be in the interval (0, 1]. By default 0.03 will be taken.

5. training_dataset (String): the path of your template dataset folder, which should only contain the positive or negative images.

6. validation_dataset (String): the path of your validation dataset folder, which should contain both positive and negative images.

7. unlabelled_dataset (String): the path of the dataset that you want to classify, which will be divided into two categories and placed in two subfolders after running our classify model.

** Dataset folders notes: since we are using the [torchvision.datasets.ImageFolder](https://pytorch.org/docs/stable/torchvision/datasets.html#imagefolder) to label the image, please follow the way to create your image folders. And the image should be cut down to small images such as 500 by 500, not the original medical micro image.
