# ZImageFunControlnet

O ZImageFunControlnet aplica uma rede de controle especializada para influenciar o processo de geração ou edição de imagens. Ele usa um modelo base, um patch de modelo e um VAE, permitindo ajustar a força do efeito de controle. Este nó pode trabalhar com uma imagem base, uma imagem de inpaint e uma máscara para edições mais direcionadas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo base usado no processo de geração. | MODEL | Sim | - |
| `patch_do_modelo` | Um modelo de patch especializado que aplica a orientação da rede de controle. | MODEL_PATCH | Sim | - |
| `vae` | O Autoencoder Variacional usado para codificar e decodificar imagens. | VAE | Sim | - |
| `força` | A força da influência da rede de controle. Valores positivos aplicam o efeito, enquanto valores negativos podem invertê-lo (padrão: 1.0). | FLOAT | Sim | -10.0 a 10.0 |
| `imagem` | Uma imagem base opcional para orientar o processo de geração. | IMAGE | Não | - |
| `imagem_para_retouch` | Uma imagem opcional usada especificamente para inpaint de áreas definidas por uma máscara. | IMAGE | Não | - |
| `máscara` | Uma máscara opcional que define quais áreas de uma imagem devem ser editadas ou receber inpaint. | MASK | Não | - |

**Nota:** O parâmetro `inpaint_image` é tipicamente usado em conjunto com um `mask` para especificar o conteúdo do inpaint. O comportamento do nó pode mudar dependendo de quais entradas opcionais são fornecidas (por exemplo, usar `image` para orientação ou usar `image`, `mask` e `inpaint_image` para inpaint).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo com o patch da rede de controle aplicado, pronto para uso em um pipeline de amostragem. | MODEL |
| `positive` | O condicionamento positivo, potencialmente modificado pelas entradas da rede de controle. | CONDITIONING |
| `negative` | O condicionamento negativo, potencialmente modificado pelas entradas da rede de controle. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e1946190a06c52dd951078d9cb753962081957cb6c38accdea26eb4129a51793`
