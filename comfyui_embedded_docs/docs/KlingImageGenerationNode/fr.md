# Génération d'image Kling

Le nœud de génération d'images Kling génère des images à partir d'invites textuelles avec la possibilité d'utiliser une image de référence comme guide. Il crée une ou plusieurs images en fonction de votre description textuelle et des paramètres de référence, puis renvoie les images générées en sortie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Invite de texte positive | STRING | Oui | Maximum 500 caractères |
| `negative_prompt` | Invite de texte négative | STRING | Oui | Maximum 500 caractères |
| `image_type` | Sélection du type de référence d'image (avancé). Requis lorsqu'une image de référence est fournie. | COMBO | Oui | `"subject_reference"`<br>`"style_reference"` |
| `image_fidelity` | Intensité de référence pour les images téléversées par l'utilisateur (par défaut : 0.5, avancé) | FLOAT | Oui | 0.0 - 1.0 |
| `human_fidelity` | Similarité de référence du sujet (par défaut : 0.45, avancé) | FLOAT | Oui | 0.0 - 1.0 |
| `model_name` | Sélection du modèle pour la génération d'images (par défaut : "kling-v3") | COMBO | Oui | `"kling-v3"` |
| `aspect_ratio` | Format d'image pour les images générées (par défaut : "16:9") | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` |
| `n` | Nombre d'images générées (par défaut : 1) | INT | Oui | 1 - 9 |
| `image` | Image de référence facultative | IMAGE | Non | - |
| `seed` | Le seed contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quel que soit le seed (par défaut : 0) | INT | Non | 0 - 2147483647 |

**Contraintes des paramètres :**

- Le paramètre `image` est facultatif. Lorsqu'une image de référence est fournie, le paramètre `image_type` détermine si la référence est utilisée comme référence de sujet ou comme référence de style.
- Lorsqu'aucune image de référence n'est fournie, les paramètres liés à la référence (`image_type`, `image_fidelity`, `human_fidelity`) n'ont aucun effet sur le résultat.
- `prompt` et `negative_prompt` ont une longueur maximale de 500 caractères.
- Le paramètre `seed` est facultatif et ne garantit pas des résultats déterministes.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `output` | Image(s) générée(s) en fonction des paramètres d'entrée. Lorsque `n` est supérieur à 1, plusieurs images sont renvoyées sous forme de lot. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/fr.md)

---
**Source fingerprint (SHA-256):** `fd344519346f63ac03975b93f03725749ed9697245d6dfa2378884c59a5325cd`
