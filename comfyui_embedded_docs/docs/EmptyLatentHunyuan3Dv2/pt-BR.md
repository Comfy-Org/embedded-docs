# EmptyLatentHunyuan3Dv2

O nó EmptyLatentHunyuan3Dv2 cria tensores latentes vazios especificamente formatados para os modelos de geração 3D Hunyuan3Dv2. Ele gera espaços latentes vazios com as dimensões e a estrutura corretas exigidas pela arquitetura Hunyuan3Dv2, permitindo que você inicie fluxos de trabalho de geração 3D do zero. O nó produz tensores latentes preenchidos com zeros que servem como base para os processos subsequentes de geração 3D.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `resolução` | A dimensão da resolução para o espaço latente (padrão: 3072) | INT | Sim | 1 - 8192 |
| `tamanho_do_lote` | O número de imagens latentes no lote (padrão: 1) | INT | Sim | 1 - 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `LATENT` | Retorna um tensor latente contendo amostras vazias marcadas com o tipo "hunyuan3dv2", formatado para a geração 3D do Hunyuan3Dv2 | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentHunyuan3Dv2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e9061301341ab84290cd2b16d5307636310a0772562cf485e3444876e4786ddd`
