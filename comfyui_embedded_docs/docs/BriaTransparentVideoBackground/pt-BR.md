# Bria Remover Fundo de Vídeo (Transparente)

Este nó remove o fundo de um vídeo usando o serviço de IA da Bria e gera os quadros recortados juntamente com uma máscara alfa. Conecte ambas as saídas a um nó de composição ou alimente-as com um nó Save WEBM para gravar um vídeo transparente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `vídeo` | O vídeo de entrada a ser processado. O vídeo deve ter 60 segundos ou menos. | VIDEO | Sim | - |
| `semente` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente (padrão: 0) | INT | Sim | 0 a 2147483647 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `imagens` | Os quadros do vídeo com o fundo removido, como imagens RGB no intervalo de 0.0 a 1.0 | IMAGE |
| `máscara` | A máscara alfa para os quadros do vídeo, seguindo a convenção do Load Image, em que 1 significa transparente | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaTransparentVideoBackground/pt-BR.md)

---
**Source fingerprint (SHA-256):** `536bd52af29218d2a342086e92799d3d9310da5ae5cbf02d705ba7503a4d73c8`
