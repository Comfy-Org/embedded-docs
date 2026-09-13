# LTXV Separar Keyframes Gerados

## Visão geral

O nó LTXV Separate Generated Keyframes separa de volta os keyframes gerados adicionados por LTXV Add Generated Keyframes de um latent amostrado e os remove do condicionamento. Use-o antes de fazer upscale espacial do latent de vídeo. Não execute LTXV Crop Guides primeiro — ele trata os keyframes gerados como guias descartáveis e os descarta.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `positive` | Condicionamento positivo que contém os metadados dos keyframes gerados. Os metadados são removidos dele na saída. | CONDITIONING | Sim | N/A |
| `negative` | Condicionamento negativo que contém os metadados dos keyframes gerados. Os metadados são removidos dele na saída. | CONDITIONING | Sim | N/A |
| `latent` | Latent de vídeo que contém os keyframes gerados. Os keyframes são removidos dele na saída. | LATENT | Sim | N/A |
| `keyframes_to_batch` | Retorna os keyframes como um lote de latents de quadro único. Deixe desativado para obtê-los como um único latent de múltiplos quadros, que é o que o upsampler de latent e um posterior Add Generated Keyframes esperam. | BOOLEAN | Não | default: False |

### Notas sobre as entradas

- `positive` deve conter metadados de keyframes gerados; caso contrário, o nó gera um erro instruindo você a adicioná-los primeiro com LTXV Add Generated Keyframes.
- `latent` deve ser um latent de vídeo simples (um tensor 5D). Se os latents de vídeo e áudio ainda estiverem combinados, separe-os primeiro com Separate AV Latent.
- O número de tokens por quadro do latent registrado quando os keyframes foram adicionados deve corresponder ao número de tokens por quadro do `latent` fornecido. Se o latent foi redimensionado depois que os keyframes foram adicionados, eles não se alinham mais e o nó gera um erro — separe-os antes de fazer upscale do latent.
- O intervalo de quadros dos keyframes registrado deve caber dentro do `latent` fornecido; caso contrário, o nó gera um erro de que os keyframes foram registrados para um latent diferente.
- O índice da entrada de atenção de guia registrado ainda deve existir no condicionamento. Se o condicionamento foi reconstruído depois que os keyframes foram adicionados, o nó gera um erro.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `positive` | Condicionamento positivo com os metadados dos keyframes gerados removidos. | CONDITIONING |
| `negative` | Condicionamento negativo com os metadados dos keyframes gerados removidos. | CONDITIONING |
| `latent` | Latent de vídeo com os keyframes gerados removidos. | LATENT |
| `keyframes` | Os keyframes separados, rotulados com generated_keyframe_indices e generated_keyframe_num_frames. Forneça-os a um posterior Add Generated Keyframes para inicializar novos slots, ou a Generated Keyframes To Guides para fixá-los como guias de imagem congeladas (os índices são remapeados se o comprimento da tela mudou). | LATENT |

## Notas

- O parâmetro `keyframes_to_batch` determina se os keyframes são retornados como um lote de latents de quadro único ou como um único latent de múltiplos quadros.
- O nó garante que os keyframes gerados sejam removidos do condicionamento e do latent antes de qualquer processamento adicional.
- A saída `keyframes` pode ser usada para inicializar novos slots para keyframes gerados ou para fixá-los como guias de imagem congeladas.
- O nó gera um `ValueError` se o latent não contiver keyframes gerados ou se os keyframes não corresponderem ao formato esperado.
- O nó assume que os keyframes gerados foram adicionados usando o nó LTXV Add Generated Keyframes e que são compatíveis com o latent atual.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateGeneratedKeyframes/pt-BR.md)

---
**Source fingerprint (SHA-256):** `295e49181e87445a1c47b2e9413d95b20585b12e89f26f13129ac5d97f913007`
