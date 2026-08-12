# Flux3ImageToVideoNode

---

Flux 3 Image to Video anime 1 à 10 images avec FLUX 3. Chaque image devient une frame du clip : une image l’ouvre, deux opèrent une transition de la première à la seconde, et plus de deux sont réparties sur toute la durée ou épinglées à des instants que vous choisissez.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | La manière dont la scène doit bouger et sonner ; le prompt est interprété et étendu avant la génération. Doit contenir au moins un caractère. | STRING | Oui | Texte multiligne (défaut : vide) |
| `keyframes` | 1 à 10 images, dans l’ordre de lecture. Minimum 256x256 pixels chacune. Chaque keyframe devient un point du clip. | IMAGE | Oui | 1 à 10 images |
| `placement` | `'spread across the clip'` laisse FLUX 3 placer les images (une ouvre le clip, deux en deviennent le début et la fin) ; `'at times'` épingle chaque image à une seconde que vous choisissez. | STRING | Oui | `"spread across the clip"` (défaut)<br>`"at times"` |
| `times` | Un temps en secondes par image, séparé par des virgules et croissant, p. ex. `'0, 2.5, 5'`. Requis quand `placement` est `"at times"`. | STRING | Non | Secondes séparées par des virgules (défaut : "0") |
| `aspect_ratio` | Ratio d’aspect de la sortie. `'auto'` en choisit un à partir du prompt et des entrées. | STRING | Oui | `"auto"` (défaut)<br>plus d’autres options disponibles |
| `duration` | Durée du clip en secondes. `'auto'` ajuste la durée au contenu. | STRING | Oui | `"auto"` (défaut)<br>plus d’autres options disponibles |
| `resolution` | Résolution de sortie. | STRING | Oui | `"720p"` (défaut)<br>`"1080p"` |
| `generate_audio` | Générer un audio synchronisé (ambiance, parole, effets). Désactivé produit une vidéo sans piste audio. | BOOLEAN | Oui | true / false (défaut : true) |
| `safety_tolerance` | Tolérance de modération, 0 étant le plus strict. Les requêtes qui envoient des images ou des vidéos sont plafonnées à 2, quelle que soit la valeur définie. | INT | Oui | 0 à 4 (défaut : 2, paramètre avancé) |
| `seed` | Graine déterminant si le nœud doit se relancer ; FLUX 3 choisit sa propre graine, donc les résultats réels sont non déterministes quelle que soit cette valeur. | INT | Oui | 0 à 4294967295 (défaut : 42, avec contrôle après génération) |

Note : `keyframes` est requis — le nœud lève une erreur si aucune image keyframe n’est connectée. Quand `placement` est `"spread across the clip"` et que 3 images ou plus sont fournies, `duration` doit être défini sur une valeur explicite (pas `"auto"`) ; sinon le nœud lève une erreur. Quand `placement` est `"at times"`, `times` doit fournir un temps en secondes par image, dans l’ordre croissant. Les requêtes qui envoient des images sont plafonnées à une tolérance de sécurité de 2, quelle que soit la valeur définie.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Le clip vidéo généré à partir des images keyframe avec le ratio d’aspect, la durée, la résolution et le réglage audio choisis. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3ImageToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `3b9472194020ec98cd4e8c60463cdd0e9dc074ec6cbc1fc03d313894fa570ba8`
