# Geração de Imagem Kling

Este documento foi gerado por IA. Se encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/en.md)

O Nó de Geração de Imagens Kling gera imagens a partir de prompts de texto, com a opção de usar uma imagem de referência como guia. Ele cria uma ou mais imagens com base na sua descrição textual e nas configurações de referência, retornando as imagens geradas como saída.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt de texto positivo | STRING | Sim | - |
| `negative_prompt` | Prompt de texto negativo | STRING | Sim | - |
| `image_type` | Seleção do tipo de referência de imagem (avançado). Obrigatório quando uma imagem de referência é fornecida. | COMBO | Sim | `"subject_reference"`<br>`"style_reference"` |
| `image_fidelity` | Intensidade da referência para imagens enviadas pelo usuário (padrão: 0.5, avançado) | FLOAT | Sim | 0.0 - 1.0 |
| `human_fidelity` | Similaridade da referência ao sujeito (padrão: 0.45, avançado) | FLOAT | Sim | 0.0 - 1.0 |
| `model_name` | Seleção do modelo para geração de imagens (padrão: "kling-v3") | COMBO | Sim | `"kling-v3"`<br>`"kling-v2"`<br>`"kling-v1-5"` |
| `aspect_ratio` | Proporção de aspecto para as imagens geradas (padrão: "16:9") | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` |
| `n` | Número de imagens geradas (padrão: 1) | INT | Sim | 1 - 9 |
| `image` | Imagem de referência opcional | IMAGE | Não | - |
| `semente` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente (padrão: 0) | INT | Não | 0 - 2147483647 |

**Restrições dos Parâmetros:**

- O parâmetro `image` é opcional. Quando uma imagem de referência é fornecida, o parâmetro `image_type` deve ser definido como `"subject_reference"` ou `"style_reference"`.
- Quando nenhuma imagem de referência é fornecida, os parâmetros `image_type`, `image_fidelity` e `human_fidelity` não são utilizados.
- O prompt e o prompt negativo têm um comprimento máximo de `MAX_PROMPT_LENGTH_IMAGE_GEN` caracteres.
- O parâmetro `seed` é opcional e não garante resultados determinísticos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | Imagem(ns) gerada(s) com base nos parâmetros de entrada | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f25164f4007b1f62285e76519238b5061b63597e1a06365acf93d4289063bd3a`
