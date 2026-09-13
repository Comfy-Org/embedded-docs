# BriaReplaceImageBackground

Ce nœud remplace l'arrière-plan d'une image par un nouveau généré par Bria. Le nouvel arrière-plan peut être décrit avec un prompt textuel ou guidé par des images de référence. Les pixels du sujet sont préservés tandis que l'arrière-plan est généré autour d'eux.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image d'entrée dont l'arrière-plan sera remplacé. | IMAGE | Oui | |
| `background` | Décrivez le nouvel arrière-plan avec un prompt, ou guidez-le avec des images de référence. | DYNAMIC_COMBO | Oui | `"prompt"`<br>`"reference images"` |
| `original_quality` | Renvoie la taille exacte en pixels de l'entrée au lieu de redimensionner le résultat à environ 1 mégapixel. Une grande entrée renvoie alors une grande image. (par défaut : false) | BOOLEAN | Non | `true`<br>`false` |
| `seed` | La même graine renvoie généralement le même arrière-plan ; l'affinement automatique du prompt peut toutefois le faire varier. (par défaut : 42) | INT | Non | 0 à 2147483647 |
| `moderation` | Paramètres de modération. (par défaut : "false") | DYNAMIC_COMBO | Non | `"false"`<br>`"true"` |

### Entrées du prompt

Affiché lorsque `background` est défini sur `"prompt"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Description du nouvel arrière-plan. Un code couleur hexadécimal tel que #FF5733 produit un arrière-plan de couleur unie. Doit contenir au moins 1 caractère. | STRING | Oui | |
| `mode` | `high_control` suit le prompt de plus près, `base` est un réglage équilibré par défaut et `fast` privilégie la vitesse au détriment des détails. | COMBO | Oui | `"high_control"`<br>`"base"`<br>`"fast"` |
| `refine_prompt` | Réécrit le prompt pour de meilleurs résultats, ce qui traduit également les prompts non anglophones. Désactivez-le pour envoyer le prompt exactement tel qu'écrit. (par défaut : true) | BOOLEAN | Non | `true`<br>`false` |

### Entrées des images de référence

Affiché lorsque `background` est défini sur `"reference images"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `ref_images` | Emplacement extensible : connectez 1 à 10 images guidant le nouvel arrière-plan ; elles n'ont pas besoin de partager une taille. Chaque référence modifie le résultat, donc quelques références cohérentes valent mieux que de nombreuses références contradictoires. Une entrée par lots compte une fois par image. | IMAGE | Oui | 1 à 10 images |
| `enhance_ref_images` | Traitement supplémentaire des images de référence pour de meilleurs résultats. (par défaut : true) | BOOLEAN | Non | `true`<br>`false` |

### Entrées de modération

Affiché lorsque `moderation` est défini sur `"true"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt_content_moderation` | Active la modération du contenu du prompt. (par défaut : false) | BOOLEAN | Non | `true`<br>`false` |
| `visual_input_moderation` | Active la modération de l'entrée visuelle. (par défaut : false) | BOOLEAN | Non | `true`<br>`false` |
| `visual_output_moderation` | Active la modération de la sortie visuelle. (par défaut : false) | BOOLEAN | Non | `true`<br>`false` |

**Remarque :** L'entrée `ref_images` accepte un maximum de 10 images ; en fournir plus de 10 renvoie une erreur. Le champ `prompt` doit contenir au moins 1 caractère. Lorsque `original_quality` est false, l'image d'entrée est réduite à environ 1 mégapixel avant traitement.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image avec le nouvel arrière-plan. | IMAGE |
| `refined_prompt` | Le prompt utilisé par Bria pour la génération, vide lorsque le chemin des images de référence est utilisé. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaReplaceImageBackground/fr.md)

---
**Source fingerprint (SHA-256):** `62c29d61983c9656d2ea2954518404c62d76961c3deba0e10d63e787d0b0b106`
