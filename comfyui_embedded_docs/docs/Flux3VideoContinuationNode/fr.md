# Flux 3 Continuation Vidéo

Ce nœud prolonge un clip vidéo existant avec FLUX 3 : le nouveau clip reprend à partir des dernières images de la vidéo que vous fournissez. Il téléverse votre clip source, envoie le prompt et les paramètres au service de génération, puis renvoie la vidéo de suite obtenue une fois qu'elle est prête.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `video` | Le clip à prolonger. | VIDEO | Oui | Clip vidéo unique |
| `prompt` | Ce que la suite doit montrer ; le prompt est interprété et développé avant la génération. (par défaut : "") | STRING | Oui | Texte non vide (minimum 1 caractère) |
| `aspect_ratio` | Format d'image de sortie. 'auto' en sélectionne un à partir du prompt et des entrées. (par défaut : "auto") | COMBO | Oui | "auto" (par défaut)<br>Plusieurs options prédéfinies |
| `duration` | Durée du clip en secondes. 'auto' adapte la durée au contenu. (par défaut : "auto") | COMBO | Oui | "auto" (par défaut)<br>Valeurs numériques en secondes |
| `resolution` | Résolution de sortie. (par défaut : "720p") | COMBO | Oui | "720p" (par défaut)<br>"1080p"<br>Autres options prédéfinies |
| `generate_audio` | Générer un audio synchronisé (ambiance, voix, effets). Désactivé produit une vidéo sans piste audio. (par défaut : true) | BOOLEAN | Oui | true<br>false |
| `safety_tolerance` | Tolérance de modération, 0 est la plus stricte. Les requêtes qui envoient des images ou une vidéo sont plafonnées à 2 quelle que soit la valeur définie ici. (paramètre avancé, par défaut : 2) | INT | Oui | 0 - 4 (maximum effectif : 2 pour les requêtes vidéo) |
| `seed` | Graine permettant de déterminer si le nœud doit être réexécuté ; FLUX 3 choisit sa propre graine, donc les résultats réels sont non déterministes quelle que soit cette valeur. (par défaut : 42) | INT | Oui | 0 - 4294967295 (0xFFFFFFFF) |

### Remarques

- `prompt` doit contenir au moins un caractère, sinon la génération échoue. Bien que le champ ait une valeur par défaut de chaîne vide, un prompt non vide est requis pour exécuter le nœud.
- `safety_tolerance` accepte toute valeur de 0 à 4, mais comme ce nœud envoie une vidéo à l'API, la tolérance effective est plafonnée à 2 quelle que soit la valeur sélectionnée.
- Lorsque `duration` est défini sur un nombre, il est converti en un nombre entier de secondes. La valeur spéciale "auto" permet au service d'adapter la durée au contenu.
- Les listes d'options exactes pour `aspect_ratio`, `duration` et `resolution` sont définies en interne par le nœud. Les options de résolution incluent au moins "720p" (valeur par défaut) et "1080p". La tarification est calculée à partir de la `resolution` et de la `duration` sélectionnées ; "1080p" est facturé à $0.7579 par seconde, tandis que les autres résolutions sont facturées à $0.5863 par seconde.
- `seed` contrôle uniquement si le nœud est réexécuté ; il n'est pas envoyé au service de génération.
- Les champs d'authentification et d'identification du nœud (`auth_token_comfy_org`, `api_key_comfy_org`, `unique_id`) sont masqués et gérés automatiquement par la plateforme.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Le clip de suite généré par FLUX 3, qui reprend à partir de la fin de la vidéo source. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3VideoContinuationNode/fr.md)

---
**Source fingerprint (SHA-256):** `129ad0eb62c368854cebb010cc886aecac4caab00f9111143b883d028d7c30d9`
