# ZImageFunControlnet

ZImageFunControlnet aplica um patch de rede de controle a um modelo base para que ele possa orientar o processo de geração ou edição de imagens. Ele combina um modelo, um patch de modelo e um VAE, e permite controlar quão fortemente o efeito de controle influencia o resultado. Entradas opcionais de `image`, `inpaint_image` e `mask` permitem edições mais direcionadas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo base usado para o processo de geração. | MODEL | Sim | - |
| `model_patch` | Um patch de modelo especializado que aplica a orientação da rede de controle. | MODEL_PATCH | Sim | - |
| `vae` | O Autoencoder Variacional usado para codificar e decodificar imagens. | VAE | Sim | - |
| `strength` | A força da influência da rede de controle. Valores positivos aplicam o efeito, enquanto valores negativos podem invertê-lo (padrão: 1.0). | FLOAT | Sim | -10.0 a 10.0 (passo 0.01) |
| `image` | Uma imagem base opcional para orientar o processo de geração. | IMAGE | Não | - |
| `inpaint_image` | Uma imagem opcional usada especificamente para inpainting de áreas definidas por uma máscara. | IMAGE | Não | - |
| `mask` | Uma máscara opcional que define quais áreas de uma imagem devem ser editadas ou submetidas a inpainting. | MASK | Não | - |

**Observação:** O parâmetro `inpaint_image` geralmente é usado em conjunto com um `mask` para especificar o conteúdo do inpainting. O comportamento do nó pode mudar dependendo de quais entradas opcionais são fornecidas (por exemplo, usar `image` para orientação ou usar `image`, `mask` e `inpaint_image` para inpainting).

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | O modelo com o patch da rede de controle aplicado, pronto para uso em um pipeline de amostragem. | MODEL |
| `positive` | O condicionamento positivo, potencialmente modificado pelas entradas da rede de controle. | CONDITIONING |
| `negative` | O condicionamento negativo, potencialmente modificado pelas entradas da rede de controle. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e1946190a06c52dd951078d9cb753962081957cb6c38accdea26eb4129a51793`
