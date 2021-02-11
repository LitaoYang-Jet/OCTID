from octid import octid
classify_model = octid.octid(model = 'googlenet', customised_model = False, feature_dimension = 3, outlier_fraction_of_SVM = 0.03, traning_dataset='small_samples/training_dataset', validation_dataset='small_samples/validation_dataset', unlabeled_dataset=None)
classify_model()
