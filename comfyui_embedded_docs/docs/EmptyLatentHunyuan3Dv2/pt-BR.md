# EmptyLatentHunyuan3Dv2

Este nó cria um lote de amostras latentes vazias (preenchidas com zeros) formatadas para modelos de geração 3D Hunyuan3Dv2. Ele produz o tensor latente com o formato correto que serve como ponto de partida para fluxos de trabalho de geração 3D, com o tensor latente marcado como tipo "hunyuan3dv2".

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `resolution` | A dimensão de resolução do espaço latente a ser criada (padrão: 3072) | INT | Sim | 1 - 8192 |
| `batch_size` | O número de imagens latentes no lote (padrão: 1) | INT | Sim | 1 - 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `LATENT` | Um tensor latente vazio de formato [batch_size, 64, resolution] contendo amostras preenchidas com zeros, marcado com o tipo "hunyuan3dv2" | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentHunyuan3Dv2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e9061301341ab84290cd2b16d5307636310a0772562cf485e3444876e4786ddd`
