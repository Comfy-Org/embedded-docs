# CLIPTextEncodeKandinsky5

O nó CLIPTextEncodeKandinsky5 prepara prompts de texto para uso com o modelo Kandinsky 5. Ele recebe duas entradas de texto separadas, as tokeniza usando um modelo CLIP fornecido e as combina em uma única saída de condicionamento. Essa saída é usada para guiar o processo de geração de imagens.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP usado para tokenizar e codificar os prompts de texto. | CLIP | Sim |  |
| `clip_l` | O prompt de texto principal. Esta entrada suporta texto multilinha e prompts dinâmicos. | STRING | Sim |  |
| `qwen25_7b` | Um prompt de texto secundário. Esta entrada suporta texto multilinha e prompts dinâmicos. | STRING | Sim |  |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `CONDITIONING` | Os dados de condicionamento combinados gerados a partir de ambos os prompts de texto, prontos para serem alimentados em um modelo Kandinsky 5 para geração de imagens. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeKandinsky5/pt-BR.md)

---
**Source fingerprint (SHA-256):** `80227cf87d46bfa42b07976ab29996ae9583a4c461b2f2408db4b7016d3e1a0c`
