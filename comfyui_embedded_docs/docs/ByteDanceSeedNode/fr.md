# ByteDance Seed

Générez des réponses textuelles à l'aide des modèles Seed 2.0 de ByteDance. Fournissez une invite textuelle et incluez éventuellement des images ou des vidéos pour un contexte multimodal.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle Seed utilisé pour générer la réponse. | DYNAMIC_COMBO | Oui | `"Seed 2.0 Pro"`<br>`"Seed 2.0 Lite"`<br>`"Seed 2.0 Mini"` |
| `invite` | Entrée textuelle du modèle. (défaut : "") | STRING | Oui | N/A |
| `seed` | La graine contrôle si le nœud doit s'exécuter à nouveau ; les résultats sont non déterministes quelle que soit la graine. (défaut : 0) | INT | Oui | 0 à 2147483647 |
| `invite système` | Instructions fondamentales qui déterminent le comportement du modèle. (défaut : "") | STRING | Non | N/A |

### Entrées du modèle (partagées par Seed 2.0 Pro, Seed 2.0 Lite et Seed 2.0 Mini)

Les trois modèles Seed exposent les mêmes sous-paramètres lorsqu'ils sont sélectionnés.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `temperature` | Contrôle le caractère aléatoire. 0.0 est déterministe, les valeurs plus élevées sont plus aléatoires. (défaut : 1.0) | FLOAT | Oui | 0.0 à 2.0 (step: 0.01) |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | Images facultatives à utiliser comme contexte pour le modèle. Jusqu'à 20 images. Emplacement extensible : connectez 1 à 20 éléments, par exemple `image_1` à `image_20`. | IMAGE | Non | 0 à 20 images |
| `videos` | Vidéos facultatives à utiliser comme contexte pour le modèle. Jusqu'à 4 vidéos. Emplacement extensible : connectez 1 à 4 éléments, par exemple `video_1` à `video_4`. | VIDEO | Non | 0 à 4 videos |

**Remarque :** Le paramètre `model` est une liste dynamique qui expose les sous-paramètres de référence et de température lorsqu'un modèle est sélectionné. Vous pouvez connecter des entrées d'images et de vidéos à ce paramètre pour fournir un contexte multimodal. Un maximum de 20 images et 4 vidéos est pris en charge par requête, et `prompt` est requis et doit contenir au moins un caractère non blanc.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La réponse textuelle générée par le modèle Seed. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedNode/fr.md)

---
**Source fingerprint (SHA-256):** `23c9b0e9983a65ce859e2e92acfe71604297f16d711fa094a6617a9915a46020`
