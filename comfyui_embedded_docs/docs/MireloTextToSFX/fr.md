# Mirelo Text to SFX

Génère un effet sonore à partir d’une description textuelle avec Mirelo SFX. Décrivez le son lui-même, pas l’image à laquelle il appartient, et le nœud renvoie une piste audio unique de la durée demandée. Utilisez-le pour le bruitage, les ambiances, les impacts et de courtes textures musicales sans filmer ni téléverser de vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Modèle à utiliser. La sélection d’un modèle révèle les paramètres qui lui sont propres : `prompt`, `negative_prompt`, `duration` et `seed`. | DYNAMIC_COMBO | Oui | `"sfx-2.0"` |
| `prompt` | Décrivez le son, pas l’image. 1 à 2000 caractères. | STRING | Oui | 1 à 2000 caractères |
| `negative_prompt` | Sons à éviter, sous la forme d’une courte liste séparée par des virgules. Peut rester vide (par défaut : vide). Maximum 1000 caractères. | STRING | Oui | Jusqu’à 1000 caractères |
| `duration` | Durée du son en secondes. (par défaut : 5.0) | FLOAT | Oui | 0.1 à 600.0 (pas de 0.1) |
| `seed` | La graine de la requête. Les résultats sont non déterministes, donc une même graine ne reproduit pas le même son. (par défaut : 42) | INT | Oui | 0 à 4294967295 |

Le nœud s’arrête avec une erreur lorsque `prompt` est vide ou dépasse 2000 caractères, et lorsque `negative_prompt` dépasse 1000 caractères.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `AUDIO` | L’effet sonore généré, d’une durée égale à `duration`. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MireloTextToSFX/fr.md)

---
**Source fingerprint (SHA-256):** `b09a9562cea636702acd9fc50feb38b272a558f8b8509da21f5fada2abd9fd48`
