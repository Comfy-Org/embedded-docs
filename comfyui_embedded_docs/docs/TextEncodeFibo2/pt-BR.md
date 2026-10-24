# TextEncodeFibo2

Codifique um prompt do Fibo 2.0 em condicionamento e um latente vazio correspondente. O prompt é texto simples ou uma legenda JSON estruturada; com imagens conectadas, ele se torna a instrução de edição, ou uma legenda JSON do resultado com uma chave `edit_instruction`, e as imagens atuam como latentes de referência para ambas as saídas quando um VAE está conectado. Faça a amostragem da saída `latent`, cujo tamanho é o tamanho para o qual as imagens são recortadas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | O codificador de texto Fibo 2.0 usado para tokenizar e codificar o prompt. | CLIP | Sim | - |
| `prompt` | A legenda a partir da qual gerar, ou a instrução de edição quando imagens estão conectadas. Consulte as imagens como `<image_1>`, `<image_2>` e assim por diante. Uma legenda JSON do resultado esperado também funciona, com a alteração descrita em sua chave `edit_instruction`. | STRING | Sim | - |
| `negative_prompt` | Legenda da qual se afastar, codificada como o condicionamento negativo. Um valor não vazio é enviado como está, dentro do template de chat do Fibo 2.0, sem ser limpo como uma legenda. Vazio é a legenda nula com a qual o Fibo 2.0 foi treinado para orientação sem classificador em fluxos de edição (padrão: vazio). | STRING | Sim | - |
| `vae` | VAE usado para codificar as imagens em latentes de referência. Sem ele, as imagens apenas condicionam a codificação de texto. | VAE | Não | - |
| `images` | Imagens a editar, até 16. Uma única imagem é escalada e recortada ao centro para o tamanho do resultado, porque a edição se alinha a ela pixel a pixel; várias imagens são cada uma escalada para seu próprio tamanho de treinamento. | IMAGE | Não | 0 a 16 imagens |
| `width` | Largura do resultado, arredondada para baixo para um múltiplo de 16. 0 usa o tamanho com o qual o Fibo 2.0 foi treinado para a proporção da primeira imagem, cerca de 1 megapixel, ou 1024 sem imagens (padrão: 0). | INT | Sim | 0 a 16384 (passo 16) |
| `height` | Altura do resultado, arredondada para baixo para um múltiplo de 16. 0 usa o tamanho com o qual o Fibo 2.0 foi treinado para a proporção da primeira imagem, cerca de 1 megapixel, ou 1024 sem imagens (padrão: 0). | INT | Sim | 0 a 16384 (passo 16) |
| `batch_size` | Número de latentes a criar no lote (padrão: 1). | INT | Sim | 1 a 4096 |

Os latentes de referência são anexados a ambas as saídas, portanto as imagens viajam com o condicionamento, e não apenas com o ramo positivo. Quando o VAE não está conectado, as imagens são vistas apenas pelo codificador de texto e nenhum latente de referência é adicionado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento do prompt, com os latentes de referência quando um VAE e imagens estão conectados. | CONDITIONING |
| `negative` | Condicionamento de `negative_prompt`, somente texto, com os mesmos latentes de referência. | CONDITIONING |
| `latent` | Latente vazio no tamanho solicitado, pronto para ser amostrado. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeFibo2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `55519ccce6420289b01b5855b80f522057da78f5a17bf7db63e2418d15f9e356`
