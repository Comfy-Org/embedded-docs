# Creatify Aurora 2.0 Avatar

Creatify Aurora 2.0 Avatar transforma uma foto mais um clipe de fala ou música em um vídeo com fala ou canto. O vídeo tem a mesma duração do áudio conectado e mantém esse áudio inalterado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagem` | Foto da pessoa a ser animada. Pelo menos 256 pixels em cada lado e uma proporção de aspecto entre 1:4 e 4:1; o vídeo mantém a proporção de aspecto da foto. | IMAGE | Sim | - |
| `áudio` | Fala ou música que movimenta a boca e determina a duração do vídeo. Até 60 segundos, ou 14 segundos em `"2k"`; cobrado por segundo iniciado. | AUDIO | Sim | Até 60 segundos |
| `resolução` | Resolução do vídeo de saída (padrão: `"720p"`). | COMBO | Sim | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"2k"` |
| `text_prompt` | Cena, câmera, iluminação, expressão ou movimento para a tomada. Vazio mantém a foto como está (padrão: string vazia). | STRING | Sim | Qualquer texto |
| `semente` | A seed controla se o nó é executado novamente. Os resultados são não determinísticos independentemente da seed (padrão: 42). | INT | Sim | 0 a 2147483647 |

**Restrições:** uma foto menor que 256 pixels em um dos lados, ou com proporção de aspecto fora de 1:4 a 4:1, gera um erro. Áudio mais longo que o limite para a resolução escolhida é rejeitado: 60 segundos normalmente e 14 segundos em `"2k"`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `VIDEO` | O vídeo com fala ou canto, com o áudio conectado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreatifyAurora2AvatarNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `29c83246ebed4bc7a9f3daf3612cd6f34bf2d5a2f1fde7612614a2da6a5010be`
