# ByteDance Seed

ByteDance Seed génère des réponses textuelles à l'aide des modèles Seed 2.0 de ByteDance. Fournissez un prompt textuel et incluez éventuellement une ou plusieurs images ou vidéos pour un contexte multimodal.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle Seed utilisé pour générer la réponse. | DYNAMIC_COMBO | Oui | `"Seed 2.0 Pro"`<br>`"Seed 2.0 Lite"`<br>`"Seed 2.0 Mini"` |
| `prompt` | Invite textuelle pour le modèle. (défaut : "") | STRING | Oui | N/A |
| `seed` | Le `seed` contrôle si le nœud doit se relancer ; les résultats sont non déterministes quel que soit le seed. (défaut : 0) | INT | Oui | 0 à 2147483647 |
| `system_prompt` | Instructions fondamentales qui dictent le comportement du modèle. (défaut : "") | STRING | Non | N/A |

### Entrées Seed 2.0 Pro, Seed 2.0 Lite et Seed 2.0 Mini

Ce paramètre est commun aux trois options de modèle.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `temperature` | Contrôle le caractère aléatoire. 0.0 est déterministe, des valeurs plus élevées sont plus aléatoires. (défaut : 1.0) | FLOAT | Oui | 0.0 à 2.0 |

### Entrées de référence

Le sélecteur `model` fournit ces emplacements extensibles, qui connectent des images et des vidéos pour donner un contexte multimodal au modèle.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | Image(s) facultative(s) à utiliser comme contexte pour le modèle. Jusqu'à 20 images. Emplacement extensible : connectez 1 à 20 éléments (par ex. `image_1`...`image_20`). | IMAGE | Non | `image_1` à `image_20` |
| `videos` | Vidéo(s) facultative(s) à utiliser comme contexte pour le modèle. Jusqu'à 4 vidéos. Emplacement extensible : connectez 1 à 4 éléments (par ex. `video_1`...`video_4`). | VIDEO | Non | `video_1` à `video_4` |

**Remarque :** Le sélecteur `model` détermine quel modèle Seed est utilisé pour générer la réponse. Chaque option correspond à un identifiant de modèle spécifique : `"Seed 2.0 Pro"` → `seed-2-0-pro-260328`, `"Seed 2.0 Lite"` → `seed-2-0-lite-260228`, et `"Seed 2.0 Mini"` → `seed-2-0-mini-260215`.

**Remarque sur les contraintes :** Un maximum de 20 images et 4 vidéos est pris en charge par requête. Le `prompt` doit être une chaîne non vide.

**Remarque sur la tarification :** La tarification est basée sur les tokens et affichée dans l'interface du nœud comme une fourchette approximative par 1K tokens : Seed 2.0 Mini : 0.00025 $ - 0.0009 $ ; Seed 2.0 Lite : 0.0003 $ - 0.002 $ ; Seed 2.0 Pro : 0.0005 $ - 0.003 $.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La réponse textuelle générée par le modèle Seed. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedNode/fr.md)

---
**Source fingerprint (SHA-256):** `23c9b0e9983a65ce859e2e92acfe71604297f16d711fa094a6617a9915a46020`
