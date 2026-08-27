# FluxVideoUpscaleNode

Flux Video Upscale agrandit un clip vidéo de 1,5 à 3 fois grâce à la super-résolution FLUX. En mode créatif, il restaure et invente des détails fins ; en mode précis, il accentue la netteté de la source sans la modifier.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `video` | Clip source d'une durée de 1 à 20 secondes avec un rapport hauteur/largeur compris entre 1:4 et 4:1. La sortie est rendue à 24 fps et plafonnée à environ 14,4 mégapixels par image. | VIDEO | Oui | Durée de 1 à 20 secondes ; rapport hauteur/largeur entre 1:4 et 4:1 ; minimum 64x64 pixels |
| `upscale_factor` | Taille de sortie par rapport à la source. Les sources très grandes sont agrandies d'un facteur inférieur à celui demandé en raison du plafond par image. (par défaut : 2.0) | FLOAT | Oui | 1.5 à 3.0 (pas 0.1) |
| `mode` | Le mode 'creative' restaure et invente des détails fins, idéal pour les séquences générées, les textures et les paysages. Le mode 'precise' accentue la netteté de la source sans la modifier, pour les visages, les produits et les séquences réelles. (par défaut : "creative") | COMBO | Oui | "creative"<br>"precise" |
| `prompt` | Description facultative du clip qui oriente les détails améliorés. Laissez vide pour un agrandissement neutre. (par défaut : vide) | STRING | Oui | Texte multiligne |
| `auto_downscale` | Réduit automatiquement les sources dont la surface dépasse 3840x2160 pixels pour respecter la limite d'entrée. Le rapport hauteur/largeur est préservé ; les vidéos plus petites ne sont pas modifiées. (par défaut : true) | BOOLEAN | Oui | true<br>false |
| `safety_tolerance` | Tolérance de modération, 0 est le plus strict. (par défaut : 2, paramètre avancé) | INT | Oui | 0 à 4 |
| `seed` | Seed pour déterminer si le nœud doit se réexécuter ; FLUX choisit sa propre seed, donc les résultats réels sont non déterministes quelle que soit cette valeur. (par défaut : 42) | INT | Oui | 0 à 4294967295 |

Remarque : La vidéo source doit avoir une durée comprise entre 1 et 20 secondes et une taille d'au moins 64x64 pixels. Si `auto_downscale` est désactivé et que la zone vidéo dépasse 3840x2160 pixels, le nœud lève une erreur. La vidéo de sortie est rendue à 24 fps et plafonnée à environ 14,4 mégapixels par image, donc les sources très grandes peuvent être agrandies d'un facteur inférieur à celui demandé.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Le clip vidéo agrandi. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVideoUpscaleNode/fr.md)

---
**Source fingerprint (SHA-256):** `22dcf7c176705ce21a9032b1c9f4fe82ee6aa153f5057b90dac653b37281a677`
