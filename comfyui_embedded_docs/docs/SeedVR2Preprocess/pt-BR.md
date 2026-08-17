# Pré-processar entrada SeedVR2

Este nó adiciona padding a uma imagem redimensionada para prepará-la para o modelo SeedVR2. Ele remove o canal alfa durante o processamento, que posteriormente é restaurado pelo nó complementar Post-Process SeedVR2 Output usando a imagem redimensionada original.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `resized_images` | A imagem redimensionada a ser processada. | IMAGE | Sim | - |

Nota: A entrada pode ser uma única imagem ou uma sequência de quadros (por exemplo, quadros de um vídeo). Sua borda mais curta deve ter pelo menos 2 pixels. Durante o processamento, o canal alfa (se presente) é removido, os valores de pixels são limitados ao intervalo [0, 1], e a largura e a altura são ajustadas para múltiplos de 16. Sequências de quadros são preenchidas de modo que seu comprimento siga o padrão 1, 5, 9, 13, ... quadros.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `images` | A imagem preenchida para a codificação VAE. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Preprocess/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f4fa433d299feba40696f27ff365c59988e5102112f09536724b5db5b09416bb`
