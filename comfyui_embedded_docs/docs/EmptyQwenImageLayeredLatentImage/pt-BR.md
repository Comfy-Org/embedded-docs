# Imagem Latente em Camadas Qwen Vazia

Empty Qwen Image Layered Latent prepara a tela em branco sobre a qual o modelo Qwen-Image-Layered pinta. Pense nele como uma pilha de folhas de papel vegetal limpas, presas juntas em ordem: o modelo preenche a primeira folha com a imagem completa e cada folha seguinte com uma parte dessa imagem. Este nó decide o tamanho das folhas e quantas são. Ele não desenha nada por si só.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `largura` | A largura da imagem latente a ser criada. O valor deve ser divisível por 16. (padrão: 640) | INT | Sim | 16 a MAX_RESOLUTION (passo 16) |
| `altura` | A altura da imagem latente a ser criada. O valor deve ser divisível por 16. (padrão: 640) | INT | Sim | 16 a MAX_RESOLUTION (passo 16) |
| `camadas` | Em quantas camadas separar a imagem. Uma folha extra é sempre reservada para a imagem completa, então você recebe `layers + 1` imagens de volta, não `layers`. Defina como 2 e você obtém a imagem completa mais 2 camadas. Defina como 0 e você obtém apenas a imagem completa. (padrão: 3) | INT | Sim | 0 a MAX_RESOLUTION (passo 1) |
| `tamanho_do_lote` | O número de amostras latentes a serem geradas em um lote. (padrão: 1) | INT | Sim | 1 a 4096 |

**Observação:** Os parâmetros `width` e `height` são divididos internamente por 8 para determinar as dimensões espaciais do tensor latente de saída.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `samples` | Um tensor latente preenchido com zeros. Sua forma é `[batch_size, 16, layers + 1, height // 8, width // 8]`. | LATENT |

## Por que você recebe uma imagem a mais do que pediu

O Qwen-Image-Layered não apenas separa uma imagem em partes. Ele também repinta a imagem completa, em sua própria folha, ao lado das camadas. É por isso que a pilha tem sempre uma folha a mais do que o número de camadas que você pediu.

- **A primeira imagem é a imagem completa, não uma camada.** É a mesma imagem que você já tem; portanto, descarte-a quando quiser apenas as camadas.
- **Empilhe todas as camadas novamente umas sobre as outras e você obtém a imagem completa de novo.** Se elas não se somarem de volta para formar aquela primeira imagem, a separação não funcionou como você queria; então, essa é uma forma rápida de conferir o resultado.
- **Mantenha as folhas em ordem.** A pilha é o único registro de qual camada fica sobre qual. Nada está escrito nas próprias folhas para dizer onde elas pertencem; portanto, reordenar ou descartar imagens significa reordenar ou perder camadas.
- **As camadas saem com transparência**, para que possam ser empilhadas sem que as inferiores fiquem escondidas atrás de um fundo opaco.

## Sugestões de uso

Envie a saída para o sampler como faria com um tensor latente vazio normal; em seguida, coloque o LatentCutToBatch com `dim` definido como `t` antes do VAE Decode. Esse é o passo que separa a pilha em imagens individuais, em ordem, começando pela imagem completa.

Comece com o padrão de 3 camadas. Pedir mais significa uma geração mais longa e uma separação mais refinada, e não vale a pena aumentar até você ver o que o modelo faz com um número pequeno.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyQwenImageLayeredLatentImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5ccac979fcbcefb65f28867a89401c095cb330e09c13270008c32feeeafb1287`
