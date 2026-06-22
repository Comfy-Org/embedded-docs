# Luma Texto para Vídeo

Gera vídeos de forma síncrona com base em um prompt de texto e configurações de saída. Este nó cria conteúdo de vídeo usando descrições textuais e diversos parâmetros de geração, produzindo o vídeo final assim que o processo de geração é concluído.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt para a geração do vídeo (padrão: string vazia). Deve ter pelo menos 3 caracteres. | STRING | Sim | - |
| `model` | O modelo de geração de vídeo a ser utilizado. | COMBO | Sim | `"ray_1_6"`<br>`"ray_2"` |
| `proporção` | A proporção de aspecto para o vídeo gerado (padrão: "16:9"). | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` |
| `resolução` | A resolução de saída do vídeo (padrão: "540p"). Este parâmetro é ignorado ao usar o modelo `ray_1_6`. | COMBO | Sim | `"540p"`<br>`"720p"`<br>`"1080p"` |
| `duração` | A duração do vídeo gerado. Este parâmetro é ignorado ao usar o modelo `ray_1_6`. | COMBO | Sim | `"5s"`<br>`"9s"` |
| `loop` | Indica se o vídeo deve ser em loop (padrão: Falso). | BOOLEAN | Sim | - |
| `seed` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0). | INT | Sim | 0 a 18446744073709551615 |
| `luma_concepts` | Conceitos de Câmera opcionais para ditar o movimento da câmera através do nó Luma Concepts. | CUSTOM | Não | - |

**Observação:** Ao usar o modelo `ray_1_6`, os parâmetros `duration` e `resolution` são automaticamente ignorados e não afetam a geração.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `44482bc91c3df2cc9ac22d06197668af45849e8bfde8bd435905f11f2593342c`
