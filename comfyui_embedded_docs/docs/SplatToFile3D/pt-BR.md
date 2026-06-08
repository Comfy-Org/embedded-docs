# Documentação do Nó SplatToFile3D

## Visão Geral

O nó SplatToFile3D converte um splat gaussiano em um objeto File3D que pode ser usado com nós Salvar ou Visualizar 3D. Ele suporta apenas um item por lote e permite escolher entre diferentes formatos de arquivo de saída para os dados 3D exportados.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `splat` | Os dados do splat gaussiano a serem serializados em um arquivo | SPLAT | Sim | - |
| `formato` | O formato do arquivo de saída para o arquivo 3D. ply: Splat Gaussiano 3D padrão com harmônicos esféricos completos. ksplat: SplatBuffer mkkellogg (nível 0, descompactado), apenas cor base. spz: Niantic compactado com gzip (~10x menor), apenas cor base (padrão: "ply") | COMBO | Sim | `"ply"`<br>`"ksplat"`<br>`"spz"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `model_3d` | Um objeto File3D contendo os dados do splat gaussiano serializados no formato selecionado, pronto para salvar ou visualizar | FILE3D |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToFile3D/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c04fe04faa8ce81ad699e67c00d047550b0cadbfd037b687331f76944501a9f6`
