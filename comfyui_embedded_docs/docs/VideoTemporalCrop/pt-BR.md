# Cortar Vídeo (Temporal)

Este nó corta um intervalo contínuo de quadros de um vídeo. Ele funciona de forma totalmente preguiçosa, o que significa que só processa a parte selecionada do vídeo conforme necessário posteriormente no fluxo de trabalho.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `vídeo` | Vídeo de entrada. | VIDEO | Sim | – |
| `quadro_inicial` | Índice do quadro inicial (padrão: 0). | INT | Sim | 0 a 99999 |
| `comprimento` | Número de quadros a manter (padrão: 16). | INT | Sim | 1 a 99999 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `vídeo` | Vídeo cortado (preguiçoso). | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTemporalCrop/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1d28a55399c9fe7ca47f0aaa872751ac89c5419a6f6be6636fbf7f020a02749d`
