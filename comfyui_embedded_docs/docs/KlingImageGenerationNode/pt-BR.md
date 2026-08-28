# Geração de Imagem Kling

O nó Kling Image Generation gera imagens a partir de prompts de texto, com a opção de usar uma imagem de referência como guia. Ele cria uma ou mais imagens com base na sua descrição de texto e nas configurações de referência e retorna as imagens geradas como saída.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto positivo | STRING | Sim | Máximo de 500 caracteres |
| `negative_prompt` | Prompt de texto negativo | STRING | Sim | Máximo de 500 caracteres |
| `image_type` | Seleção do tipo de referência de imagem (avançado). Obrigatório quando uma imagem de referência é fornecida. | COMBO | Sim | `"subject_reference"`<br>`"style_reference"` |
| `image_fidelity` | Intensidade da referência para imagens enviadas pelo usuário (padrão: 0.5, avançado) | FLOAT | Sim | 0.0 - 1.0 |
| `human_fidelity` | Similaridade da referência de assunto (padrão: 0.45, avançado) | FLOAT | Sim | 0.0 - 1.0 |
| `model_name` | Seleção do modelo para geração de imagens (padrão: "kling-v3") | COMBO | Sim | `"kling-v3"` |
| `aspect_ratio` | Proporção de aspecto para as imagens geradas (padrão: "16:9") | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` |
| `n` | Número de imagens geradas (padrão: 1) | INT | Sim | 1 - 9 |
| `image` | Imagem de referência opcional | IMAGE | Não | - |
| `semente` | O parâmetro `seed` controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente (padrão: 0) | INT | Não | 0 - 2147483647 |

**Restrições dos Parâmetros:**

- O parâmetro `image` é opcional. Quando uma imagem de referência é fornecida, o parâmetro `image_type` determina se a referência é usada como referência de assunto ou referência de estilo.
- Quando nenhuma imagem de referência é fornecida, as configurações relacionadas à referência (`image_type`, `image_fidelity`, `human_fidelity`) não têm efeito no resultado.
- `prompt` e `negative_prompt` têm comprimento máximo de 500 caracteres.
- O parâmetro `seed` é opcional e não garante resultados determinísticos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | Imagem(ns) gerada(s) com base nos parâmetros de entrada. Quando `n` é maior que 1, várias imagens são retornadas como um lote. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fd344519346f63ac03975b93f03725749ed9697245d6dfa2378884c59a5325cd`
