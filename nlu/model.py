from re import X
import yaml
import numpy as np
data = yaml.safe_load(open('./train.yml', 'r', encoding='utf-8').read())

inputs, outputs = [], []


for command in data['commands']:
    inputs.append(command['input'].lower())
    outputs.append('{}\{}'.format(command['entity'], command['action']))


# Processar texto
chars = set()

for input in inputs + outputs:
    for ch in input:
        if ch not in chars:
            chars.add(ch)
# Mapear chat-index
ch2ixd = {}
idx2char = {}
for i, ch in enumerate(chars):
    ch2ixd[ch] = i
    idx2char[i] = ch

print('Números de chars:', len(chars))

max_seq = max([len(X) for X in inputs])
print('Número máximo de sequências:', max_seq)

# Criar dataset one-hot (numeros de exemplos, tamanho sequências, numeros caracteres)
# Criar dataset disperso (numeros de exemplos, tamanho sequências, numeros caracteres)
input_data = np.zeros((len(inputs), max_seq, len(chars)), dtype='int32')

for i, input in enumerate(inputs):
    for k, ch in enumerate(input):
        input_data[i, k, ch2ixd[ch]] = 1.0
print(input_data[0])

'''
print(inputs)
print(outputs)
'''
