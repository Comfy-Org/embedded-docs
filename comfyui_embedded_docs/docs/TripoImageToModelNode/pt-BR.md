# Tripo: Imagem para Modelo

Gera modelos 3D de forma síncrona com base em uma única imagem usando a API da Tripo. Forneça uma imagem de entrada, e o nó cria um modelo 3D finalizado a partir dela, com controles opcionais para versão do modelo, geração de textura, nível de detalhe e formato de saída. Esta é a versão legada do nó de imagem para modelo, mantida para fluxos de trabalho mais antigos.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagem` | A imagem de entrada usada para gerar o modelo 3D. Uma imagem deve ser fornecida, caso contrário o nó lança um erro. | IMAGE | Sim | - |
| `versão_do_modelo` | A versão do modelo a ser usada para a geração. | COMBO | Não | `"v3.1-20260211"`<br>`"v3.0-20250812"` |
| `estilo` | Não é mais suportado pela Tripo e é ignorado. Mantido para fluxos de trabalho mais antigos. (padrão: `"None"`) | COMBO | Não | `"None"`<br>`"realistic"`<br>`"cartoon"`<br>`"sculpture"`<br>`"low_poly"` |
| `textura` | Gera mapas de textura. Desativado retorna geometria bruta e ignora `pbr`. (padrão: True) | BOOLEAN | Não | True<br>False |
| `pbr` | Mapas de material PBR (cor base, metálico, rugosidade, normal). Requer `texture`. (padrão: True) | BOOLEAN | Não | True<br>False |
| `semente_do_modelo` | Semente aleatória para geração do modelo. (padrão: 42) | INT | Não | 0 a 2147483647 |
| `orientação` | Configuração de orientação para o modelo gerado. (padrão: `"default"`) | COMBO | Não | `"default"`<br>`"front"`<br>`"back"`<br>`"left"`<br>`"right"`<br>`"top"`<br>`"bottom"` |
| `semente_da_textura` | Semente aleatória para geração de textura. (padrão: 42) | INT | Não | 0 a 2147483647 |
| `qualidade_da_textura` | Nível de qualidade para geração de textura: `detailed` = texturas HD, `extreme` = texturas Ultra 8K. (padrão: `"standard"`) | COMBO | Não | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `alinhamento_da_textura` | Método de alinhamento para mapeamento de textura. (padrão: `"original_image"`) | COMBO | Não | `"original_image"`<br>`"geometry"` |
| `limite_de_faces` | Número máximo de faces. -1 permite que a Tripo escolha de forma adaptativa (cerca de 1,4M de faces no padrão v3.x, 2M no detalhado). A Tripo limita silenciosamente: malhas quad em 150.000. (padrão: -1) | INT | Não | -1 a 2000000 |
| `quad` | Saída de malha quad. A Tripo entrega malhas quad como FBX, então o resultado chega na saída FBX e a saída GLB permanece vazia. (padrão: False) | BOOLEAN | Não | True<br>False |
| `qualidade_da_geometria` | Nível de qualidade para geração de geometria. (padrão: `"standard"`) | COMBO | Não | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | Malha low-poly com topologia limpa de estilo artesanal (500-20.000 faces, quad 500-10.000). Melhor para objetos simples; objetos complexos podem falhar. (padrão: False) | BOOLEAN | Não | True<br>False |
| `auto_size` | Dimensiona modelos texturizados para seu tamanho real em metros. A Tripo armazena o tamanho como a transformação de cena do modelo e o incorpora quando o modelo é convertido, rigado ou retargetizado; ignorado sem textura. (padrão: True) | BOOLEAN | Não | True<br>False |

Nota: O parâmetro `image` é obrigatório; se estiver ausente, o nó lança um RuntimeError. Quando `texture` é False, o modelo contém apenas geometria bruta e `pbr` é forçado para False. Quando `smart_low_poly` está ativado, `face_limit` deve estar entre 500 e 20.000 para malhas triangulares, ou entre 500 e 10.000 quando `quad` também está ativado; se o limite for inválido, o nó lança um ValueError. Definir `face_limit` como -1 (o padrão) não envia nenhum limite explícito de faces para a API, permitindo que a Tripo escolha adaptativamente.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `arquivo_do_modelo` | O arquivo de modelo 3D gerado (apenas para compatibilidade com versões anteriores). | STRING |
| `task_id_do_modelo` | O ID da tarefa para acompanhar o processo de geração do modelo. | MODEL_TASK_ID |
| `GLB` | O modelo 3D gerado no formato GLB. Vazio quando `quad` está ativado. | FILE3DGLB |
| `FBX` | O modelo 3D gerado no formato FBX. Preenchido apenas quando `quad` está ativado. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3b278abfd13329ee58ebab1bfeb47d32d09f4797f3d8628a35a028c3d15a7314`
