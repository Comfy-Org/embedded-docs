> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddNoise/pt-BR.md)

# AddNoise

Este nó adiciona ruído controlado a uma imagem latente usando parâmetros de ruído e valores sigma especificados. Ele processa a entrada através do sistema de amostragem do modelo para aplicar uma escala de ruído apropriada para a faixa sigma fornecida.

## Como Funciona

O nó recebe uma imagem latente e aplica ruído a ela com base no gerador de ruído e nos valores sigma fornecidos. Primeiro, ele verifica se há sigmas fornecidos - se não houver, retorna a imagem latente original inalterada. Em seguida, o nó utiliza o sistema de amostragem do modelo para processar a imagem latente e aplicar ruído escalonado. A escala do ruído é determinada pela diferença entre o primeiro e o último valor sigma quando múltiplos sigmas são fornecidos, ou pelo valor sigma único quando apenas um está disponível. Imagens latentes vazias (contendo apenas zeros) não são deslocadas durante o processamento. A saída final é uma nova representação latente com o ruído aplicado, com quaisquer valores NaN ou infinitos convertidos para zeros para garantir estabilidade.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | Obrigatório | - | - | O modelo que contém os parâmetros de amostragem e funções de processamento |
| `noise` | NOISE | Obrigatório | - | - | O gerador de ruído que produz o padrão de ruído base |
| `sigmas` | SIGMAS | Obrigatório | - | - | Valores sigma que controlam a intensidade da escala do ruído |
| `latent_image` | LATENT | Obrigatório | - | - | A representação latente de entrada à qual o ruído será adicionado |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `LATENT` | LATENT | A representação latente modificada com ruído adicionado |
