# Visão Geral

Anexe imagens de referência tanto ao condicionamento positivo quanto ao negativo. Este nó permite fornecer uma ou mais imagens de referência que serão usadas para guiar o processo de geração de imagem, seja para edição baseada em instruções ou para personalização orientada por assunto.

# Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positivo` | O condicionamento positivo ao qual anexar as imagens de referência. | CONDITIONING | Sim | - |
| `negativo` | O condicionamento negativo ao qual anexar as imagens de referência. | CONDITIONING | Sim | - |
| `imagens` | Imagens de referência. 1 imagem permite edição baseada em instruções; 2 a 10 imagens permitem personalização orientada por assunto com múltiplas referências. | IMAGE | Sim | 1 a 10 imagens |

**Observação sobre o parâmetro `images`:** Esta é uma entrada de crescimento automático que aceita entre 1 e 10 imagens. As imagens são identificadas como `image_1` até `image_10`. Você deve fornecer pelo menos 1 imagem. O número de imagens determina o modo de operação: uma única imagem é usada para instruções de edição, enquanto múltiplas imagens (2 a 10) são usadas para personalização orientada por assunto.

# Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | O condicionamento positivo com as imagens de referência anexadas. | CONDITIONING |
| `negativo` | O condicionamento negativo com as imagens de referência anexadas. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1ReferenceImages/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b14a8fc2acd44618370bd7e94758d469ff37530f2e19498a6c72ee3748559303`
