# Imagem Latente em Camadas Qwen Vazia

O nó Empty Qwen Image Layered Latent prepara a tela em branco sobre a qual o modelo Qwen-Image-Layered desenha. Pense nele como uma pilha de folhas de papel vegetal limpas, presas em ordem: o modelo preenche a primeira folha com a imagem completa e cada folha seguinte com uma parte dessa imagem. Este nó decide o tamanho e a quantidade das folhas. Ele não desenha nada por si só.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `largura` | A largura da imagem latente a ser criada. O valor deve ser divisível por 16. (padrão: 640) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | A altura da imagem latente a ser criada. O valor deve ser divisível por 16. (padrão: 640) | INT | Sim | 16 a MAX_RESOLUTION |
| `camadas` | Em quantas camadas dividir a imagem. Uma folha extra é sempre reservada para a imagem completa, então você obtém `layers + 1` imagens, não `layers`. Defina como 2 e você obtém a imagem completa mais 2 camadas. Defina como 0 e você obtém apenas a imagem completa. (padrão: 3) | INT | Sim | 0 a MAX_RESOLUTION |
| `tamanho_do_lote` | O número de amostras latentes a serem geradas em um lote. (padrão: 1) | INT | Não | 1 a 4096 |

**Observação:** Os parâmetros `width` e `height` são internamente divididos por 8 para determinar as dimensões espaciais do tensor latente de saída.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `samples` | Um tensor latente preenchido com zeros. Sua forma é `[batch_size, 16, layers + 1, height // 8, width // 8]`. | LATENT |

## Por que você obtém uma imagem a mais do que pediu

O Qwen-Image-Layered não apenas decompõe uma imagem. Ele também redesenha a imagem completa, em sua própria folha, junto com as camadas. É por isso que a pilha é sempre uma folha mais alta do que o número de camadas que você pediu.

- **A primeira imagem é a imagem completa, não uma camada.** É a mesma imagem que você já tem, então descarte-a quando quiser apenas as camadas.
- **Se você empilhar todas as camadas, obterá a imagem completa novamente.** Se elas não somarem aquela primeira imagem, a separação não funcionou como você queria, então esta é uma forma rápida de verificar o resultado.
- **Mantenha as folhas em ordem.** A pilha é o único registro de qual camada fica sobre qual. Nada está escrito nas folhas para indicar onde elas vão, então reordenar ou descartar imagens significa reordenar ou perder camadas.
- **As camadas saem com transparência**, para que possam ser empilhadas sem que as camadas inferiores fiquem ocultas atrás de um fundo opaco.

## Sugestões de uso

Envie a saída para o amostrador como faria com uma latente vazia normal e, em seguida, coloque LatentCutToBatch com `dim` definido como `t` antes da decodificação VAE. Esse é o passo que separa a pilha em imagens individuais, em ordem, começando pela imagem completa.

Comece com o padrão de 3 camadas. Pedir mais significa uma geração mais longa e uma separação mais fina, e não vale a pena aumentar até você ver o que o modelo faz com um número pequeno.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyQwenImageLayeredLatentImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fe97966663c534dd347aa49a908a8026f2c34716631f1d17be97d74eacc3574e`
