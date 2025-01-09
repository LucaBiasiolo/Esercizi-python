from emnist import extract_training_samples, extract_test_samples

training_letters, training_labels = extract_training_samples('letters')
testing_letters, testing_labels = extract_test_samples('letters')

print(training_letters[0])
