from octid import octid
classify_model = octid.octid(model = 'googlenet', customised_model = False, feature_dimension = 3, outlier_fraction_of_SVM = 0.03, traning_dataset='training_dataset', validation_dataset='validation_dataset', unlabeled_dataset=None)
classify_model()
