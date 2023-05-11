import torch

if __name__ == "__main__":
    if torch.cuda.is_available():
        device = torch.device("cuda")  # Use GPU
        print("GPU available. Using", torch.cuda.get_device_name(0))
    else:
        device = torch.device("cpu")  # Use CPU
        print("GPU not available. Using CPU.")