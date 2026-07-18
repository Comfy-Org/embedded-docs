# SeedVR2TemporalChunk

Este nó divide um latent de vídeo SeedVR2 em partes temporais menores e sobrepostas que podem ser processadas uma de cada vez dentro da VRAM disponível. As partes são projetadas para serem passadas tanto para o nó Apply SeedVR2 Conditioning quanto para a entrada latent do sampler, e posteriormente recombinadas usando o nó Merge SeedVR2 Latents.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `latent` | O latent SeedVR2 codificado por VAE a ser dividido | LATENT | Sim | - |
| `temporal_overlap` | Quadros latentes compartilhados entre partes adjacentes e com crossfade na mesclagem; 0 significa sem sobreposição (padrão: 0) | INT | Não | 0 a 16384 |
| `chunking_mode` | manual = usa frames_per_chunk exatamente; auto = prevê a maior parte que cabe na VRAM livre | COMBO | Sim | "auto"<br>"manual" |

Quando `chunking_mode` está definido como "manual", o seguinte parâmetro fica disponível:

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `frames_per_chunk` | Quadros de pixel por parte temporal (deve ser 4n+1: 1, 5, 9, 13, ...) (padrão: 21) | INT | Sim | 1 a 16384, passo 4 |

**Observações sobre restrições de parâmetros:**
- O `latent` de entrada deve ser um latent de vídeo 5-dimensional com formato (B, C, T, H, W) e exatamente 4 canais latentes
- Ao usar o modo "manual", `frames_per_chunk` deve ser um valor 4n+1 (1, 5, 9, 13, 17, 21, ...)
- `temporal_overlap` é automaticamente limitado para ser menor que o tamanho da parte
- No modo "auto", o nó calcula o tamanho ideal da parte com base na VRAM livre disponível

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `latents` | As partes temporais em ordem sequencial | LATENT |
| `temporal_overlap` | A sobreposição efetiva de quadros latentes entre partes adjacentes, para o Merge SeedVR2 Latents | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalChunk/pt-BR.md)

---
**Source fingerprint (SHA-256):** `40af2b690f74555efbe38f4cf76825417f52735ce90296a9ad662f78cfe4c6bf`
