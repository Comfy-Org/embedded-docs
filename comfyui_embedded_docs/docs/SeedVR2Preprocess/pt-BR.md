# Pré-processar entrada SeedVR2

Este nó prepara uma imagem ou vídeo redimensionado para o modelo SeedVR2, aplicando preenchimento (padding) até a forma esperada pelo modelo. Ele remove o canal alfa durante o processamento; o nó complementar Post-Process SeedVR2 Output o restaura posteriormente a partir da imagem redimensionada original. Os valores de pixel são limitados ao intervalo 0-1, a altura e a largura são preenchidas até múltiplos de 16, e a contagem de quadros é ampliada repetindo o último quadro quando necessário.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `resized_images` | A imagem redimensionada a ser processada. | IMAGE | Sim | - |

Nota: A entrada pode ser um único quadro, uma sequência de quadros ou um lote de vídeos. Se tiver mais de 3 canais, o canal alfa é removido e apenas o RGB é mantido. O lado menor da entrada deve ter pelo menos 2 pixels. O preenchimento espacial é preenchido com preto (valor 0), e contagens válidas de quadros seguem um padrão 4n+1 (1, 5, 9, 13, ...).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `images` | A imagem preenchida para codificação VAE. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Preprocess/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f4fa433d299feba40696f27ff365c59988e5102112f09536724b5db5b09416bb`
