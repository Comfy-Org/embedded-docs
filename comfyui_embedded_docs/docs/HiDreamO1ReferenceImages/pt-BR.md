# Imagens de Referência HiDream-O1

## Visão Geral

Anexe imagens de referência ao condicionamento positivo e negativo. Este nó permite fornecer uma ou mais imagens de referência que serão usadas para guiar o processo de geração de imagem, seja para edição com base em uma instrução ou para personalização orientada por assunto.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | O condicionamento positivo ao qual anexar as imagens de referência. | CONDITIONING | Sim | - |
| `negative` | O condicionamento negativo ao qual anexar as imagens de referência. | CONDITIONING | Sim | - |
| `images` | Imagens de referência. 1 imagem = edição por instrução; 2 a 10 imagens = múltiplas referências. | IMAGE | Sim | 1 to 10 images |

**Observação sobre o parâmetro `images`:** Esta é uma entrada de crescimento automático que aceita entre 1 e 10 imagens. As imagens são rotuladas como `image_1` a `image_10`. Você deve fornecer pelo menos 1 imagem. O número de imagens determina o modo de operação: uma única imagem é usada para instruções de edição, enquanto múltiplas imagens (2-10) são usadas para personalização orientada por assunto.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | O condicionamento positivo com as imagens de referência anexadas. | CONDITIONING |
| `negative` | O condicionamento negativo com as imagens de referência anexadas. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1ReferenceImages/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f05f6be19df8b8697a98507163e8f60fd0cf2048c81f92597d2ae0a3395b8c6d`
