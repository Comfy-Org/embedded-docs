> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLSLShader/fr.md)

Le nœud Shader GLSL applique un code de fragment shader GLSL ES personnalisé aux images d’entrée. Il permet d’écrire des programmes shader capables de traiter plusieurs images et d’accepter des paramètres uniformes (flottants, entiers, booléens et courbes) pour créer des effets visuels complexes. La taille de sortie peut être déterminée par la première image d’entrée ou définie manuellement.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `fragment_shader` | STRING | Oui | N/D | Code source du fragment shader GLSL (compatible GLSL ES 3.00 / WebGL 2.0). Par défaut : un shader basique qui produit la première image d’entrée. |
| `size_mode` | COMBO | Oui | `"from_input"`<br>`"custom"` | Taille de sortie : 'from_input' utilise les dimensions de la première image d’entrée, 'custom' permet une taille manuelle. |
| `width` | INT | Non | 1 à 16384 | Largeur de l’image de sortie lorsque `size_mode` est défini sur `"custom"`. Par défaut : 512. |
| `height` | INT | Non | 1 à 16384 | Hauteur de l’image de sortie lorsque `size_mode` est défini sur `"custom"`. Par défaut : 512. |
| `images` | IMAGE | Oui | 1 à 8 images | Images d’entrée à traiter par le shader. Les images sont accessibles sous les noms `u_image0` à `u_image7` (sampler2D) dans le code du shader. |
| `floats` | FLOAT | Non | 0 à 8 flottants | Valeurs uniformes flottantes pour le shader. Les flottants sont accessibles sous les noms `u_float0` à `u_float7` dans le code du shader. Par défaut : 0.0. |
| `ints` | INT | Non | 0 à 8 entiers | Valeurs uniformes entières pour le shader. Les entiers sont accessibles sous les noms `u_int0` à `u_int7` dans le code du shader. Par défaut : 0. |
| `booléens` | BOOLEAN | Non | 0 à 8 booléens | Valeurs uniformes booléennes pour le shader. Les booléens sont accessibles sous les noms `u_bool0` à `u_bool7` (bool) dans le code du shader. Par défaut : False. |
| `courbes` | CURVE | Non | 0 à 8 courbes | Valeurs uniformes de courbes pour le shader. Les courbes sont accessibles sous les noms `u_curve0` à `u_curve7` (sampler2D, LUT 1D) dans le code du shader. Échantillonnez avec `texture(u_curve0, vec2(x, 0.5)).r`. |

**Remarques :**

* Les paramètres `width` et `height` ne sont requis et visibles que lorsque `size_mode` est défini sur `"custom"`.
* Au moins une image d’entrée est requise.
* Le code du shader a toujours accès à un uniforme `u_resolution` (vec2) contenant les dimensions de sortie.
* Un maximum de 8 images d’entrée, 8 uniformes flottants, 8 uniformes entiers, 8 uniformes booléens et 8 uniformes de courbes peuvent être fournis.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `IMAGE1` | IMAGE | Première image de sortie du shader. Accessible via `layout(location = 0) out vec4 fragColor0` dans le code du shader. |
| `IMAGE2` | IMAGE | Deuxième image de sortie du shader. Accessible via `layout(location = 1) out vec4 fragColor1` dans le code du shader. |
| `IMAGE3` | IMAGE | Troisième image de sortie du shader. Accessible via `layout(location = 2) out vec4 fragColor2` dans le code du shader. |
| `IMAGE3` | IMAGE | Quatrième image de sortie du shader. Accessible via `layout(location = 3) out vec4 fragColor3` dans le code du shader. |

---
**Source fingerprint (SHA-256):** `7830977409a5efab205b7c927eb83499a9e1e8299959b34643c9c3f1f586c058`
