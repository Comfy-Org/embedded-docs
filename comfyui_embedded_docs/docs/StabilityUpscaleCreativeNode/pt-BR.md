> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleCreativeNode/pt-BR.md)

Aumenta a resolução da imagem com alterações mínimas para 4K. Este nó utiliza a tecnologia de upscaling criativo da Stability AI para melhorar a resolução da imagem, preservando o conteúdo original e adicionando detalhes criativos sutis.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `imagem` | IMAGE | Sim | - | A imagem de entrada a ser ampliada |
| `prompt` | STRING | Sim | - | O que você deseja ver na imagem de saída. Um prompt forte e descritivo que defina claramente elementos, cores e assuntos levará a melhores resultados. (padrão: string vazia) |
| `criatividade` | FLOAT | Sim | 0.1-0.5 | Controla a probabilidade de criar detalhes adicionais que não são fortemente condicionados pela imagem inicial. (padrão: 0.3) |
| `estilo_predefinido` | STRING | Sim | `"3d-model"`<br>`"analog-film"`<br>`"anime"`<br>`"cinematic"`<br>`"comic-book"`<br>`"digital-art"`<br>`"enhance"`<br>`"fantasy-art"`<br>`"isometric"`<br>`"line-art"`<br>`"low-poly"`<br>`"modeling-compound"`<br>`"neon-punk"`<br>`"origami"`<br>`"photographic"`<br>`"pixel-art"`<br>`"tile-texture"` | Estilo desejado opcional da imagem gerada. (padrão: "None") |
| `semente` | INT | Sim | 0-4294967294 | A semente aleatória usada para criar o ruído. (padrão: 0) |
| `prompt_negativo` | STRING | Não | - | Palavras-chave do que você NÃO deseja ver na imagem de saída. Este é um recurso avançado. (padrão: string vazia) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `imagem` | IMAGE | A imagem ampliada na resolução 4K |

---
**Source fingerprint (SHA-256):** `46f7bdd3cb4254b6305407f43e4a9a69a54fd3a0ac285d784c899dbf52edd552`
