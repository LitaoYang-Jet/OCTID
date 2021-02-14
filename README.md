
# OCTID: One-Class learning-based tool for Tumor Image Detection

OCTID is an one-class learning-based python package for tumor tile detection. OCTID can capture patterns from the available normal WSIs to identify and remove normal tiles from the training dataset. By using OCTID, researchers without pathology expertise can select the tumor images based on the readily available data. Utilizing the power of machine learning, OCTID can conduct image pre-processing easily on the large-scale dataset. Example datasets can be downloaded [here](https://github.com/LitaoYang-Jet/OCTID/tree/main/small_samples).

## Getting started

Install OCTID from PyPI
(You may need to creat a new environment before installing OCTID.)

```bash
$ pip install octid
```

to run your first example
(A test.py file can be found [here](https://github.com/LitaoYang-Jet/OCTID/tree/main).)

```python
from octid import octid
# initialize the classify model with the requiered parameters
classify_model = octid.octid(model = 'googlenet', customised_model = False, feature_dimension = 3, outlier_fraction_of_SVM = 0.03,
                              training_dataset = 'training_dataset_path', validation_dataset = 'validation_dataset_path', unlabelled_dataset='unlabelled_dataset_path')

# run the classify model
classify_model()
```

### Parameters

1. model (String): Default value is "GoogleNet". The available models are listed below. The pre-defined models or customised models can be loaded when customised_model is set to "False" or "True".

2. customised_model (Boolean): The default value is False. If you want to use your own model, you can set this parameter to "Ture" and load and pass your model to the "model" parameter.

3. feature_dimension (Int): Feature dimension reduced by using [Umap](https://umap-learn.readthedocs.io/en/latest/), and the default value is 3.

4. outlier_fraction_of_SVM (Float) : The default value is 0.03. The rbf kernel is used in one-class [SVM](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html). This parameter is an upper bound on the fraction of training errors and a lower
bound of the fraction of support vectors, which is ranging from 0 to 1.

5. training_dataset (String): The path of your template dataset folder, which should only contain the positive or negative images.

6. validation_dataset (String): The path of your validation dataset folder, which should contain both positive and negative images.

7. unlabelled_dataset (String): The path of the dataset that you want to classify, which will be re-saved to two subfolders, corresponding to two classes.

* Dataset folders notes: since we are using the [torchvision.datasets.ImageFolder](https://pytorch.org/docs/stable/torchvision/datasets.html#imagefolder) to label the image, please follow the way to create your image folders. 
** Images processed here are small tiles not the whole slide images, which should be segmented into small images, such as 500 by 500.

### Available pre-trained models for OCTID

![image](https://github.com/LitaoYang-Jet/OCTID/blob/main/Available%20pre-trained%20models%20for%20OCTID.jpeg)
