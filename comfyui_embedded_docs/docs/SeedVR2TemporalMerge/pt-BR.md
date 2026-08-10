# Unir latentes SeedVR2

Este nó recombina partes latentes temporais amostradas do SeedVR2 em um único latente de comprimento total. Quando uma sobreposição temporal é especificada, ele aplica crossfade com janela de Hann em cada região sobreposta para criar transições suaves entre as partes; quando a sobreposição é 0, realiza concatenação simples.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `latents` | As partes temporais amostradas em ordem sequencial. | LATENT | Sim | Lista de latentes |
| `temporal_overlap` | A saída temporal_overlap do nó Dividir Latente SeedVR2. 0 = concatenação simples. (padrão: 0) | INT | Sim | 0 a 16384 |

**Observação:** O valor de `temporal_overlap` deve ser maior ou igual a 0. Todas as partes devem ser latentes de vídeo 5-dimensionais (B, C, T, H, W) e devem corresponder em todas as dimensões, exceto o eixo temporal (T); apenas a parte final pode ser mais curta que as outras. Se apenas uma parte for fornecida, ela é retornada inalterada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `latent` | O latente recombindo de comprimento total. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalMerge/pt-BR.md)

---
**Source fingerprint (SHA-256):** `647653fc651462f62bcc9dca2919cfcaa4b476b4c679b0a1111698facab83f28`
