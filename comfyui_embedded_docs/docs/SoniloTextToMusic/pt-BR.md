> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloTextToMusic/pt-BR.md)

Aqui está a tradução da documentação para português brasileiro, seguindo as regras estabelecidas:

O nó Sonilo Text to Music gera música a partir de uma descrição textual usando o modelo de IA da Sonilo. Você fornece um prompt descrevendo a música desejada, e o nó envia uma solicitação ao serviço Sonilo para criar um arquivo de áudio. Você pode especificar uma duração alvo ou deixar o modelo inferi-la a partir do seu prompt.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `prompt` | STRING | Sim | N/A | Prompt textual descrevendo a música a ser gerada. Este é um campo obrigatório. |
| `duration` | INT | Não | 0 a 360 | Duração alvo em segundos. Defina como 0 para permitir que o modelo infira a duração a partir do prompt. Máximo: 6 minutos (360 segundos). Padrão: 0. |
| `seed` | INT | Não | 0 a 18446744073709551615 | Semente para reprodutibilidade. Atualmente ignorada pelo serviço Sonilo, mas mantida para consistência do grafo. Padrão: 0. |

**Observação:** A entrada `seed` é fornecida para consistência do fluxo de trabalho, mas atualmente não afeta a saída do serviço Sonilo.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `audio` | AUDIO | A música gerada como um arquivo de áudio. |

---
**Source fingerprint (SHA-256):** `aac2762d9310179279ed7dcc9766f38342400902de2f8791b78d8092a96b86b4`
