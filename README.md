# PythonStatsModule
Basic Python module that handles basic but most tricky stats functions
OOP Oriented, each functions is represented by an object: 

```py
script_mean_controller = Mean()
players_mean = script_mean_controller.get({...})
```

Module handles some of these functions : 

Mean Handling: 

![equation](https://latex.codecogs.com/gif.image?%5Chuge%20%5Cdpi%7B110%7D%5Cbg%7Bblack%7D%5Coverline%7Bx%7D=%5Cfrac%7B%5Csum%20x%7D%7Bn%7D)

Variance Handling:

![equation](https://latex.codecogs.com/gif.image?%5Chuge%20%5Cdpi%7B110%7D%5Cbg%7Bblack%7D%5Csum%5Cfrac%7B%5Cleft(%20x_%7Bi%7D%20-%20%5Cmu%20%20%5Cright%20)%5E%7B2%7D%7D%7B%5Ceta%20%7D%20)

Typical Gap Handling: 

![equation](https://latex.codecogs.com/gif.image?%5Chuge%20%5Cdpi%7B110%7D%5Cbg%7Bblack%7D%5Csigma=%20%5Csqrt%7B%5Cnu%7D_%7Ba%7D)

Intervall Checker: 

![equation](https://latex.codecogs.com/gif.image?%5Chuge%20%5Cdpi%7B110%7D%5Cbg%7Bblack%7Dx%5Cin%20%5Csqsubset%20%5Calpha%20-%202*%5Csigma%20;%5Calpha%20&plus;%202*%5Csigma%5Csqsupset%20)
