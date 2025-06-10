`Codificar Texto CLIP (Prompt)` actúa como un traductor, convirtiendo tus descripciones textuales creativas en un "lenguaje" especial que la IA puede entender, ayudando así a la IA a interpretar con precisión qué tipo de imagen deseas crear.

## Principio de Funcionamiento

Imagina que estás comunicándote con un artista extranjero - necesitas un traductor para transmitir con precisión la obra que deseas. Este nodo actúa como ese traductor, utilizando el modelo CLIP (un modelo de IA entrenado con grandes cantidades de pares de imagen y texto) para entender tus descripciones textuales y convertirlas en "instrucciones" que el modelo de arte de IA puede comprender.

## Entradas

| Parámetro | Tipo de Dato | Método de Entrada | Valor Predeterminado | Rango | Descripción |
|-----------|--------------|-------------------|---------------------|--------|-------------|
| text | STRING | Entrada de texto | Vacío | Cualquier texto | Como instrucciones detalladas a un artista, ingresa aquí tu descripción de imagen. Admite texto multilínea para descripciones detalladas. |
| clip | CLIP | Selección de modelo | Ninguno | Modelos CLIP cargados | Como elegir un traductor específico, diferentes modelos CLIP son como diferentes traductores con comprensiones ligeramente diferentes de los estilos artísticos. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| ACONDICIONAMIENTO | CONDITIONING | Estas son las "instrucciones de pintura" traducidas que contienen directrices creativas detalladas que el modelo de IA puede entender. Estas instrucciones le indican al modelo de IA cómo crear una imagen que coincida con tu descripción. |

## Consejos de Uso

1. **Uso Básico de Prompts de Texto**
   - Escribe descripciones detalladas como si estuvieras redactando un breve ensayo
   - Las descripciones más específicas conducen a resultados más precisos
   - Usa comas en inglés para separar diferentes elementos descriptivos

2. **Función Especial: Uso de Modelos de Embedding**
   - Los modelos de embedding son como paquetes de estilos artísticos preestablecidos que pueden aplicar rápidamente efectos artísticos específicos
   - Actualmente soporta los formatos de archivo .safetensors, .pt y .bin, y no necesariamente necesitas usar el nombre completo del modelo
   - Cómo usar:
     1. Coloca el archivo del modelo de embedding (en formato .pt) en la carpeta `ComfyUI/models/embeddings`
     2. Usa `embedding:nombre_del_modelo` en tu texto
     Ejemplo: Si tienes un modelo llamado `EasyNegative.pt`, puedes usarlo así:

     ```
     a beautiful landscape, embedding:EasyNegative, high quality
     ```

3. **Ajuste de Pesos de Prompts**
   - Usa paréntesis para ajustar la importancia de ciertas descripciones
   - Por ejemplo: `(beautiful:1.2)` hará que la característica "beautiful" sea más prominente
   - Los paréntesis simples `()` tienen un peso predeterminado de 1.1
   - Usa los atajos de teclado `ctrl + flechas arriba/abajo` para ajustar rápidamente los pesos
   - El tamaño del paso de ajuste de peso se puede modificar en la configuración

4. **Notas Importantes**
   - Asegúrate de que el modelo CLIP esté correctamente cargado
   - Usa descripciones textuales positivas y claras
   - Al usar modelos de embedding, asegúrate de que el nombre del archivo sea correcto y compatible con la arquitectura de tu modelo principal actual
