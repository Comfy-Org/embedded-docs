# Bria Remove Video Background (Transparent)

Este nó remove o fundo de um vídeo usando o serviço de IA da Bria e gera os quadros recortados junto com uma máscara alfa. Conecte ambas as saídas a um nó de composição ou alimente-as em um nó Save WEBM para escrever um vídeo transparente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-----------|---------------|-------------|-------|
| `vídeo` | O vídeo de entrada a ser processado | VIDEO | Sim | - |
| `semente` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente (padrão: 0) | INT | Sim | 0 a 2147483647 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `images` | Os quadros do vídeo com o fundo removido | IMAGE |
| `mask` | A máscara alfa para os quadros do vídeo | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaTransparentVideoBackground/pt-BR.md)

---
**Source fingerprint (SHA-256):** `45fb3fc185b5c6420d6ac2b87f2403566e1ef6dcdc57791fb833b6ccb2a64cd9`
