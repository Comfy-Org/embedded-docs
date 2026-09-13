# Flux 3 Image vers Vidéo

Flux 3 Image to Video anime 1 à 10 images avec FLUX 3. Chaque image devient une image du clip : une image l'ouvre, deux effectuent un morphing de la première vers la seconde, et davantage sont réparties sur le clip ou fixées à des instants de votre choix.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `placement` | "spread across the clip" permet à FLUX 3 de placer les images (une ouvre le clip, deux deviennent son début et sa fin) ; "at times" fixe chaque image à une seconde de votre choix. | DYNAMIC_COMBO | Oui | `"spread across the clip"` (par défaut)<br>`"at times"` |
| `prompt` | Décrit comment la scène doit se déplacer et ce qu'elle doit produire comme son ; le prompt est interprété et développé avant la génération. Doit contenir au moins un caractère. | STRING | Oui | Texte multiligne (par défaut : vide) |
| `aspect_ratio` | Ratio d'aspect de sortie. "auto" en choisit un à partir du prompt et des entrées. | COMBO | Oui | `"auto"` (par défaut)<br>autres ratios d'aspect disponibles |
| `duration` | Durée du clip en secondes. "auto" adapte la durée au contenu. | COMBO | Oui | `"auto"` (par défaut)<br>autres durées disponibles |
| `resolution` | Résolution de sortie. | COMBO | Oui | `"720p"` (par défaut)<br>`"1080p"` |
| `generate_audio` | Génère de l'audio synchronisé (ambiance, paroles, effets). Désactivé produit une vidéo sans piste audio. | BOOLEAN | Oui | true / false (par défaut : true) |
| `safety_tolerance` | Tolérance de modération, 0 étant la plus stricte. Les requêtes qui envoient des images ou de la vidéo sont plafonnées à 2, quelle que soit la valeur définie ici. | INT | Oui | 0 à 4 (par défaut : 2, réglage avancé) |
| `seed` | Graine permettant de déterminer si le nœud doit être réexécuté ; FLUX 3 choisit sa propre graine, donc les résultats réels sont non déterministes quelle que soit cette valeur. | INT | Oui | 0 à 4294967295 (par défaut : 42, contrôle après génération) |

### Entrées spread across the clip

Cette option de placement n'a aucun paramètre supplémentaire.

### Entrées at times

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `times` | Un temps en secondes par image, séparé par des virgules et croissant, par ex. "0, 2.5, 5". N'apparaît que lorsque `placement` est "at times" ; un temps est requis pour chaque image clé. | STRING | Non | Secondes séparées par des virgules (par défaut : "0") |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `keyframes` | Emplacement extensible : connectez 1 à 10 images clés dans l'ordre de lecture, par ex. `image_1`, `image_2`, etc. Chaque image devient une image du clip. Minimum 256x256 pixels chacune ; le ratio d'aspect ne peut pas être plus extrême que 64:1. | IMAGE | Oui | 1 à 10 images |

Remarque : `keyframes` doit contenir au moins une image ; le nœud déclenche une erreur si aucune n'est connectée. Chaque image clé doit faire au moins 256x256 pixels et son ratio d'aspect ne peut pas être plus extrême que 64:1.

Lorsque `placement` est "spread across the clip" et que 3 images clés ou plus sont connectées, `duration` doit être défini sur une valeur explicite, et non "auto" ; sinon, le nœud déclenche une erreur.

Lorsque `placement` est "at times", `times` doit fournir un temps en secondes par image. Les temps doivent être croissants, ne peuvent pas être négatifs, et le dernier temps ne peut pas aller au-delà de la fin du clip (jusqu'à 20 secondes lorsque `duration` est "auto").

Comme ce nœud envoie des images, `safety_tolerance` est plafonné à 2, quelle que soit la valeur définie.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Le clip vidéo généré à partir des images clés avec le ratio d'aspect, la durée, la résolution et le réglage audio choisis. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3ImageToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `1c49838dfa13adc2ed70a51094f0dd860df7207970b8dceab6bb273653d7161c`
