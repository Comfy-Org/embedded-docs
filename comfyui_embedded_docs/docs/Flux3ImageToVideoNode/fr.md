# Flux 3 Image vers Vidéo

Flux 3 Image to Video anime 1 à 10 images avec FLUX 3. Chaque image devient une image du clip : une image l'ouvre, deux images effectuent une transition de la première à la seconde, et les autres sont réparties sur toute la durée ou épinglées à des moments de votre choix.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Comment la scène doit bouger et sonner ; le prompt est interprété et développé avant la génération. Doit contenir au moins un caractère. | STRING | Oui | Texte multiligne (défaut : vide) |
| `keyframes` | 1 à 10 images, dans l'ordre de lecture. Minimum 256x256 pixels chacune. Entrée extensible : connectez les images comme `image_1`, `image_2`, etc. | IMAGE | Oui | 1 à 10 images |
| `placement` | « spread across the clip » laisse FLUX 3 placer les images (une image ouvre le clip, deux images en deviennent le début et la fin) ; « at times » épingle chaque image à une seconde de votre choix. | DYNAMIC_COMBO | Oui | `"spread across the clip"` (défaut)<br>`"at times"` |
| `times` | Un temps en secondes par image, séparés par des virgules et croissants, p. ex. « 0, 2.5, 5 ». N'apparaît que lorsque `placement` est « at times » ; un temps est requis pour chaque image clé. | STRING | Non | Secondes séparées par des virgules (défaut : "0") |
| `aspect_ratio` | Format d'image de sortie. « auto » en choisit un à partir du prompt et des entrées. | COMBO | Oui | `"auto"` (défaut)<br>autres formats d'image disponibles |
| `duration` | Durée du clip en secondes. « auto » adapte la longueur au contenu. | COMBO | Oui | `"auto"` (défaut)<br>autres durées disponibles |
| `resolution` | Résolution de sortie. | COMBO | Oui | `"720p"` (défaut)<br>`"1080p"` |
| `generate_audio` | Générer un audio synchronisé (ambiance, parole, effets). Désactivé produit une vidéo sans piste audio. | BOOLEAN | Oui | true / false (défaut : true) |
| `safety_tolerance` | Tolérance de modération, 0 est la plus stricte. Les requêtes qui envoient des images ou des vidéos sont plafonnées à 2, quelle que soit la valeur définie ici. | INT | Oui | 0 à 4 (défaut : 2, paramètre avancé) |
| `seed` | Graine (seed) pour déterminer si le nœud doit se relancer ; FLUX 3 choisit sa propre graine, donc les résultats réels sont non déterministes quelle que soit cette valeur. | INT | Oui | 0 à 4294967295 (défaut : 42, contrôle après génération) |

Remarque : `keyframes` doit contenir au moins une image ; le nœud génère une erreur si aucune n'est connectée. Chaque image clé doit faire au moins 256x256 pixels et son format d'image ne peut pas être plus extrême que 64:1.

Lorsque `placement` est « spread across the clip » et que 3 images clés ou plus sont connectées, `duration` doit être défini sur une valeur explicite, et non sur « auto » ; sinon le nœud génère une erreur.

Lorsque `placement` est « at times », `times` doit fournir un temps en secondes par image. Les temps doivent être croissants, ne peuvent pas être négatifs, et le dernier temps ne peut pas dépasser la fin du clip (jusqu'à 20 secondes lorsque `duration` est « auto »).

Comme ce nœud envoie des images, `safety_tolerance` est plafonné à 2, quelle que soit la valeur définie.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Le clip vidéo généré à partir des images clés, avec le format d'image, la durée, la résolution et le réglage audio choisis. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3ImageToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `1c49838dfa13adc2ed70a51094f0dd860df7207970b8dceab6bb273653d7161c`
