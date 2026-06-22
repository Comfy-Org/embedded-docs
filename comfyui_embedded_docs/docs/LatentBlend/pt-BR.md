# Latent Blend

O nó LatentBlend combina duas amostras latentes mesclando-as usando um fator de mistura especificado. Ele recebe duas entradas latentes e cria uma nova saída onde a primeira amostra é ponderada pelo fator de mistura e a segunda amostra é ponderada pelo inverso. Se as amostras de entrada tiverem formatos diferentes, a segunda amostra é redimensionada automaticamente para corresponder às dimensões da primeira amostra.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `amostras1` | A primeira amostra latente a ser mesclada | LATENT | Sim | - |
| `amostras2` | A segunda amostra latente a ser mesclada | LATENT | Sim | - |
| `fator_de_mistura` | Controla a proporção de mesclagem entre as duas amostras (padrão: 0.5) | FLOAT | Sim | 0 a 1 |

**Nota:** Se `samples1` e `samples2` tiverem formatos diferentes, `samples2` será redimensionado automaticamente para corresponder às dimensões de `samples1` usando interpolação bicúbica com recorte central.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `latent` | A amostra latente mesclada combinando ambas as amostras de entrada | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBlend/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a19808c5b606a8c05f2685fcd78d9f08c1ba51613a4029b36cf0ce5305618c2f`
