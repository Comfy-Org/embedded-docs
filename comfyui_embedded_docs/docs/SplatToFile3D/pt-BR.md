# Criar Arquivo 3D (de Splat)

O nó SplatToFile3D converte um splat gaussiano em um objeto File3D que pode ser usado com os nós Save ou Preview 3D. Ele suporta apenas um item por lote e permite que você escolha entre diferentes formatos de arquivo de saída para os dados 3D exportados.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `splat` | Os dados do splat gaussiano a serem serializados em um arquivo | SPLAT | Sim | - |
| `formato` | O formato de arquivo de saída para o arquivo 3D. ply: Splat Gaussiano 3D padrão com harmônicos esféricos completos. ksplat: mkkellogg SplatBuffer (nível 0, não compactado), somente cor base. spz: compactado com gzip da Niantic (~10x menor), somente cor base (padrão: "ply") | COMBO | Sim | "ply"<br>"ksplat"<br>"spz" |

Nota: Este nó suporta apenas um item por lote. Se o splat de entrada contiver mais de um item no lote, o nó registra um aviso e usa o primeiro item. Se um formato não suportado for fornecido, o nó gera um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `modelo_3d` | Um objeto File3D contendo os dados do splat gaussiano serializados no formato selecionado, pronto para salvar ou visualizar | FILE3D |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToFile3D/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4bb49f417a66f25fce577894a67f39bae6157c4eb88ccf8fad77d74141a50409`
