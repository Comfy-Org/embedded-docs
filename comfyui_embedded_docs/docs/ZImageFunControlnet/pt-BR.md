> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/pt-BR.md)

O nó ZImageFunControlnet aplica uma rede de controle especializada para influenciar o processo de geração ou edição de imagens. Ele utiliza um modelo base, um patch de modelo e um VAE, permitindo ajustar a intensidade do efeito de controle. Este nó pode trabalhar com uma imagem base, uma imagem para inpaint e uma máscara para edições mais direcionadas.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `modelo` | MODEL | Sim | - | O modelo base utilizado no processo de geração. |
| `patch_do_modelo` | MODEL_PATCH | Sim | - | Um patch de modelo especializado que aplica a orientação da rede de controle. |
| `vae` | VAE | Sim | - | O Autoencoder Variacional usado para codificar e decodificar imagens. |
| `força` | FLOAT | Sim | -10.0 a 10.0 | A intensidade da influência da rede de controle. Valores positivos aplicam o efeito, enquanto valores negativos podem invertê-lo (padrão: 1.0). |
| `imagem` | IMAGE | Não | - | Uma imagem base opcional para guiar o processo de geração. |
| `imagem_para_retouch` | IMAGE | Não | - | Uma imagem opcional usada especificamente para inpaint em áreas definidas por uma máscara. |
| `máscara` | MASK | Não | - | Uma máscara opcional que define quais áreas de uma imagem devem ser editadas ou receber inpaint. |

**Observação:** O parâmetro `inpaint_image` é tipicamente usado em conjunto com uma `mask` para especificar o conteúdo do inpaint. O comportamento do nó pode mudar com base em quais entradas opcionais são fornecidas (por exemplo, usando `image` para orientação ou usando `image`, `mask` e `inpaint_image` para inpaint).

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `modelo` | MODEL | O modelo com o patch da rede de controle aplicado, pronto para uso em um pipeline de amostragem. |
| `positive` | CONDITIONING | O condicionamento positivo, potencialmente modificado pelas entradas da rede de controle. |
| `negative` | CONDITIONING | O condicionamento negativo, potencialmente modificado pelas entradas da rede de controle. |

---
**Source fingerprint (SHA-256):** `465f9eb0dd60af23e6cdc2031579e404b4fed021738e592ee6acbb6ee57e83a0`
