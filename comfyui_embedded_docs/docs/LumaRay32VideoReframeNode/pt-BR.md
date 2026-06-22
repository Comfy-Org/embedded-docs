# LumaRay32VideoReframeNode

Este nó altera a proporção de aspecto de um vídeo existente usando o Luma Ray 3.2, que preenche as áreas recém-expostas da tela com conteúdo gerado. O vídeo de origem pode ter até 30 segundos de duração, e a cobrança é por segundo de saída.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `video` | Vídeo de origem para reenquadrar. Até 30 segundos. | VIDEO | Sim | - |
| `prompt` | Descreve como as áreas recém-expostas da tela devem ser preenchidas. | STRING | Sim | - |
| `aspect_ratio` | A proporção de aspecto desejada para o vídeo reenquadrado (padrão: "16:9"). | STRING | Sim | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4"<br>"21:9" |
| `resolution` | A resolução de saída do vídeo reenquadrado (padrão: "720p"). | STRING | Sim | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `seed` | Semente para geração reproduzível. | INT | Sim | - |

**Observação:** A resolução `1080p` não está disponível para proporções de aspecto verticais (`9:16` e `3:4`) ao reenquadrar.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `video` | O vídeo reenquadrado com a nova proporção de aspecto e áreas da tela preenchidas. | VIDEO |
| `generation_id` | O identificador único para a solicitação de geração. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32VideoReframeNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d35ff5b63a850e4e44a40857188918ab5cde00b9159e3720a189a81807cfa7cb`
