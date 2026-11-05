# Pika SFX

Este nó gera um efeito sonoro a partir de uma descrição textual com o Pika. Descreva o som e por quanto tempo ele deve durar, e o nó retorna um clipe de áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descrição do efeito sonoro desejado. Não pode estar vazio. Padrão: "" (string vazia). | STRING | Sim | 1 a 4000 caracteres |
| `duration` | Duração do efeito sonoro em segundos. Padrão: 5.0. | FLOAT | Sim | 1.0 a 20.0 (passo: 0.1) |
| `seed` | Semente para amostragem. Padrão: 42. | INT | Sim | 0 a 2147483647 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `AUDIO` | O efeito sonoro gerado. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaSFXNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a1dcd374d158009aceae2aecd87ed08f8105bff7db75160a99e8624be9459dfa`
