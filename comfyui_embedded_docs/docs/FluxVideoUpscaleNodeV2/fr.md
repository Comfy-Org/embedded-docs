# Flux Video Upscale

Flux Video Upscale agrandit une vidéo grâce à la super-résolution FLUX, soit vers une taille d’image fixe de 1080p, 2K ou 4K, soit par un facteur de 1,5 à 3. Le mode creative restaure et invente les détails fins, ce qui convient aux séquences générées ; le mode precise accentue la netteté de la source sans la modifier, ce qui convient aux visages, aux produits et aux séquences réelles. Le clip est téléversé, la tâche BFL est interrogée, et la vidéo terminée est renvoyée à 24 images/s.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `video` | Clip source de 1 à 20 secondes et 50 Mo maximum, d’au moins 64x64 pixels, avec un rapport d’aspect compris entre 1:4 et 4:1. La sortie est rendue à 24 images/s et limitée à environ 14,4 mégapixels par image. | VIDEO | Oui | Durée de 1 à 20 secondes ; rapport d’aspect compris entre 1:4 et 4:1 ; minimum 64x64 pixels |
| `target_resolution` | Taille de sortie. `"1080p"`, `"2K"` et `"4K"` ajustent le résultat dans 1920x1080, 2560x1440 ou 3840x2160 pixels, avec une orientation adaptée aux clips en portrait ; `"by factor"` utilise `upscale_factor` à la place. | DYNAMIC_COMBO | Oui | `"2K"`<br>`"4K"`<br>`"1080p"`<br>`"by factor"` |
| `mode` | `"creative"` restaure et invente les détails fins, idéal pour les séquences générées, les textures et les paysages. `"precise"` accentue la netteté de la source sans la modifier, pour les visages, les produits et les séquences réelles. (par défaut : `"creative"`) | COMBO | Oui | `"creative"`<br>`"precise"` |
| `prompt` | Description facultative du clip qui oriente le détail amélioré. Laisser vide pour un agrandissement neutre. (par défaut : vide) | STRING | Oui | Texte multiligne |
| `auto_downscale` | Réduit l’échelle des sources trop volumineuses au lieu de les rejeter : au-dessus de 2560x1440 pixels en surface, ou au-dessus de deux tiers de la résolution cible. Le rapport d’aspect est conservé. (par défaut : true) | BOOLEAN | Oui | true<br>false |
| `safety_tolerance` | Tolérance de modération ; 0 correspond au niveau le plus strict. (par défaut : 2, paramètre avancé) | INT | Oui | 0 à 4 |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; FLUX choisit sa propre graine, les résultats réels sont donc non déterministes indépendamment de cette valeur. (par défaut : 42) | INT | Oui | 0 à 4294967295 |

### Entrées by factor

Ces entrées apparaissent lorsque `target_resolution` est défini sur `"by factor"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `upscale_factor` | Taille de sortie relative à la source. Les sources très volumineuses sont agrandies par un facteur inférieur à celui demandé en raison de la limite par image. (par défaut : 2.0) | FLOAT | Oui | 1.5 à 3.0 (pas 0.1) |

Une taille cible est appliquée sous forme de facteur d’agrandissement limité à 1,5-3,0 ; une source trop petite pour remplir le cadre à 3× ressort donc plus petite que la résolution demandée, et une source qui nécessiterait moins de 1,5× pour tenir dans le cadre est d’abord réduite. Lorsque `auto_downscale` est désactivé, le nœud s’arrête avec une erreur au lieu de réduire l’échelle. La sortie est à 24 images/s et limitée à environ 14,4 mégapixels par image ; les sources très volumineuses peuvent donc être agrandies par un facteur inférieur à celui demandé.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Le clip vidéo agrandi. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVideoUpscaleNodeV2/fr.md)

---
**Source fingerprint (SHA-256):** `bef6ef4614d75bc9e6bab977f5f19c45fe30d300907913462a058e6e7e7e4ac7`
