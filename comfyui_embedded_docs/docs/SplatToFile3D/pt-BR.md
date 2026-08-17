# Criar Arquivo 3D (de Splat)

O SplatToFile3D converte um splat gaussiano em um objeto File3D que pode ser usado com os nós Save ou Preview 3D. Você pode escolher o formato do arquivo de saída. O nó suporta apenas um item por lote; se receber mais de um item, ele usa o primeiro e registra um aviso.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|--------------|-------------|-----------|
| `splat` | Os dados do splat gaussiano a serem serializados em um arquivo. Apenas um item por lote é suportado. Se mais de um item for fornecido, somente o primeiro será usado. | SPLAT | Sim | - |
| `format` | O formato do arquivo de saída para o arquivo 3D. ply: splat gaussiano 3D padrão com harmônicos esféricos completos. ksplat: SplatBuffer mkkellogg (nível 0, descompactado), somente cor base. spz: compactado com gzip da Niantic (~10x menor), somente cor base (padrão: "ply") | COMBO | Sim | `"ply"`<br>`"ksplat"`<br>`"spz"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-------------|--------------|
| `model_3d` | Um objeto File3D contendo os dados do splat gaussiano serializados no formato selecionado, pronto para salvar ou visualizar | FILE3D |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToFile3D/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4bb49f417a66f25fce577894a67f39bae6157c4eb88ccf8fad77d74141a50409`
