# SeedVR2TemporalMerge

Este nó recombina partes latentes temporais amostradas do SeedVR2 em um único latente de comprimento total. Ele usa uma sobreposição com janela Hann (Hann window crossfade) sobre a região de sobreposição entre as partes para criar transições suaves, ou realiza concatenação simples quando nenhuma sobreposição é especificada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `latents` | As partes temporais amostradas em ordem sequencial. | LATENT | Sim | Lista de latentes |
| `temporal_overlap` | A saída temporal_overlap do nó Dividir Latente SeedVR2. 0 = concatenação simples. (padrão: 0) | INT | Sim | 0 a 16384 |

**Nota:** O valor de `temporal_overlap` deve ser maior ou igual a 0. A parte final da sequência pode ter menos quadros temporais do que as outras partes. Todas as partes devem ter dimensões correspondentes, exceto pelo eixo temporal (T), e a primeira parte deve ser pentadimensional (B, C, T, H, W).

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `latent` | O latente recombindo de comprimento total. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalMerge/pt-BR.md)

---
**Source fingerprint (SHA-256):** `647653fc651462f62bcc9dca2919cfcaa4b476b4c679b0a1111698facab83f28`
