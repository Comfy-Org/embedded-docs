# Bria Remover Fundo de Vídeo (Transparente)

Este nó remove o fundo de um vídeo usando o serviço de IA da Bria e retorna os quadros recortados juntamente com uma máscara alfa. Conecte ambas as saídas a um nó de composição ou alimente-as com um nó Save WEBM para escrever um vídeo transparente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|---------------|-------------|-------|
| `video` | O vídeo de entrada para processar. A duração máxima é de 60 segundos. | VIDEO | Sim | - |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente (padrão: 0) | INT | Sim | 0 a 2147483647 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `images` | Os quadros do vídeo com o fundo removido | IMAGE |
| `mask` | A máscara alfa para os quadros do vídeo, onde 1 significa transparente | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaTransparentVideoBackground/pt-BR.md)

---
**Source fingerprint (SHA-256):** `536bd52af29218d2a342086e92799d3d9310da5ae5cbf02d705ba7503a4d73c8`
