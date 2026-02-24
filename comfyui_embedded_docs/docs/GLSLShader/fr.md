> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLSLShader/fr.md)

Le nœud GLSL Shader applique un code de nuanceur de fragments GLSL ES personnalisé aux images d'entrée. Il vous permet d'écrire des programmes de nuanceurs qui peuvent traiter plusieurs images et accepter des paramètres uniformes (nombres à virgule flottante et entiers) pour créer des effets visuels complexes. La taille de sortie peut être déterminée par la première image d'entrée ou définie manuellement.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `fragment_shader` | STRING | Oui | N/A | Code source du nuanceur de fragments GLSL (compatible GLSL ES 3.00 / WebGL 2.0). Par défaut : un nuanceur de base qui sort la première image d'entrée. |
| `size_mode` | COMBO | Oui | `"from_input"`<br>`"custom"` | Taille de sortie : 'from_input' utilise les dimensions de la première image d'entrée, 'custom' permet une taille manuelle. |
| `width` | INT | Non | 1 à 16384 | La largeur de l'image de sortie lorsque `size_mode` est défini sur `"custom"`. Par défaut : 512. |
| `height` | INT | Non | 1 à 16384 | La hauteur de l'image de sortie lorsque `size_mode` est défini sur `"custom"`. Par défaut : 512. |
| `images` | IMAGE | Oui | 1 à 8 images | Images d'entrée à traiter par le nuanceur. Les images sont disponibles sous les noms `u_image0` à `u_image7` (sampler2D) dans le code du nuanceur. |
| `floats` | FLOAT | Non | 0 à 8 floats | Valeurs uniformes à virgule flottante pour le nuanceur. Les floats sont disponibles sous les noms `u_float0` à `u_float7` dans le code du nuanceur. Par défaut : 0.0. |
| `ints` | INT | Non | 0 à 8 entiers | Valeurs uniformes entières pour le nuanceur. Les entiers sont disponibles sous les noms `u_int0` à `u_int7` dans le code du nuanceur. Par défaut : 0. |

**Notes :**

* Les paramètres `width` et `height` ne sont requis et visibles que lorsque `size_mode` est défini sur `"custom"`.
* Au moins une image d'entrée est requise.
* Le code du nuanceur a toujours accès à une variable uniforme `u_resolution` (vec2) contenant les dimensions de sortie.
* Un maximum de 8 images d'entrée, 8 uniformes float et 8 uniformes integer peut être fourni.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `IMAGE0` | IMAGE | La première image de sortie du nuanceur. Disponible via `layout(location = 0) out vec4 fragColor0` dans le code du nuanceur. |
| `IMAGE1` | IMAGE | La deuxième image de sortie du nuanceur. Disponible via `layout(location = 1) out vec4 fragColor1` dans le code du nuanceur. |
| `IMAGE2` | IMAGE | La troisième image de sortie du nuanceur. Disponible via `layout(location = 2) out vec4 fragColor2` dans le code du nuanceur. |
| `IMAGE3` | IMAGE | La quatrième image de sortie du nuanceur. Disponible via `layout(location = 3) out vec4 fragColor3` dans le code du nuanceur. |
