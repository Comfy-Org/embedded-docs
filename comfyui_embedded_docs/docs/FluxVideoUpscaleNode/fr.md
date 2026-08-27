# FluxVideoUpscaleNode

Flux Video Upscale agrandit un clip vidéo de 1,5 à 3 fois grâce à la super-résolution FLUX. En mode `creative`, il restaure et invente des détails fins ; en mode `precise`, il accentue la source sans la modifier.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|----------------|--------|-------|
| `video` | Clip source de 1 à 20 secondes avec un rapport hauteur/largeur compris entre 1:4 et 4:1. La sortie est rendue à 24 fps et plafonnée à environ 14,4 mégapixels par image. | VIDEO | Oui | Durée de 1 à 20 secondes ; rapport hauteur/largeur entre 1:4 et 4:1 ; minimum 64x64 pixels |
| `upscale_factor` | Taille de sortie par rapport à la source. Les sources très grandes sont agrandies avec un facteur inférieur à celui demandé en raison du plafond par image. (défaut : 2.0) | FLOAT | Oui | 1.5 à 3.0 (pas de 0.1) |
| `mode` | Le mode `creative` restaure et invente des détails fins, idéal pour les images générées, les textures et les paysages. Le mode `precise` accentue la source sans la modifier, pour les visages, les produits et les images réelles. (défaut : "creative") | COMBO | Oui | "creative"<br>"precise" |
| `prompt` | Description facultative du clip qui oriente l’amélioration des détails. Laissez vide pour un agrandissement neutre. (défaut : vide) | STRING | Oui | Texte multiligne |
| `auto_downscale` | Réduit automatiquement les sources dont la surface dépasse 3840x2160 pixels pour respecter la limite d’entrée. Le rapport hauteur/largeur est préservé ; les vidéos plus petites ne sont pas modifiées. (défaut : true) | BOOLEAN | Oui | true<br>false |
| `safety_tolerance` | Tolérance de modération, 0 étant la plus stricte. (défaut : 2, paramètre avancé) | INT | Oui | 0 à 4 |
| `seed` | Seed permettant de déterminer si le nœud doit s’exécuter à nouveau ; FLUX choisit sa propre seed, donc les résultats réels sont non déterministes quelle que soit cette valeur. (défaut : 42) | INT | Oui | 0 à 4294967295 |

Remarque : La vidéo source doit durer entre 1 et 20 secondes et mesurer au moins 64x64 pixels. Si `auto_downscale` est désactivé et que la surface de la vidéo dépasse 3840x2160 pixels, le nœud génère une erreur. La vidéo de sortie est rendue à 24 fps et plafonnée à environ 14,4 mégapixels par image ; par conséquent, les sources très grandes peuvent être agrandies avec un facteur inférieur à celui demandé.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Le clip vidéo agrandi. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVideoUpscaleNode/fr.md)

---
**Source fingerprint (SHA-256):** `22dcf7c176705ce21a9032b1c9f4fe82ee6aa153f5057b90dac653b37281a677`
