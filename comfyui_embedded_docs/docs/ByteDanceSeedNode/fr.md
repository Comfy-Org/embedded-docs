# ByteDance Seed

Générez des réponses textuelles avec les modèles Seed 2.0 de ByteDance. Fournissez une invite textuelle et connectez éventuellement des images ou des vidéos pour donner au modèle un contexte supplémentaire. Le modèle est choisi parmi les variantes Seed 2.0 disponibles, et le nœud renvoie la réponse textuelle du modèle.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Entrée textuelle pour le modèle. (par défaut : "") | STRING | Oui | N/A |
| `model` | Le modèle Seed utilisé pour générer la réponse. Ce sélecteur expose également les sous-paramètres du modèle. | DYNAMIC_COMBO | Oui | `"Seed 2.0 Pro"`<br>`"Seed 2.0 Lite"`<br>`"Seed 2.0 Mini"` |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. (par défaut : 0) | INT | Oui | 0 à 2147483647 |
| `system_prompt` | Instructions fondamentales qui dictent le comportement du modèle. (par défaut : "") | STRING | Non | N/A |

### Entrées du modèle (partagées par Seed 2.0 Pro, Seed 2.0 Lite et Seed 2.0 Mini)

Les trois modèles Seed exposent les mêmes sous-paramètres lorsqu'ils sont sélectionnés.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `temperature` | Contrôle l'aléatoire. 0,0 est déterministe, des valeurs plus élevées sont plus aléatoires. (par défaut : 1.0) | FLOAT | Oui | 0,0 à 2,0 (pas : 0,01) |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | Image(s) facultative(s) à utiliser comme contexte pour le modèle. Jusqu'à 20 images. Emplacement extensible : connectez 1..20 éléments, par ex. `image_1` jusqu'à `image_20`. | IMAGE | Non | 0 à 20 images |
| `videos` | Vidéo(s) facultative(s) à utiliser comme contexte pour le modèle. Jusqu'à 4 vidéos. Emplacement extensible : connectez 1..4 éléments, par ex. `video_1` jusqu'à `video_4`. | VIDEO | Non | 0 à 4 vidéos |

**Remarque :** Le paramètre `model` est une liste déroulante dynamique qui révèle les sous-paramètres de référence et de température une fois qu'un modèle est sélectionné. Les emplacements `images` et `videos` sont extensibles, vous pouvez donc connecter plusieurs entrées pour un contexte multimodal.

- `prompt` est requis et doit contenir au moins un caractère autre qu'un espace blanc ; sinon, une erreur est levée.
- Un maximum de 20 images est pris en charge par requête. Cette limite compte toutes les images de tous les lots connectés.
- Un maximum de 4 vidéos est pris en charge par requête.
- Une erreur est levée si le modèle renvoie une réponse vide, ou s'il refuse de répondre (le texte de refus est signalé).

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | Réponse textuelle générée par le modèle Seed. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedNode/fr.md)

---
**Source fingerprint (SHA-256):** `23c9b0e9983a65ce859e2e92acfe71604297f16d711fa094a6617a9915a46020`
