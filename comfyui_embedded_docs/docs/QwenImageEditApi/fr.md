# QwenImageEditApi

Ce nœud utilise les modèles Qwen-Image 3.0 pour éditer ou combiner jusqu'à 3 images de référence guidées par un prompt texte. Vous fournissez le prompt texte et les images de référence, et le nœud renvoie le résultat généré sous forme d'une ou plusieurs images.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser. Cette sélection inclut également le prompt texte, jusqu'à 3 entrées d'images de référence et un prompt négatif optionnel. | COMBO | Oui | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `size` | Résolution de sortie. « match input » réutilise la taille de la première image de référence, « auto » laisse le modèle choisir une taille avec le même ratio d'aspect, « custom » définit une largeur et une hauteur explicites. | COMBO | Oui | "match input"<br>"auto"<br>"custom" |
| `n` | Nombre d'images à générer, renvoyé sous forme de lot. (défaut : 1) | INT | Non | 1 à 6 |
| `seed` | Seed à utiliser pour la génération. (défaut : 42) | INT | Non | 0 à 2147483647 |
| `prompt_extend` | Indique s'il faut améliorer le prompt avec l'assistance de l'IA. (défaut : True) | BOOLEAN | Non | True<br>False |
| `watermark` | Indique s'il faut ajouter un filigrane généré par l'IA au résultat. (défaut : False) | BOOLEAN | Non | True<br>False |

### Contraintes

- Le prompt texte est requis et doit contenir au moins un caractère.
- Un maximum de 3 images de référence est pris en charge ; une erreur est levée si plus d'images sont fournies (une entrée par lot compte pour une image).
- Lorsque `size` est défini sur « custom », des valeurs explicites de largeur et de hauteur doivent être fournies et sont validées.
- Lorsque `size` est défini sur « match input », au moins une image de référence est requise car les dimensions de la première image de référence sont utilisées.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| IMAGE | L'image ou les images générées renvoyées sous forme de lot. Jusqu'à `n` images sont renvoyées. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageEditApi/fr.md)

---
**Source fingerprint (SHA-256):** `efa8d2b1a039a7b91789c0332b751a5f90ab8dad755ef0e25124d7d1c44d9abb`
