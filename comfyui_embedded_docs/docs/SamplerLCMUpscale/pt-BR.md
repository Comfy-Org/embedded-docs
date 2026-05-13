> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/pt-BR.md)

O nó SamplerLCMUpscale fornece um método de amostragem especializado que combina a amostragem do Modelo de Consistência Latente (LCM) com capacidades de redimensionamento de imagem. Ele permite redimensionar imagens durante o processo de amostragem usando vários métodos de interpolação, sendo útil para gerar saídas de maior resolução enquanto mantém a qualidade da imagem.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `scale_ratio` | FLOAT | Não | 0,1 - 20,0 | O fator de escala a ser aplicado durante o redimensionamento (padrão: 1,0) |
| `scale_steps` | INT | Não | -1 - 1000 | O número de etapas a serem usadas no processo de redimensionamento. Use -1 para cálculo automático (padrão: -1) |
| `upscale_method` | COMBO | Sim | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" | O método de interpolação usado para redimensionar a imagem |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `sampler` | SAMPLER | Retorna um objeto de amostragem configurado que pode ser usado no pipeline de amostragem |

---
**Source fingerprint (SHA-256):** `fe0d4c8676454a9e8ecf4bb4e149c9b5e22083322447749116d624984d75e73c`
