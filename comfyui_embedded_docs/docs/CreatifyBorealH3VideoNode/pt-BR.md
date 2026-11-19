# Creatify Boreal-H3 Video

Creatify Boreal-H3 Video transforma um prompt de texto em um vídeo com som, usando o modelo H3 pós-treinado da Creatify, criado para anúncios em vídeo. Conecte um primeiro quadro para animar uma imagem estática e, opcionalmente, um último quadro para finalizar a cena em uma imagem escolhida.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto que descreve o vídeo. Deve conter pelo menos um caractere que não seja espaço em branco. | STRING | Sim | Qualquer texto não vazio |
| `first_frame` | Imagem a partir da qual o vídeo começa. Quando ela está conectada, mantenha `aspect_ratio` em `"auto"` para que o vídeo siga a imagem. | IMAGE | Não | - |
| `last_frame` | Imagem na qual o vídeo termina. Requer um `first_frame` conectado. | IMAGE | Não | - |
| `resolution` | Resolução do vídeo de saída (padrão: `"768p"`). | COMBO | Sim | `"768p"`<br>`"1088p"`<br>`"2k"` |
| `aspect_ratio` | Proporção de aspecto do vídeo de saída. `"auto"` segue o primeiro quadro quando um está conectado; nesse caso, deixe-o em `"auto"` (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Duração do vídeo em segundos (padrão: 5). Em `"2k"`, o máximo é 14 segundos. | INT | Sim | 1 a 15 (passo 1) |
| `prompt_enhancement` | Como a Creatify reescreve o prompt antes da renderização: `"auto"` e `"ads"` o transformam em um prompt de anúncio em vídeo e podem adicionar falas; `"general"` o reescreve para qualquer outro vídeo; `"none"` o renderiza como escrito (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"ads"`<br>`"general"`<br>`"none"` |
| `seed` | A seed controla se o nó é executado novamente. A Creatify escolhe sua própria aleatoriedade, então as mesmas entradas geram o mesmo vídeo apenas com `prompt_enhancement` definido como `"none"` (padrão: 42). | INT | Sim | 0 a 2147483647 |

**Restrições:** com um `first_frame`, a proporção de aspecto sempre vem da imagem, portanto qualquer outro valor de `aspect_ratio` gera um erro. Um `last_frame` sem um `first_frame` é rejeitado, e uma `duration` acima de 14 segundos é rejeitada em `"2k"`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `VIDEO` | O vídeo gerado com som. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreatifyBorealH3VideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `535bcbeced69cffd4d0edca04f30dd00dac4ec728cd8eb638b4f9d9af8448336`
