# Mise à l’échelle vidéo Flux

Flux Video Upscale agrandit un clip vidéo de 1,5 à 3 fois à l'aide de la super-résolution FLUX. En mode créatif, il restaure et invente les détails fins ; en mode précis, il accentue la netteté de la source sans la modifier.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `video` | Clip source de 1 à 20 secondes avec un rapport d'aspect compris entre 1:4 et 4:1. La sortie est rendue à 24 ips et limitée à environ 14,4 mégapixels par image. | VIDEO | Oui | Durée de 1 à 20 secondes ; rapport d'aspect entre 1:4 et 4:1 ; minimum 64x64 pixels |
| `upscale_factor` | Taille de sortie relative à la source. Les sources très volumineuses sont agrandies par un facteur inférieur à celui demandé en raison de la limite par image. (par défaut : 2.0) | FLOAT | Oui | 1.5 à 3.0 (pas de 0.1) |
| `mode` | 'creative' restaure et invente les détails fins, idéal pour les séquences générées, les textures et les paysages. 'precise' accentue la netteté de la source sans la modifier, pour les visages, les produits et les séquences réelles. (par défaut : "creative") | COMBO | Oui | "creative"<br>"precise" |
| `prompt` | Description facultative du clip qui oriente les détails améliorés. Laisser vide pour un agrandissement neutre. (par défaut : vide) | STRING | Oui | Texte multiligne |
| `auto_downscale` | Réduit automatiquement l'échelle des sources dont la surface dépasse 3840x2160 pixels pour respecter la limite d'entrée. Le rapport d'aspect est préservé ; les vidéos plus petites ne sont pas modifiées. (par défaut : true) | BOOLEAN | Oui | true<br>false |
| `safety_tolerance` | Tolérance de modération, 0 étant la plus stricte. (par défaut : 2, paramètre avancé) | INT | Oui | 0 à 4 |
| `seed` | Graine permettant de déterminer si le nœud doit être réexécuté ; FLUX choisit sa propre graine, donc les résultats réels sont non déterministes quelle que soit cette valeur. (par défaut : 42) | INT | Oui | 0 à 4294967295 |

Remarque : La vidéo source doit durer entre 1 et 20 secondes, mesurer au moins 64x64 pixels et avoir un rapport d'aspect compris entre 1:4 et 4:1. Si `auto_downscale` est désactivé et que la surface de la vidéo dépasse 3840x2160 pixels, le nœud génère une erreur. La vidéo de sortie est rendue à 24 ips et limitée à environ 14,4 mégapixels par image ; les sources très volumineuses peuvent donc être agrandies par un facteur inférieur à celui demandé.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Le clip vidéo agrandi. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVideoUpscaleNode/fr.md)

---
**Source fingerprint (SHA-256):** `22dcf7c176705ce21a9032b1c9f4fe82ee6aa153f5057b90dac653b37281a677`
