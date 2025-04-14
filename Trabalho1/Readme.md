# 1. Regressão linear

Com parâmetros b=0, w=0, alpha=0.01, partir de um numero de iteração de 1500, mudanças no EQM são da ordem de 10^-4, e o resultado obtido para até 3 casas decimais foi de 8.527.
Com b=100 e w=100, mantendo um mesmo valor para o alpha, um numero maior de iterações foram necessárias para que as mudanças no EQM se mantivessem na ordem de 10^-4, no caso, o numero de iterações necesárias foi de cerca de 2500.



# 2. Tensorflow/Keras

 ### Características do datasets:
 CIFAR10 - imagens 32x32 com 3 canais de cores - "50,000 training images and 10,000 testing images" - 10 classes
 CIFAR100 - imagens 32x32 com 3 canais de cores - "50,000 training images and 10,000 testing images" - 100 classes
 MNIST - imagens 28x28 com 1 canal de cor - "60,000 training images and 10,000 testing images" - 10 classes
 FASHION MNIST - imagens 28x28 com 1 canal de cor -  "60,000 training images and 10,000 testing images" - 10 classes


### 1.
CIFAR100 é mais complexo que o CIFAR10 porque possui um número maior de classes  
CIFAR10 é mais complexon que o FASHION_MNIST porque possui mais canais de cores  
FASHION_MNIST é mais complexo que o MNIST pois possui classes mais complexas, com uma variabilidade intraclasse maior,
com diferentes classes sendo menos distingíveis entre si e com os tons de cinza possuindo mais expressividade, não representando apenas transições entre a existência ou não de um tracejado  
Ou seja: CIFAR100 >> CIFAR10 >> FASHION_MNIST >> MNIST

### 2.

results = {   
&nbsp; &nbsp; &nbsp; &nbsp; "mnist": {"time": 27.76, "acc": 99.27},  
&nbsp; &nbsp; &nbsp; &nbsp; "fashion_mnist": {"time": 32.83, "acc": 91.76},  
&nbsp; &nbsp; &nbsp; &nbsp; "cifar10": {"time": 60.65, "acc": 0.77},  
&nbsp; &nbsp; &nbsp; &nbsp; "cifar100": {"time": 51.14, "acc": 0.49},  
}


