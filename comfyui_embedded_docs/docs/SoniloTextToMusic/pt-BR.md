# Sonilo Texto para Música

O nó Sonilo Text to Music gera música a partir de uma descrição textual usando o modelo de IA da Sonilo. Você fornece um prompt descrevendo a música desejada, e o nó envia uma solicitação ao serviço Sonilo para criar um arquivo de áudio. Você também pode especificar a duração alvo da música gerada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto descrevendo a música a ser gerada. Deve conter entre 1 e 1000 caracteres. | STRING | Sim | 1 a 1000 caracteres |
| `duration` | Duração alvo em segundos. Máximo: 6 minutos. Padrão: 30. | INT | Não | 1 a 360 |
| `seed` | Semente para reprodutibilidade. Atualmente ignorada pelo serviço Sonilo, mas mantida para consistência do grafo. Padrão: 0. | INT | Não | 0 a 18446744073709551615 |

**Nota:** O parâmetro `seed` é fornecido para consistência do fluxo de trabalho, mas atualmente não afeta a saída do serviço Sonilo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `audio` | A música gerada como um arquivo de áudio. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloTextToMusic/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9dd1503428b0f23e0fb316ca97e3b64ddf11bcb4a82fc34fd248f481a60c1afe`
