# FLUX 3 Max Text to Video

FLUX 3 Max Text to Video gera um vídeo com áudio sincronizado a partir de um prompt de texto. O prompt é interpretado e expandido pelo FLUX 3 Max antes da renderização, o nó aguarda a conclusão da renderização e o clipe finalizado é retornado.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | O que o clipe deve mostrar, em linguagem natural. Descreva som ambiente, música e fala separadamente para áudio em camadas (padrão: vazio). | STRING | Sim | Texto multilinha |
| `aspect_ratio` | Proporção de saída. `"auto"` é 16:9 para prompts de texto (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"21:9"`<br>`"2:1"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | Duração do clipe em segundos (padrão: `"5"`). | COMBO | Sim | `"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"`<br>`"11"`<br>`"12"`<br>`"13"`<br>`"14"`<br>`"15"`<br>`"16"`<br>`"17"`<br>`"18"`<br>`"19"`<br>`"20"` |
| `resolution` | Resolução de saída (padrão: `"720p"`). | COMBO | Sim | `"720p"`<br>`"1080p"` |
| `reasoning_level` | Quanto o modelo raciocina sobre o prompt e o expande antes de gerar. `"high"` leva mais tempo; o preço é o mesmo (padrão: `"high"`). | COMBO | Sim | `"low"`<br>`"high"` |
| `generate_audio` | Gera áudio sincronizado. Desativado produz um vídeo sem faixa de áudio (padrão: true). | BOOLEAN | Sim | `true`<br>`false` |
| `seed` | Semente que controla se o nó é executado novamente. Os resultados são não determinísticos independentemente desse valor (padrão: 42). | INT | Sim | 0 a 2147483646 |

Nota: `prompt` deve conter pelo menos um caractere. O preço exibido é baseado em `resolution` e `duration`: 720p é cobrado a US$ 0,060775 por segundo e 1080p a US$ 0,103675 por segundo até 7 de novembro de 2026, e a US$ 0,2431 e US$ 0,4147 por segundo após essa data. O custo total estimado do clipe é mostrado na interface do usuário.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `video` | O clipe de vídeo gerado, com áudio sincronizado quando `generate_audio` está habilitado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3MaxTextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6dcb11e7aa7f1592169ede449c4092740db43e635501205eba02a066f03a967f`
