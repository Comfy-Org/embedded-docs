# SeedVR2TemporalChunk

Este nó divide um latent de vídeo SeedVR2 em partes temporais menores que podem ser processadas uma de cada vez dentro da VRAM disponível. Ele calcula automaticamente o tamanho ideal da parte com base na memória da sua GPU ou permite que você especifique o tamanho da parte manualmente, e gera as partes em ordem sequencial para processamento.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-----------|---------------|-------------|-------|
| `latent` | O latent SeedVR2 codificado por VAE a ser dividido. | LATENT | Sim | - |
| `temporal_overlap` | Quadros latentes compartilhados entre partes adjacentes e mesclados com crossfade na junção; 0 significa sem sobreposição (padrão: 0). | INT | Não | 0 a 16384 |
| `chunking_mode` | Manual usa exatamente frames_per_chunk; auto prevê a maior parte que cabe na VRAM livre. | COMBO | Sim | "auto"<br>"manual" |

Quando `chunking_mode` está definido como "manual", um parâmetro adicional fica disponível:

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-----------|---------------|-------------|-------|
| `frames_per_chunk` | Quadros de pixel por parte temporal. Deve ser um valor 4n+1 (1, 5, 9, 13, 17, 21, ...) (padrão: 21). | INT | Sim | 1 a 16384 |

Nota: O parâmetro `frames_per_chunk` só aparece quando `chunking_mode` está definido como "manual". O valor deve satisfazer a fórmula `(frames_per_chunk - 1) % 4 == 0`, ou seja, deve ser um dos seguintes: 1, 5, 9, 13, 17, 21, etc.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `latents` | As partes temporais em ordem sequencial. | LATENT |
| `temporal_overlap` | A sobreposição efetiva de quadros latentes entre partes adjacentes, para o nó Merge SeedVR2 Latents. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalChunk/pt-BR.md)

---
**Source fingerprint (SHA-256):** `40af2b690f74555efbe38f4cf76825417f52735ce90296a9ad662f78cfe4c6bf`
