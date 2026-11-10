# Bake Texture From Views

Projette les images rendues sur la disposition UV du maillage. Rendez le maillage avec Render Mesh, modifiez ou régénérez les images, puis cuisez-les avec le même maillage et les mêmes caméras. Les texels qu'aucune vue ne couvre conservent la texture ou les couleurs de sommets propres au maillage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `mesh` | Le maillage déplié en UV qui a été rendu. | MESH | Oui | - |
| `images` | Une image par caméra, dans l'ordre des caméras (Batch Images). Toute résolution ayant le rapport d'aspect du rendu ; une résolution plus élevée donne une cuisson plus nette. | IMAGE | Oui | - |
| `camera_info` | Les caméras avec lesquelles les images ont été rendues, telles que connectées à Render Mesh. Joignez les rigs avec Batch Cameras. Aucun : vue de face auto-cadrée de Render Mesh. | LOAD3D_CAMERA | Non | - |
| `resolution` | Résolution de la texture carrée. 0 conserve la taille de texture actuelle du maillage, ou 2048 lorsqu'il n'en a pas ; sinon, la texture actuelle est rééchantillonnée à cette taille. Par défaut : 0. | INT | Non | 0 à 8192 (pas : 64) |
| `blend_exponent` | Les vues sont pondérées par cos(angle de vue)^exposant. Une valeur plus élevée favorise la vue la plus frontale (plus nette, coutures plus marquées) ; une valeur plus faible moyenne davantage de vues (plus douce). Par défaut : 4.0. | FLOAT | Non | 0.0 à 32.0 (pas : 0.5) |
| `fill_unseen` | Les texels qu'aucune vue ne voit prennent une couleur développée à partir de la surface vue au lieu de la texture ou des couleurs de sommets propres au maillage. Utilisez-le lorsque les vues remplacent toute la texture. Par défaut : false. | BOOLEAN | Non | true<br>false |
| `mask` | Zones modifiées par vue ; seuls les pixels masqués sont projetés. Un masque unique s'applique à chaque vue. | MASK | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `base_color` | La texture cuite, pour Apply Texture to Mesh. | IMAGE |
| `confidence` | Par texel, à quel point la meilleure vue l'a vu de face ; 0 signifie non vu. | MASK |

Remarque : Les rendus effectués avec une transformation de modèle de visionneuse ne s'alignent pas avec la cuisson, et seul le premier maillage d'un lot est utilisé.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeTextureFromViews/fr.md)

---
**Source fingerprint (SHA-256):** `e5f2456977693dc09e69ce4d846f2ab775f2520115623d9f63a76807d6c9f797`
