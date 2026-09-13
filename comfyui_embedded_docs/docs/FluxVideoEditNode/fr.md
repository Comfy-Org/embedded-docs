# Édition vidéo Flux

Modifie un clip vidéo existant à partir d'une instruction écrite. Vous pouvez supprimer, ajouter ou remplacer des objets, modifier le décor, restyler la séquence, modifier le texte à l'écran ou remplacer le dialogue parlé. La durée, le cadrage, le mouvement de caméra et l'audio proviennent du clip source, donc tout ce que vous ne mentionnez pas dans le prompt est censé rester tel quel.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `video` | Clip source de 0,7 à 15 secondes, d'au moins 160x160 pixels. La sortie est rendue à 24 fps et limitée à environ 0,9 mégapixel par image, donc une source plus grande est renvoyée plus petite. | VIDEO | Oui | 0,7 à 15 secondes ; minimum 160x160 pixels |
| `prompt` | Ce qu'il faut modifier, en langage simple, jusqu'à 4096 caractères. Tout ce que vous ne mentionnez pas est censé rester tel quel. Le dialogue de remplacement doit s'adapter à la durée de la parole d'origine, et un clip silencieux reste silencieux. Par défaut : chaîne vide. | STRING | Oui | 1 à 4096 caractères |
| `auto_downscale` | Réduit automatiquement l'échelle des sources dont la surface est supérieure à 1280x704 pixels avant l'envoi. Le rapport d'aspect est préservé ; les vidéos plus petites ne sont pas modifiées. Par défaut : true. | BOOLEAN | Non | true<br>false |
| `safety_tolerance` | Tolérance de modération, 0 étant la plus stricte. Par défaut : 4. | INT | Non | 0 à 4 |
| `seed` | Graine permettant de déterminer si le nœud doit être réexécuté ; FLUX choisit sa propre graine, donc les résultats réels sont non déterministes quelle que soit cette valeur. Par défaut : 42. | INT | Non | 0 à 4294967295 |

**Remarque :** Le `prompt` doit contenir au moins 1 caractère et au plus 4096 caractères. La source `video` doit durer entre 0,7 et 15 secondes et mesurer au moins 160x160 pixels ; les envois qui dépassent ces limites sont rejetés avant l'envoi de la requête.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | Le clip vidéo modifié renvoyé par le service FLUX. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVideoEditNode/fr.md)

---
**Source fingerprint (SHA-256):** `169b14700acfee3f6ccc247f08f3ae8c5f3c4610062a447e8215246460299b6a`
