# Flux 3 Continuation Vidéo

Ce nœud prolonge un clip vidéo existant avec FLUX 3 : le nouveau clip reprend à partir des dernières images de la vidéo fournie. Il télécharge votre clip source, envoie la requête et les paramètres au service de génération, puis renvoie la vidéo de continuation une fois celle-ci prête.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `vidéo` | Le clip à prolonger. | VIDEO | Oui | Clip vidéo unique |
| `prompt` | Ce que la continuation doit montrer ; la requête est interprétée et développée avant la génération. (défaut : "") | STRING | Oui | Texte non vide (minimum 1 caractère) |
| `rapport d'aspect` | Format de l'image de sortie. « auto » en choisit un en fonction de la requête et des entrées. (défaut : "auto") | COMBO | Oui | "auto" (défaut)<br>Plusieurs options prédéfinies |
| `durée` | Durée du clip en secondes. « auto » adapte la durée au contenu. (défaut : "auto") | COMBO | Oui | "auto" (défaut)<br>Valeurs numériques en secondes |
| `résolution` | Résolution de sortie. (défaut : "720p") | COMBO | Oui | "720p" (défaut)<br>"1080p"<br>Autres options prédéfinies |
| `générer l'audio` | Générer un son synchronisé (ambiance, parole, effets). Désactivé produit une vidéo sans piste audio. (défaut : true) | BOOLEAN | Oui | true<br>false |
| `tolérance de sécurité` | Tolérance de modération, 0 étant le plus strict. Les requêtes envoyant des images ou des vidéos sont plafonnées à 2, quelle que soit la valeur définie ici. (paramètre avancé, défaut : 2) | INT | Oui | 0 - 4 (maximum effectif : 2 pour les requêtes vidéo) |
| `seed` | Graine déterminant si le nœud doit être réexécuté ; FLUX 3 choisit sa propre graine, donc les résultats réels sont non déterministes quelle que soit cette valeur. (paramètre avancé, défaut : 42) | INT | Oui | 0 - 4294967295 (0xFFFFFFFF) |

### Remarques

- `prompt` doit contenir au moins un caractère, sinon la génération échoue. Bien que le champ soit vide par défaut, une requête non vide est requise pour exécuter le nœud.
- `safety_tolerance` accepte toute valeur de 0 à 4, mais comme ce nœud envoie une vidéo à l'API, la tolérance effective est plafonnée à 2 quelle que soit la valeur sélectionnée.
- Lorsque `duration` est défini sur un nombre, il est converti en un nombre entier de secondes. La valeur spéciale « auto » permet au service d'adapter la durée au contenu.
- Les listes exactes d'options pour `aspect_ratio`, `duration` et `resolution` sont définies en interne par le nœud. Les options de résolution incluent au moins « 720p » (le défaut) et « 1080p ». Le prix est calculé à partir de la `resolution` et de la `duration` sélectionnées ; la « 1080p » est facturée à 0,7579 $ par seconde, tandis que les autres résolutions sont facturées à 0,5863 $ par seconde.
- Les champs d'authentification et d'identification du nœud (`auth_token_comfy_org`, `api_key_comfy_org`, `unique_id`) sont masqués et gérés automatiquement par la plateforme.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Le clip de continuation généré par FLUX 3, qui reprend à partir de la fin de la vidéo source. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3VideoContinuationNode/fr.md)

---
**Source fingerprint (SHA-256):** `129ad0eb62c368854cebb010cc886aecac4caab00f9111143b883d028d7c30d9`
