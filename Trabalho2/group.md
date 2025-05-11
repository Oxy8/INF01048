# Integrantes

Eduardo Fonseca da Silva - 00577262 - Turma B  
Estevan Kuster - 00334328 - Turma B  
Pedro de Sene Bavaresco - 00333563 - Turma B  

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
&nbsp; &nbsp; &nbsp; &nbsp; "cifar10": {"time": 60.65, "acc": 77.63},  
&nbsp; &nbsp; &nbsp; &nbsp; "cifar100": {"time": 51.14, "acc": 45.91},  
}

**Tempo em segundos e acurácia em porcentagem**  

o fit dos modelos pros datasets mnist e fashion_mnist foi feito com batch_size de 2048 e 30 épocas  
o fit dos modelos pros datasets cifar10 e cifar100 foi feito com batch_size de 32 e 10 épocas  


Durante o desenvolvimento das redes, buscou-se aumentar o número de camadas de convolução e de neurônios para otimizar a acurácia durante o treinamento. Se percebíamos um overfit (performance em treinos muito melhor que em testes), buscavamos reduzir o número de camadas ou de neurônios/filtros por camada. Também foram utilizados dropouts para diminuit o overfit. Aumentar o número de camadas de convolução mostrou-se mais benéfico do que aumentar o número de camadas de neurônios: As camadas de convolução pareciam influenciar mais na melhora da acurácia dos casos de teste, enquanto que um aumento do número de neurônios geravam uma melhora na acurácia dos treinamentos que normalmente era acompanhada de um overfit difícil de corrigir.  

Além dessas estratégias, também foram realizados testes variando o tamanho da janela de convolução e da operação de max pooling, que impactam diretamente na extração de características das imagens. Observamos que tanto janelas muito pequenas quanto muito grandes afetavam negativamente a acurácia — possivelmente por reduzirem a capacidade da rede de detectar padrões relevantes. Janelas pequenas tendem a capturar apenas detalhes locais, enquanto janelas grandes podem perder informações mais refinadas ao olhar para áreas muito amplas. O número de filtros nas camadas convolucionais também foi ajustado em diferentes versões da rede. Um maior número de filtros geralmente melhorava a capacidade de extração de padrões, mas também aumentava o risco de overfitting. Para mitigar esse risco e estabilizar o treinamento, incorporamos a técnica de batch normalization, que contribuiu para acelerar a convergência e melhorar a generalização da rede.  

Foram realizados testes com batch_size de diferentes tamanhos, mas isso não se deu com o intuito de otimizar a performance da rede, mas sim, como forma de acelerar o processo de treinamento ao permitir que a GPU fosse mais bem utilizada com batch_size maiores.



