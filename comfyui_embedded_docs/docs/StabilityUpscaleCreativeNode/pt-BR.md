Aumenta a resolução da imagem com alterações mínimas para 4K. Este nó utiliza a tecnologia de upscaling criativo da Stability AI para melhorar a resolução da imagem, preservando o conteúdo original e adicionando detalhes criativos sutis.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `imagem` | A imagem de entrada a ser ampliada | IMAGE | Sim | - |
| `prompt` | O que você deseja ver na imagem de saída. Um prompt forte e descritivo que defina claramente elementos, cores e assuntos levará a melhores resultados. (padrão: string vazia) | STRING | Sim | - |
| `criatividade` | Controla a probabilidade de criar detalhes adicionais que não são fortemente condicionados pela imagem inicial. (padrão: 0.3) | FLOAT | Sim | 0.1-0.5 |
| `estilo_predefinido` | Estilo desejado opcional da imagem gerada. (padrão: "None") | STRING | Sim | `"3d-model"`<br>`"analog-film"`<br>`"anime"`<br>`"cinematic"`<br>`"comic-book"`<br>`"digital-art"`<br>`"enhance"`<br>`"fantasy-art"`<br>`"isometric"`<br>`"line-art"`<br>`"low-poly"`<br>`"modeling-compound"`<br>`"neon-punk"`<br>`"origami"`<br>`"photographic"`<br>`"pixel-art"`<br>`"tile-texture"` |
| `semente` | A semente aleatória usada para criar o ruído. (padrão: 0) | INT | Sim | 0-4294967294 |
| `prompt_negativo` | Palavras-chave do que você NÃO deseja ver na imagem de saída. Este é um recurso avançado. (padrão: string vazia) | STRING | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `imagem` | A imagem ampliada na resolução 4K | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleCreativeNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `46f7bdd3cb4254b6305407f43e4a9a69a54fd3a0ac285d784c899dbf52edd552`
