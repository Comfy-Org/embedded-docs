# Génération d'image Kling

Le nœud de génération d'images Kling crée des images à partir de descriptions textuelles, avec la possibilité d'utiliser une image de référence comme guide. Il génère une ou plusieurs images selon votre description textuelle et vos paramètres de référence, puis renvoie les images générées en sortie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt textuel positif | STRING | Oui | - |
| `negative_prompt` | Prompt textuel négatif | STRING | Oui | - |
| `image_type` | Sélection du type de référence d'image (avancé). Requis lorsqu'une image de référence est fournie. | COMBO | Oui | `"subject_reference"`<br>`"style_reference"` |
| `image_fidelity` | Intensité de la référence pour les images téléchargées par l'utilisateur (par défaut : 0.5, avancé) | FLOAT | Oui | 0.0 - 1.0 |
| `human_fidelity` | Similarité de la référence au sujet (par défaut : 0.45, avancé) | FLOAT | Oui | 0.0 - 1.0 |
| `model_name` | Sélection du modèle pour la génération d'images (par défaut : "kling-v3") | COMBO | Oui | `"kling-v3"`<br>`"kling-v2"`<br>`"kling-v1-5"` |
| `aspect_ratio` | Format d'image pour les images générées (par défaut : "16:9") | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` |
| `n` | Nombre d'images générées (par défaut : 1) | INT | Oui | 1 - 9 |
| `image` | Image de référence facultative | IMAGE | Non | - |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine (par défaut : 0) | INT | Non | 0 - 2147483647 |

**Contraintes des paramètres :**

- Le paramètre `image` est facultatif. Lorsqu'une image de référence est fournie, le paramètre `image_type` doit être défini sur `"subject_reference"` ou `"style_reference"`.
- Lorsqu'aucune image de référence n'est fournie, les paramètres `image_type`, `image_fidelity` et `human_fidelity` ne sont pas utilisés.
- Le prompt et le prompt négatif ont une longueur maximale de `MAX_PROMPT_LENGTH_IMAGE_GEN` caractères.
- Le paramètre `seed` est facultatif et ne garantit pas des résultats déterministes.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Image(s) générée(s) en fonction des paramètres d'entrée | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/fr.md)

---
**Source fingerprint (SHA-256):** `f25164f4007b1f62285e76519238b5061b63597e1a06365acf93d4289063bd3a`
