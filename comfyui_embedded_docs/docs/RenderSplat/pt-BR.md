# Render Splat

Renderiza um gaussian splat como imagem usando um rasterizador EWA anisotrópico com splats elípticos orientados, antialiasing e renderização ordenada por profundidade de frente para trás. A câmera vem de uma entrada camera_info, ou você pode deixá-la vazia para enquadrar automaticamente o splat. Defina frames maior que 1 para um lote de imagens em mesa giratória para alimentar um nó de Vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `splat` | Os dados do gaussian splat a serem renderizados | SPLAT | Sim | - |
| `largura` | Largura da imagem de saída (padrão: 1024) | INT | Sim | 64 a 2048 (passo: 8) |
| `altura` | Altura da imagem de saída (padrão: 1024) | INT | Sim | 64 a 2048 (passo: 8) |
| `frames` | Número de quadros a renderizar. -1, 0 ou 1 produz uma única imagem estática. Valores maiores que 1 criam uma animação em mesa giratória onde a câmera orbita em uma volta completa de 360 graus. Valores negativos orbitam na direção oposta (padrão: 1) | INT | Sim | -240 a 240 |
| `escala_splat` | Multiplicador da projeção de cada splat. Valores menores produzem pontos mais nítidos, valores maiores produzem superfícies mais suaves e cheias (padrão: 1,0) | FLOAT | Sim | 0,1 a 5,0 (passo: 0,05) |
| `nitidez` | Controla a nitidez de splats sobrepostos. Um valor de 1,0 fornece mesclagem fisicamente correta. Valores acima de 1,0 tendem cada pixel para seu splat dominante (mais próximo) para textura mais nítida sem encolher splats ou abrir lacunas (padrão: 2,0) | FLOAT | Sim | 1,0 a 8,0 (passo: 0,5) |
| `sombreamento_headlight` | Sombreamento difuso de uma luz na posição da câmera, usando as normais dos surfels do splat. Escurece superfícies que se afastam da visão para revelar forma e curvatura. 0 dá albedo plano, 1 dá sombreamento mais forte (padrão: 0,0) | FLOAT | Sim | 0,0 a 3,0 (passo: 0,05) |
| `limite_opacidade` | Elimina gaussianos com opacidade abaixo deste limite, removendo elementos flutuantes fracos (padrão: 0,0) | FLOAT | Sim | 0,0 a 1,0 (passo: 0,01) |
| `estilo_render` | O que a saída de imagem mostra. Opções: color (renderização colorida completa), clay (sombreamento com albedo neutro), depth (objetos próximos aparecem claros), normal (mapa de normais OpenGL) (padrão: "color") | COMBO | Sim | "color"<br>"clay"<br>"depth"<br>"normal" |
| `fundo` | Cor de fundo sólida para a renderização (padrão: #000000) | COLOR | Sim | - |
| `imagem_fundo` | Plano de fundo opcional composto atrás do splat. Substitui a cor de fundo sólida. Redimensionado para o tamanho da renderização. Um lote de imagens é usado por quadro, uma única imagem é usada para todos os quadros. Funciona apenas com estilos de renderização color e clay | IMAGE | Não | - |
| `camera_info` | Câmera para renderizar. Pode vir de um nó Load3D, Preview3D ou Create Camera Info. Se vazio, o splat é enquadrado automaticamente a partir de uma visão 3/4 padrão | CAMERA_3D | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `image` | A imagem renderizada do gaussian splat | IMAGE |
| `mask` | A máscara alfa do splat renderizado | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderSplat/pt-BR.md)

---
**Source fingerprint (SHA-256):** `038bd9fb032f347ecda665c03719a64b0cf907599b701606f5cf6d0606d19d98`
