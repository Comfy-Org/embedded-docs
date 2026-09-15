# LTXV Adicionar Quadros-chave Gerados

O nó LTXV Add Generated Keyframes anexa keyframes de detalhamento a um latent de vídeo. Cada keyframe é um frame latente de tokens posicionado sobre um único frame de pixel; ele passa por denoising junto com o vídeo e não faz parte da saída decodificada. O posicionamento é de um slot a cada `interval_frames` pixels, pulando frames I2V, guias existentes e keyframes gerados já presentes no condicionamento; extraia-os de volta com LTXV Separate Generated Keyframes. É necessário um checkpoint treinado para keyframes gerados (um que contenha `keyframes_abs_pos_embedding`).

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `positive` | Condicionamento positivo ao qual os keyframes são anexados. | CONDITIONING | Sim | N/A |
| `negative` | Condicionamento negativo ao qual os keyframes são anexados. | CONDITIONING | Sim | N/A |
| `vae` | Usado apenas para ler os fatores de escala do latent. | VAE | Sim | N/A |
| `latent` | Latent de vídeo 5D simples para gerar keyframes junto. Adicione-os antes de Concat AV Latent. | LATENT | Sim | N/A |
| `interval_frames` | Passo de frames de pixel para posicionamento automático. O padrão 24 equivale a cerca de um keyframe por segundo a 24 fps. Pixels ocupados são pulados. Ignorado quando `frame_indices` está definido. (padrão: 24) | INT | Não | 1-1024 |
| `keyframes` | Conteúdo opcional para inicializar os novos keyframes. Conecte keyframes de um Separate anterior (mesmo tamanho espacial), ou um latent de vídeo simples para copiar o frame mais próximo em cada novo slot (ex.: após upscale temporal). Eles ainda passam por denoising, não são fixados como guias. Índices registrados em um latent de keyframes são ignorados, a menos que `frame_indices` esteja definido. Só tem efeito quando a amostragem começa abaixo de sigma 1. | LATENT | Não | N/A |
| `frame_indices` | Índices opcionais de frames de pixel. Deixe vazio para posicionar a partir de `interval_frames` no canvas atual. Quando definido, esta lista é o posicionamento (os keyframes conectados são correspondidos em ordem). O último frame é permitido; o frame 0 não (ele já é um token independente). (padrão: string vazia) | STRING | Não | Inteiros separados por vírgula; 1 até o último frame de pixel (frame 0 excluído) |

**Observação:** O `latent` deve ser um latent de vídeo 5D simples com keyframes gerados adicionados antes de Concat AV Latent. Quando `frame_indices` está definido, cada frame de pixel listado deve ser único e não pode já conter um keyframe de imagem, uma guia ou um keyframe gerado. Se `frame_indices` estiver vazio, pixels ocupados são pulados automaticamente; se não existir um slot de detalhamento livre, o nó lança um erro. Ao anexar a keyframes gerados existentes, o latent ainda deve ter os mesmos tokens por frame e o bloco existente deve terminar no último frame latente.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | Condicionamento positivo com atenção de keyframes gerados anexada. | CONDITIONING |
| `negative` | Condicionamento negativo com atenção de keyframes gerados anexada. | CONDITIONING |
| `latent` | Latent de vídeo com keyframes gerados anexados em T. | LATENT |

## Notas

- O parâmetro `interval_frames` define o espaçamento dos keyframes posicionados automaticamente. Um valor mais alto resulta em menos keyframes e espaçamento maior; um valor mais baixo produz mais keyframes.
- A entrada `keyframes` permite inicializar os novos keyframes com keyframes existentes ou um latent de vídeo. Se um latent de vídeo simples mais longo for fornecido, o frame de vídeo mais próximo é copiado em cada novo slot. Esses keyframes ainda passam por denoising e não são fixados como guias.
- O parâmetro `frame_indices` permite especificar índices exatos de frames de pixel onde os keyframes devem ser posicionados. Quando fornecido, `interval_frames` é ignorado. A lista deve conter inteiros únicos dentro do intervalo válido de pixels, e o frame 0 não é permitido.
- As saídas `positive` e `negative` contêm o condicionamento com atenção de keyframes gerados anexada.
- A saída `latent` contém o latent de vídeo com keyframes gerados anexados em T.
- É necessário um checkpoint treinado para keyframes gerados (um que contenha `keyframes_abs_pos_embedding`).
- Extraia os keyframes gerados de volta com LTXV Separate Generated Keyframes.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGeneratedKeyframes/pt-BR.md)

---
**Source fingerprint (SHA-256):** `43053d15eceb61f37223c46dd46417c71f0503ef3a412ee50a3b2f764f310a64`
