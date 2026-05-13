> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeKandinsky5/pt-BR.md)

O nó CLIPTextEncodeKandinsky5 prepara prompts de texto para uso com o modelo Kandinsky 5. Ele recebe duas entradas de texto separadas, as tokeniza usando um modelo CLIP fornecido e as combina em uma única saída de condicionamento. Essa saída é usada para guiar o processo de geração de imagens.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `clip` | CLIP | Sim | | O modelo CLIP usado para tokenizar e codificar os prompts de texto. |
| `clip_l` | STRING | Sim | | O prompt de texto principal. Esta entrada suporta texto multilinha e prompts dinâmicos. |
| `qwen25_7b` | STRING | Sim | | Um prompt de texto secundário. Esta entrada suporta texto multilinha e prompts dinâmicos. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `CONDITIONING` | CONDITIONING | Os dados de condicionamento combinados gerados a partir de ambos os prompts de texto, prontos para serem alimentados em um modelo Kandinsky 5 para geração de imagens. |

---
**Source fingerprint (SHA-256):** `80227cf87d46bfa42b07976ab29996ae9583a4c461b2f2408db4b7016d3e1a0c`
