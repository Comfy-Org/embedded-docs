# Comfy Cloud MiniMax H3 Première-dernière image vers vidéo [BETA]

Exécute le workflow MiniMax H3 first-last frame sur un GPU Comfy Cloud et renvoie le mouvement entre deux images clés avec une bande-son assortie. Fournissez-lui les images d'ouverture et de fermeture, et le modèle comble le plan entre elles. La dernière image est facultative : omettez-la et le mouvement s'éloigne plutôt de la première image. Ce nœud est en version bêta et est facturé à la seconde de GPU.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `first_frame` | L'image à partir de laquelle la vidéo commence. Elle est téléversée jusqu'à 2048x2048 pixels avant l'exécution du workflow. | IMAGE | Oui | - |
| `last_frame` | Image de fermeture facultative. Lorsqu'elle est connectée, le mouvement généré se termine sur cette image ; sans elle, le mouvement s'éloigne de `first_frame`. | IMAGE | Non | - |
| `prompt` | Description textuelle du mouvement et des sons que le plan doit comporter. Les espaces de début et de fin sont supprimés avant la soumission. | STRING | Oui | 1 à 4096 caractères |
| `seed` | Graine aléatoire qui contrôle le résultat généré (valeur par défaut : 42). | INT | Oui | 0 à 18446744073709551615 |
| `aspect_ratio` | Rapport d'aspect de la vidéo générée (valeur par défaut : `"1:1"`). | COMBO | Oui | `"1:1"`<br>`"3:4"`<br>`"2:3"`<br>`"3:2"`<br>`"4:3"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"` |
| `resolution` | Budget de taille d'image (valeur par défaut : `"480p"`). La 720p coûte environ deux fois plus de secondes de GPU que la 480p. | COMBO | Oui | `"480p"`<br>`"720p"` |
| `duration_seconds` | Durée en secondes (valeur par défaut : 5). Le pipeline quantifie par pas de 17 images à 24 ips, de sorte que la durée du clip reste à environ deux tiers de seconde près de cette valeur. | INT | Oui | 5 à 15 |

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------------|
| `VIDEO` | La vidéo générée avec sa bande-son. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMiniMaxH3FirstLastFrameToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `5b9d1a2155951fb953e94726f0c6ca7720a805ab5d3015adaa5cc496acaa0de3`
