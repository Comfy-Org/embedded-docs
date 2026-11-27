# Tripo: Multiview para Modelo

Este nó gera modelos 3D de forma síncrona usando a API do Tripo, processando até quatro imagens que mostram diferentes vistas de um objeto (frontal, esquerda, traseira, direita). Ele exige uma imagem frontal e pelo menos uma vista adicional (esquerda, traseira ou direita) para construir o modelo 3D. Textura, material PBR, qualidade da geometria e formato de saída podem ser controlados a partir do nó.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagem` | Imagem da vista frontal do objeto. | IMAGE | Sim | - |
| `imagem_esquerda` | Imagem da vista esquerda do objeto. | IMAGE | Não | - |
| `imagem_traseira` | Imagem da vista traseira do objeto. | IMAGE | Não | - |
| `imagem_direita` | Imagem da vista direita do objeto. | IMAGE | Não | - |
| `versão_do_modelo` | A versão do modelo a ser usada para a geração. | COMBO | Não | Várias opções disponíveis |
| `orientação` | Configuração de orientação para o modelo 3D (padrão: `"default"`). | COMBO | Não | Várias opções disponíveis |
| `textura` | Gerar mapas de textura. Desativado retorna geometria sem textura e ignora pbr. (padrão: True) | BOOLEAN | Não | - |
| `pbr` | Mapas de material PBR (cor base, metálico, rugosidade, normal). Requer textura. (padrão: True) | BOOLEAN | Não | - |
| `semente_do_modelo` | Semente aleatória para geração do modelo (padrão: 42). | INT | Não | 0 a 2,147,483,647 |
| `semente_da_textura` | Semente aleatória para geração de textura (padrão: 42). | INT | Não | 0 a 2,147,483,647 |
| `qualidade_da_textura` | Nível de qualidade para geração de textura (padrão: `"standard"`). `"detailed"` = texturas HD, `"extreme"` = texturas 8K Ultra. | COMBO | Não | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `alinhamento_da_textura` | Método usado para alinhar texturas ao modelo (padrão: `"original_image"`). | COMBO | Não | `"original_image"`<br>`"geometry"` |
| `limite_de_faces` | Contagem máxima de faces. -1 permite que o Tripo escolha adaptativamente (cerca de 1,4M de faces no v3.x standard, 2M no detailed). O Tripo limita silenciosamente: malhas quad em 150.000. (padrão: -1) | INT | Não | -1 a 2,000,000 |
| `quad` | Saída de malha quad. O Tripo entrega malhas quad como FBX, então o resultado chega na saída FBX e a saída GLB permanece vazia. (padrão: False) | BOOLEAN | Não | - |
| `qualidade_da_geometria` | Nível de qualidade para geração de geometria (padrão: `"standard"`). | COMBO | Não | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | Malha low-poly com topologia limpa e de estilo artesanal (500-20,000 faces, quad 500-10,000). Melhor para objetos simples; objetos complexos podem falhar. (padrão: False) | BOOLEAN | Não | - |
| `auto_size` | Dimensiona modelos texturizados para seu tamanho real em metros. O Tripo armazena o tamanho como a transformação de cena do modelo e o incorpora quando o modelo é convertido, rigado ou retargetado; ignorado sem textura. (padrão: False) | BOOLEAN | Não | - |

**Observação:** A imagem frontal (`image`) é sempre obrigatória, e pelo menos uma entre `image_left`, `image_back` ou `image_right` também deve ser fornecida. Desativar `texture` também desativa `pbr` automaticamente, já que `pbr` requer textura. Quando `smart_low_poly` está habilitado e `face_limit` não é deixado em -1, `face_limit` deve estar entre 500 e 20,000 para malhas triangulares ou entre 500 e 10,000 para malhas quad.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `arquivo_do_modelo` | Caminho de arquivo ou identificador para o modelo 3D gerado (apenas para compatibilidade com versões anteriores). | STRING |
| `task_id_do_modelo` | Identificador de tarefa para acompanhar o processo de geração do modelo. | MODEL_TASK_ID |
| `GLB` | O arquivo de modelo 3D gerado no formato GLB. Vazio quando `quad` está habilitado. | FILE3DGLB |
| `FBX` | O arquivo de modelo 3D gerado no formato FBX. Preenchido apenas quando `quad` está habilitado. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b66df4cad6167fa27edf1fe21b96cb47af90027b3fbe0a3c9c14101506281ed7`
