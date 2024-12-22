from datasets import load_dataset

dataset_path = "./dataset/cnn_dailymail/train.csv"

dataset = load_dataset("cnn_dailymail", '3.0.0')
train_data = dataset["train"]
validation_data = dataset["validation"]
test_data = dataset["test"]

print(train_data)
print(validation_data)