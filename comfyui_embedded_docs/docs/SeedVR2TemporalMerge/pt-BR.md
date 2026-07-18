# SeedVR2TemporalMerge

Este nó recombina partes temporais de dados de vídeo latente que foram previamente divididos pelo nó Split SeedVR2 Latent. Ele utiliza uma sobreposição com janela de Hann para criar uma transição suave entre as partes nas regiões de sobreposição, ou realiza uma concatenação simples quando nenhuma sobreposição é especificada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|--------------|-------------|-------|
| `latents` | As partes temporais amostradas em ordem sequencial. | LATENT | Sim | Lista de latentes |
| `temporal_overlap` | A saída `temporal_overlap` do Split SeedVR2 Latent. 0 = concatenação simples. | INT | Sim | 0 a 16384 (padrão: 0) |

**Nota:** O parâmetro `temporal_overlap` deve ser conectado a partir da saída `temporal_overlap` do nó Split SeedVR2 Latent. Todas as partes latentes de entrada devem ter o mesmo tamanho de lote, número de canais, altura e largura. Apenas a parte final pode ter uma dimensão temporal menor que as demais.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `latent` | O latente de comprimento total recombinado. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalMerge/pt-BR.md)

---
**Source fingerprint (SHA-256):** `647653fc651462f62bcc9dca2919cfcaa4b476b4c679b0a1111698facab83f28`
