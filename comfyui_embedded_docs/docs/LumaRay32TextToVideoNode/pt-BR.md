# LumaRay32TextToVideoNode

Este nó gera um vídeo a partir de um prompt de texto usando o modelo Ray 3.2 da Luma. Ele envia seu prompt e configurações de vídeo para a API da Luma e retorna o vídeo gerado junto com um ID de geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para a geração do vídeo. | STRING | Sim | 1-6000 caracteres |
| `proporção` | A proporção de aspecto do vídeo gerado. | STRING | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"` |
| `resolução` | A resolução de saída do vídeo (padrão: "720p"). | STRING | Sim | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `duração` | A duração do vídeo gerado. | STRING | Sim | `"5s"`<br>`"10s"` |
| `loop` | Faz o vídeo repetir-se continuamente. Disponível apenas com duração de 5s. | BOOLEAN | Não | Verdadeiro/Falso (padrão: Falso) |
| `seed` | Semente para geração reproduzível. | INT | Não | 0 a 2147483647 |

**Observação:** O parâmetro `loop` só pode ser ativado quando `duration` estiver definido como "5s". Se você selecionar a duração "10s" e ativar o loop, o nó retornará um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `VIDEO` | O arquivo de vídeo gerado. | VIDEO |
| `generation_id` | O identificador único para a solicitação de geração de vídeo. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32TextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `04358a872530e5a2622bf0f148a694f2c707ce8535586d8f860bdf9911e1fa6a`
