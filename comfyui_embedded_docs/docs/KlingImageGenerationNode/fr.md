# Génération d'image Kling

Kling Image Generation Node génère des images à partir de descriptions textuelles, avec la possibilité d'utiliser une image de référence comme guide. Il crée une ou plusieurs images selon votre description textuelle et vos paramètres de référence, puis renvoie les images générées en sortie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Description textuelle positive | STRING | Oui | 500 caractères maximum |
| `negative_prompt` | Description textuelle négative | STRING | Oui | 500 caractères maximum |
| `image_type` | Sélection du type de référence d'image (avancé). Utilisé lorsqu'une image de référence est fournie. | COMBO | Oui | `"subject_reference"`<br>`"style_reference"` |
| `image_fidelity` | Intensité de la référence pour les images téléchargées par l'utilisateur (défaut : 0,5, avancé) | FLOAT | Oui | 0,0 - 1,0 |
| `human_fidelity` | Similarité de la référence du sujet (défaut : 0,45, avancé) | FLOAT | Oui | 0,0 - 1,0 |
| `model_name` | Sélection du modèle pour la génération d'images (défaut : "kling-v3") | COMBO | Oui | `"kling-v3"`<br>`"kling-v2"` |
| `aspect_ratio` | Ratio d'aspect pour les images générées (défaut : "16:9") | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` |
| `n` | Nombre d'images générées (défaut : 1) | INT | Oui | 1 - 9 |
| `image` | Image de référence facultative | IMAGE | Non | - |
| `seed` | La graine (seed) détermine si le nœud doit s'exécuter à nouveau ; les résultats ne sont pas déterministes quelle que soit la graine (défaut : 0) | INT | Non | 0 - 2147483647 |

**Contraintes des paramètres :**

- Le paramètre `image` est facultatif. Lorsqu'une image de référence est fournie, `image_type` détermine si elle est utilisée comme référence de sujet ou comme référence de style. Lorsqu'aucune image de référence n'est fournie, `image_type` n'est pas appliqué.
- `prompt` doit contenir au moins 1 caractère et au plus 500 caractères. `negative_prompt` peut être vide, mais est limité à 500 caractères.
- Le paramètre `seed` est facultatif et ne garantit pas des résultats déterministes.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | Image(s) générée(s) à partir des paramètres d'entrée. Lorsque plusieurs images sont demandées, toutes les images sont renvoyées empilées dans un seul lot. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/fr.md)

---
**Source fingerprint (SHA-256):** `165d18244870b5b4f34587633a5492e733ad0b0a923bb8c3e506319460321906`
