self.layers = torch.nn.Sequential(
            collections.OrderedDict(
                [
                    ("enc_fc1", nn.Linear(input_size,128)),
                    ("enc_relu1", torch.nn.ReLU()),
                    ("enc_fc2", nn.Linear(128,64)),
                    ("enc_relu2", torch.nn.ReLU()),
                    ("enc_fc3", nn.Linear(64,32)),
                    ("enc_relu3", torch.nn.ReLU()),
                    ("enc_fc4", nn.Linear(32,latent_dim)),
                    ("enc_relu4", torch.nn.ReLU()),
                ]
            )
        )

self.layers = torch.nn.Sequential(
            collections.OrderedDict(
                [
                    ("dec_fc1", nn.Linear(latent_dim,32)),
                    ("dec_relu1", torch.nn.ReLU()),
                    ("dec_fc2", nn.Linear(32,64)),
                    ("dec_relu2", torch.nn.ReLU()),
                    ("dec_fc3", nn.Linear(64,128)),
                    ("dec_relu3", torch.nn.ReLU()),
                    ("dec_fc4", nn.Linear(128,input_size)),
                    ("dec_relu4", torch.nn.ReLU()),
                ]
            )
        )

# import netron
# netron.start(f1, 8081)



# from torchviz import make_dot

# def visualize_model(model, *input_tensor):
#     """
#     Visualize the given PyTorch model.
    
#     Parameters:
#     - model: A PyTorch model
#     - input_tensor: A tensor suitable for the model's forward method
#     """
    
#     # Carry out forward pass to create computational graph
#     output = model(*input_tensor)
    
#     # Visualize the computational graph
#     dot = make_dot(output[0].mean(), params=dict(model.named_parameters()))
    
#     return dot

# # Assuming `model` is your model and `dummy_input` is a suitable tensor for its forward method
# visualize_model(model, X, Xdot).view()
