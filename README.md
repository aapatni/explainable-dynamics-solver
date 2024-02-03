# explainable-dynamics-solver

## Abstract 

This work deals with adding explainability to SINDy Autoencoders. SINDy Autoencoders are a machine learning technique that combine encoder-decoder neural networks and a regression algorithm to generate a set of coordinates and dynamical equations for a dynamical system [1]. The regression portion of the technique is quite interpretable in itself as it is just regression, and the output is an ODE describing a system, which is quite easy for a domain expert to decipher. However, the main problem comes with the encoder-decoder neural network, which is used to look at high dimensional sensor data and reduce it to a few coordinates or features for SINDy to act on. While SINDy Autoencoders can generate interpretable ordinary differential equations (ODEs) from time series data, they face difficulties in making the coordinate generation part, handled by neural networks, interpretable. This lack of interpretability is problematic for domain experts who need a clear physical understanding of the coordinates or features used in their models. To help with this aspect we propose a way to make the coordinate generation part of SINDy Autoencoders more explainable.

## Methodology

The methodology proposed in the paper revolves around creating explanations that clarify the meaning of the learned coordinate system. Since scientific data often comes in the form of images or videos, the goal is to establish a 1-to-1 visualization between the learned coordinates and spatial features. For instance, if the original data represents geometric shapes, the coordinates could be replaced with images of those shapes. The explanations are generated using techniques like Grad-Cam/explanation by example or alternative dimensionality reduction methods that prioritize interpretability.

## Experiments + Results + Visualization 
### (short version - reach out if youd like read our final paper)

Dataset - Georgia Tech Spinodal Decomposition Dataset which models a phase separation process where a single-phase solution becomes unstable and spontaneously separates into two distinct phases. The dataset maps this reaction through 100 discrete timesteps over a variety of starting configurations + experimental parameters.

Mapping: state [x] -> partial derivative of state [d(x)/dt]

Architecture: x -> Encoder -> SINDY -> Decoder -> dx/dt

Our encoder's latent space is 2-dimensional. SINDY operates on this latent space and fits and ODE to best model the evolution of the system. 

These two visualizations model the gradient w.r.t loss of the the networks decoder.

https://github.com/aapatni/explainable-dynamics-solver/assets/21110240/e3121984-8385-4e99-addf-625af6c779c6

https://github.com/aapatni/explainable-dynamics-solver/assets/21110240/b57d0dad-f15e-4a2e-a37d-b7c951a3166a

This visualization models the importance of each dimension of the latent space, showing that the two variables in the latent space are generally uncorrelated in each timestep (one dominates).

![sim_7_encoder fc4_latent_gradients_evolution](https://github.com/aapatni/explainable-dynamics-solver/assets/21110240/6301005f-e5ef-4b68-afdd-564286dbc7d6)


## References
[1] Brunton, S. L., Proctor, J. L., & Kutz, J. N. (2016). Discovering governing equations from data by sparse identification of nonlinear dynamical systems. Proceedings of the national academy of sciences, 113(15), 3932-3937.

[2] Champion, K., Lusch, B., Kutz, J. N., & Brunton, S. L. (2019). Data-driven discovery of coordinates and governing equations. Proceedings of the National Academy of Sciences, 116(45), 22445-22451.

[3] Fetni, S., Pham, T. Q. D., Hoang, T. V., Tran, H. S., Duchêne, L., Tran, X. V., & Habraken, A. M. (2023). Capabilities of Auto-encoders and Principal Component Analysis of the reduction of microstructural images; Application on the acceleration of Phase-Field simulations. Computational Materials Science, 216, 111820.

## Contributors
Michael Buzzy, Husain Gynai, Adam Patni
Prof: Sonia Chernova
