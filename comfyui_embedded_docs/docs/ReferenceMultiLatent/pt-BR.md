# Set Reference Multi Latent

Este nó codifica uma ou mais imagens de referência e anexa seus latents ao condicionamento que um modelo de edição consome. É a contraparte multi-imagem do Set Reference Latent: você conecta um VAE mais um conjunto de imagens de referência, e o nó anexa cada latent codificado ao condicionamento positivo e, quando um está conectado, também ao condicionamento negativo. Use-o quando um modelo espera várias imagens de referência ao mesmo tempo em vez de um único latent.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | O condicionamento positivo a ser modificado com os latents de referência. | CONDITIONING | Sim | - |
| `negative` | Condicionamento negativo opcional que recebe os mesmos latents de referência. Deixe-o desconectado para reutilizar o condicionamento positivo modificado na saída `negative`. | CONDITIONING | Não | - |
| `vae` | O VAE usado para codificar as imagens de referência conectadas. Obrigatório sempre que pelo menos uma imagem estiver conectada; caso contrário, o nó gera um erro. | VAE | Não | - |
| `resolution` | Como cada imagem de referência é preparada antes da codificação. `"keep resolution"` codifica-a no tamanho de entrada; `"resize"` redimensiona-a para uma contagem alvo de megapixels enquanto preserva a proporção, o que revela `megapixels`. (padrão: "keep resolution") | DYNAMIC_COMBO | Sim | `"keep resolution"`<br>`"resize"` |
| `images` | Slot expansível: conecte uma ou mais imagens de referência (`image_1`, `image_2`, ...) para usar como referências. As imagens são codificadas na ordem dos slots e anexadas ao condicionamento nessa ordem. | IMAGE | Não | 1 a 100 |

### Entradas de redimensionamento

Estas opções aparecem quando `resolution` é definido como `"resize"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `megapixels` | Tamanho alvo de cada imagem de referência, preservando a proporção. 1.0 equivale a aproximadamente 1024 x 1024 pixels. (padrão: 1.0) | FLOAT | Sim | 0.01 a 16.0 |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `positive` | O condicionamento positivo com os latents de referência codificados anexados. | CONDITIONING |
| `negative` | O condicionamento negativo com os mesmos latents de referência anexados. Retorna a saída positiva quando nenhum condicionamento negativo está conectado. | CONDITIONING |
| `empty_latent` | O primeiro latent de referência multiplicado por 0.0, pronto para inicializar um sampler. Vazio quando nenhuma imagem de referência está conectada. | LATENT |

## Observações

- Os latents são anexados em vez de substituídos, portanto encadear vários nós Set Reference Multi Latent acumula referências.
- Cada imagem conectada é codificada individualmente, então as imagens de referência não precisam compartilhar o mesmo tamanho.
- Sem nenhuma imagem conectada, `positive` e `negative` são retornados inalterados e `empty_latent` fica vazio.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceMultiLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7416feb8ac81cbf7e2d424e0212e88ab60235958c64550b0ee8c303093673756`
