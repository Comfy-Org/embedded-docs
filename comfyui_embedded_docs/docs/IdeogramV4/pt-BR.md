# Ideogram V4

Gera imagens usando o modelo Ideogram 4.0 a partir de um prompt de texto. Este nó envia sua descrição textual para a API do Ideogram e retorna a imagem gerada como um tensor de saída.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `prompt` | Prompt de texto para a geração da imagem. | STRING | Sim | Sem restrições |
| `resolução` | A resolução da imagem gerada. Padrão: "Auto" que permite ao modelo escolher a melhor resolução. | COMBO | Sim | `"Auto"`<br>`"2048x2048 (1:1)"`<br>`"1440x2880 (1:2)"`<br>`"2880x1440 (2:1)"`<br>`"1664x2496 (2:3)"`<br>`"2496x1664 (3:2)"`<br>`"1792x2240 (4:5)"`<br>`"2240x1792 (5:4)"`<br>`"1440x2560 (9:16)"`<br>`"2560x1440 (16:9)"`<br>`"1600x2560 (5:8)"`<br>`"2560x1600 (8:5)"`<br>`"1728x2304 (3:4)"`<br>`"2304x1728 (4:3)"`<br>`"1296x3168 (9:22)"`<br>`"3168x1296 (22:9)"`<br>`"1152x2944 (9:23)"`<br>`"2944x1152 (23:9)"`<br>`"1248x3328 (3:8)"`<br>`"3328x1248 (8:3)"`<br>`"1280x3072 (5:12)"`<br>`"3072x1280 (12:5)"` |
| `velocidade_de_renderização` | Controla a relação entre velocidade de geração e qualidade. Padrão: "DEFAULT". | COMBO | Sim | `"DEFAULT"`<br>`"TURBO"`<br>`"QUALITY"` |
| `semente` | Semente para geração reproduzível. Padrão: 0. | INT | Sim | Mín: 0<br>Máx: 2147483647 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `IMAGE` | A imagem gerada como um tensor. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV4/pt-BR.md)

---
**Source fingerprint (SHA-256):** `47a486824211d34b9109c5038b0b094d192c4e243c0a6c4ceab13af3bdabe6e4`
