from fastembed import TextEmbedding

if __name__ == "__main__":
    supported_models = TextEmbedding.list_supported_models()
    supported_models_dims = [model["dim"] for model in supported_models]
    print(min(supported_models_dims))