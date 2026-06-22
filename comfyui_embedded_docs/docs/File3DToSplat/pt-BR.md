# Obter Splat

Este nó converte um arquivo 3D contendo dados de gaussian splat em um formato de gaussian splat que pode ser utilizado no grafo de nós. Ele suporta os formatos de arquivo PLY, SPLAT, KSPLAT e SPZ, sendo que o formato do arquivo é detectado automaticamente a partir do conteúdo do arquivo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `modelo_3d` | Um arquivo 3D de gaussian splat | FILE3D | Sim | - |

O arquivo de entrada deve estar em um dos formatos suportados: PLY, SPLAT, KSPLAT ou SPZ. Arquivos PLY contêm dados completos de harmônicos esféricos, enquanto os outros formatos contêm apenas informações de cor base. O formato é detectado automaticamente a partir do conteúdo do arquivo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `splat` | Um gaussian splat contendo dados de posição, escala, rotação, opacidade e harmônicos esféricos | SPLAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/File3DToSplat/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9f45210a1366e57a91de6e1251f0e2e09f39e6498dbec1db7bf9826ebedd167b`
