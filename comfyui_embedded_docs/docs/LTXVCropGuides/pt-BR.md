> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/pt-BR.md)

O nó LTXVCropGuides processa entradas de condicionamento e latentes para geração de vídeo, removendo informações de keyframes e ajustando as dimensões latentes. Ele recorta a imagem latente e a máscara de ruído para excluir seções de keyframes, enquanto limpa os índices de keyframes das entradas de condicionamento positivo e negativo. Isso prepara os dados para fluxos de trabalho de geração de vídeo que não exigem orientação por keyframes.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `positive` | CONDITIONING | Sim | - | A entrada de condicionamento positivo contendo informações de orientação para a geração |
| `negative` | CONDITIONING | Sim | - | A entrada de condicionamento negativo contendo informações sobre o que evitar na geração |
| `latent` | LATENT | Sim | - | A representação latente contendo amostras de imagem e dados de máscara de ruído |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `positive` | CONDITIONING | O condicionamento positivo processado com índices de keyframes e entradas de atenção guiada limpos |
| `negative` | CONDITIONING | O condicionamento negativo processado com índices de keyframes e entradas de atenção guiada limpos |
| `latent` | LATENT | A representação latente recortada com amostras e máscara de ruído ajustadas, onde as seções de keyframes foram removidas |

---
**Source fingerprint (SHA-256):** `029309c260e09221cc9a046897589d99498f6e8ad984ef6052e50be9a0ea7b6d`
