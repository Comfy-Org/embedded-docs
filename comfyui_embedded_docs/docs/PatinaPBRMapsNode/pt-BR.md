# Patina PBR Material Maps

Deriva um conjunto de mapas de material PBR a partir de uma imagem de textura existente: basecolor, normal, roughness, metalness e height. Habilite apenas os mapas necessários, pois cada mapa habilitado aumenta o custo. Use-o para completar uma textura que ainda não tenha mapas de material ou para reconstruir um único mapa danificado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A fotografia ou renderização a partir da qual derivar os mapas PBR. | IMAGE | Sim | - |
| `basecolor` | Gere o mapa de cor base (albedo). Padrão: True. | BOOLEAN | Sim | true<br>false |
| `normal` | Gere o mapa normal. Padrão: True. | BOOLEAN | Sim | true<br>false |
| `roughness` | Gere o mapa de rugosidade. Padrão: False. | BOOLEAN | Sim | true<br>false |
| `metalness` | Gere o mapa de metalicidade. Padrão: False. | BOOLEAN | Sim | true<br>false |
| `height` | Gere o mapa de altura (deslocamento). Padrão: False. | BOOLEAN | Sim | true<br>false |
| `seed` | Semente para redução de ruído reproduzível. Padrão: 42. | INT | Sim | 0 a 2147483646 |
| `safety_checker` | Execute a verificação de segurança de conteúdo do provedor na solicitação. Configuração avançada. Padrão: False. | BOOLEAN | Sim | true<br>false |
| `auto_downscale` | Reduz automaticamente a escala de uma imagem de entrada cujo lado mais longo exceda 2048 pixels, o limite de entrada do modelo, preservando a proporção; imagens menores permanecem como estão. Desative para gerar um erro em imagens com tamanho excessivo. Configuração avançada. Padrão: True. | BOOLEAN | Não | true<br>false |

**Restrições e comportamento:**

* Pelo menos um mapa deve estar habilitado, caso contrário a execução falha.
* A imagem de entrada é limitada a 2048 pixels em seu lado mais longo; permita que `auto_downscale` a reduza ou a execução falhará em uma imagem com tamanho excessivo.
* Cada mapa desabilitado ainda retorna uma saída, mas como uma imagem de espaço reservado 1x1, então conecte apenas as saídas que você realmente gerou.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `basecolor` | O mapa de cor base (albedo) gerado, ou um espaço reservado 1x1 quando esse mapa está desabilitado. | IMAGE |
| `normal` | O mapa normal gerado, ou um espaço reservado 1x1 quando esse mapa está desabilitado. | IMAGE |
| `roughness` | O mapa de rugosidade gerado, ou um espaço reservado 1x1 quando esse mapa está desabilitado. | IMAGE |
| `metalness` | O mapa de metalicidade gerado, ou um espaço reservado 1x1 quando esse mapa está desabilitado. | IMAGE |
| `height` | O mapa de altura (deslocamento) gerado, ou um espaço reservado 1x1 quando esse mapa está desabilitado. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatinaPBRMapsNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `813c5bb3336c5ca54a9ca9ee95e84e7f27791170650248d0169acee39c4b3ce1`
