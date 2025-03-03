import torch
from torchvision import datasets, transforms

def test_data_shape():
    # Define transformations
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

    # Load the MNIST training dataset
    train_dataset = datasets.MNIST(root="../data", train=True, download=True, transform=transform)

    # Check the shape of the first data point
    data, label = train_dataset[0]
    assert data.shape == torch.Size([1, 28, 28]), f"Unexpected data shape: {data.shape}"
    assert label in range(10), f"Unexpected label: {label}"

    print("Data shape test passed!")

def test_data_normalization():
    # Define transformations
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

    # Load the MNIST training dataset
    train_dataset = datasets.MNIST(root="../data", train=True, download=True, transform=transform)

    # Check the normalization of the first data point
    data, _ = train_dataset[0]
    assert torch.all(data >= -1.0) and torch.all(data <= 1.0), "Data is not normalized correctly"

    print("Data normalization test passed!")

def test_data_labels():
    # Define transformations
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

    # Load the MNIST training dataset
    train_dataset = datasets.MNIST(root="../data", train=True, download=True, transform=transform)

    # Check that all labels are in the range 0-9
    for _, label in train_dataset:
        assert label in range(10), f"Unexpected label: {label}"

    print("Data labels test passed!")

if __name__ == "__main__":
    test_data_shape()
    test_data_normalization()
    test_data_labels()
