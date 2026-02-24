> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBlend/pt-BR.md)

O nó LatentBlend combina duas amostras latentes mesclando-as usando um fator de mesclagem especificado. Ele recebe duas entradas latentes e cria uma nova saída onde a primeira amostra é ponderada pelo fator de mesclagem e a segunda amostra é ponderada pelo inverso. Se as amostras de entrada tiverem formas diferentes, a segunda amostra será redimensionada automaticamente para corresponder às dimensões da primeira amostra.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `samples1` | LATENT | Sim | - | A primeira amostra latente a ser mesclada |
| `samples2` | LATENT | Sim | - | A segunda amostra latente a ser mesclada |
| `blend_factor` | FLOAT | Sim | 0 a 1 | Controla a proporção de mesclagem entre as duas amostras (padrão: 0.5) |

**Observação:** Se `samples1` e `samples2` tiverem formas diferentes, `samples2` será redimensionada automaticamente para corresponder às dimensões de `samples1` usando interpolação bicúbica com recorte central.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `latent` | LATENT | A amostra latente mesclada que combina ambas as amostras de entrada |
