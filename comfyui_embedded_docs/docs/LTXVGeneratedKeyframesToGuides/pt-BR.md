# LTXV Keyframes Gerados para Guias

O nó LTXV Generated Keyframes to Guides fixa keyframes gerados de um estágio anterior como guias de imagem congeladas em um canvas posterior. Ele decodifica os keyframes como frames independentes, redimensiona-os se necessário e os grava com uma máscara de ruído 0 para que não passem por denoising novamente. Após um upscale temporal, os índices registrados são reescalados do canvas em que foram gerados para este; use `override_frame_indices` para definir posições explicitamente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `positive` | Condicionamento positivo ao qual adicionar as guias de keyframes. | CONDITIONING | Sim | |
| `negative` | Condicionamento negativo ao qual adicionar as guias de keyframes. | CONDITIONING | Sim | |
| `vae` | A VAE usada para decodificar os keyframes se for necessário redimensionamento. | VAE | Sim | |
| `latent` | O latent de vídeo de destino ao qual adicionar as guias, por exemplo, o que passou por upscale temporal. | LATENT | Sim | |
| `keyframes` | A saída keyframes de LTXV Separate Generated Keyframes, que carrega o índice do frame em pixels no qual cada keyframe foi gerado. | LATENT | Sim | |
| `strength` | Força da guia. 1.0 é uma fixação rígida; valores menores a relaxam. (padrão: 1.0) | FLOAT | Sim | 0.0 - 10.0 (passo 0.01) |
| `override_frame_indices` | Opcional — fixar nesses frames em pixels em vez das posições registradas (ou escaladas automaticamente). Forneça um índice por keyframe. Deixe vazio para reutilizar as posições registradas ou para escalá-las quando o canvas de destino tiver um comprimento diferente (por exemplo, após x2 temporal). (padrão: "") | STRING | Não | |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-----------|-----------|
| `positive` | Condicionamento positivo com os keyframes fixados como guias de imagem. | CONDITIONING |
| `negative` | Condicionamento negativo com os keyframes fixados como guias de imagem. | CONDITIONING |
| `latent` | Latent de vídeo de destino com os keyframes adicionados como guias congeladas. | LATENT |

## Notas

- A entrada `keyframes` deve estar conectada à saída keyframes de LTXV Separate Generated Keyframes. O nó gera um erro se o latent não carregar posições de keyframes gerados.
- As entradas de condicionamento `positive` e `negative` devem vir das saídas positive e negative de LTXV Separate Generated Keyframes. O nó gera um erro se o condicionamento positivo ainda carregar keyframes gerados.
- A entrada `latent` deve ser um latent de vídeo simples (tensor 5D). As guias devem ser adicionadas antes de mesclar os latents de vídeo e áudio com Concat AV Latent.
- Apenas tamanho de lote 1 é suportado. Cada guia é codificada a partir de uma imagem, portanto não pode variar entre elementos do lote.
- O número de keyframes no latent `keyframes` deve corresponder ao número de posições registradas; caso contrário, um erro será gerado.
- Se `override_frame_indices` for deixado vazio, as posições registradas serão usadas. Se o canvas de destino tiver um número de frames diferente do canvas em que os keyframes foram gerados, os índices registrados serão escalados automaticamente.
- Se `override_frame_indices` for fornecido, ele deve conter um índice inteiro por keyframe, separado por vírgulas ou espaços. Os índices devem ser únicos e estar entre 1 e (número de frames em pixels no latent de destino - 1). Caso contrário, um erro será gerado.
- Se qualquer índice final de keyframe for maior ou igual ao número de frames em pixels no latent de destino, o nó gera um erro. Isso pode acontecer quando o destino foi redimensionado temporalmente após os keyframes serem gerados.
- O parâmetro `strength` tem um mínimo de 0.0 e um máximo de 10.0.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVGeneratedKeyframesToGuides/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b5dbf302fad5a7ffd3522d468d1a51b993145d90277592058315499f08e17e7b`
