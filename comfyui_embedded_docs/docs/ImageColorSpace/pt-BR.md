# Converter Espaço de Cor da Imagem

O nó ImageColorSpace converte imagens entre os espaços de cor sRGB (Rec.709), linear Rec.709, HDR (Rec.2020 HLG), HDR PQ (Rec.2020 PQ), HDR LogC3 e HDR ACEScct. LogC3 usa a curva EI 800 com primárias Rec.709 e códigos limitados a [0, 1]; ACEScct usa primárias AP1 e branco D60, com adaptação Bradford para D65. Ao converter para saída SDR, ou de HDR PQ para HDR, ele aplica tone mapping à luminância excedente em todo o lote e comprime cores fora da gama; saídas linear e ACEScct, e conversões de linear para HDR, preservam valores estendidos. Saídas HLG e PQ recortam canais negativos. As conversões são calculadas em float32, e qualquer canal alfa é passado sem alterações.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem de entrada a ser convertida. | IMAGE | Sim | Qualquer imagem válida. |
| `source` | Espaço de cor dos pixels de entrada. Padrão: `"sRGB"`. | COMBO | Sim | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"`<br>`"linear"`<br>`"HDR LogC3"`<br>`"HDR ACEScct"` |
| `destination` | Espaço de cor dos pixels de saída. Configure o nó de salvamento para este mesmo espaço de cor. Converta LogC3 ou ACEScct para linear antes de salvar EXR, ou para sRGB/HDR/HDR PQ antes de salvar vídeo. Padrão: `"sRGB"`. | COMBO | Sim | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"`<br>`"linear"`<br>`"HDR LogC3"`<br>`"HDR ACEScct"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem convertida no espaço de cor de destino especificado. | IMAGE |

## Notas

- Linear 1.0 usa o mesmo branco de referência de 203 nits que sRGB; HLG usa uma exibição de referência de 1000 nits.
- Saídas linear e ACEScct preservam valores estendidos; conversões de linear para HDR preservam realces sem tone mapping.
- Saída SDR e conversão de PQ para HLG aplicam tone mapping à luminância excedente em todo o lote (compartilhando um ponto de branco para que a exposição não mude quadro a quadro) e comprimem cores fora da gama. Saídas HLG e PQ recortam canais negativos.
- As conversões são calculadas em float32 e retornam o dispositivo e dtype intermediários.
- LogC3 e ACEScct são codificações log de câmera: converta-os para linear para salvar em EXR, ou para sRGB/HDR/HDR PQ antes de salvar em vídeo.
- O alfa straight não é transformado em cor; apenas os canais RGB são convertidos.
- Se `source` e `destination` forem iguais, nenhuma transformação de cor é aplicada — a imagem é apenas movida para o dispositivo e dtype intermediários.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorSpace/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fdf8b4f16a1e0c7ff9a86b8cc40f6f796175205e4b1f491b595a74a8456b9b94`
