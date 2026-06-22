# EmptyLatentHunyuan3Dv2

O nó EmptyLatentHunyuan3Dv2 cria tensores latentes vazios especificamente formatados para modelos de geração 3D Hunyuan3Dv2. Ele gera espaços latentes vazios com as dimensões e estrutura corretas exigidas pela arquitetura Hunyuan3Dv2, permitindo iniciar fluxos de trabalho de geração 3D do zero. O nó produz tensores latentes preenchidos com zeros que servem como base para processos subsequentes de geração 3D.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `resolução` | A dimensão de resolução para o espaço latente (padrão: 3072) | INT | Sim | 1 - 8192 |
| `tamanho_do_lote` | O número de imagens latentes no lote (padrão: 1) | INT | Sim | 1 - 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `LATENT` | Retorna um tensor latente contendo amostras vazias formatadas para geração 3D Hunyuan3Dv2 | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentHunyuan3Dv2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f912b226bcec4e2edd52250682d0583ab378b5502173f8e027e0e8fbff1db08f`
