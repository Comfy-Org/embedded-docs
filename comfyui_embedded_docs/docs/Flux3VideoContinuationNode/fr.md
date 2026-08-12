# Flux3VideoContinuationNode

Ce nœud prolonge un clip vidéo existant avec FLUX 3, de sorte que le nouveau clip prend la suite des dernières images de la vidéo que vous fournissez. Il téléverse votre clip source, envoie le prompt et les paramètres au service de génération, puis renvoie la vidéo de continuation obtenue une fois qu’elle est prête.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `video` | Le clip à prolonger. | VIDEO | Oui | Clip vidéo unique |
| `prompt` | Ce que la continuation doit montrer ; le prompt est interprété et développé avant la génération. (défaut : "") | STRING | Oui | Texte non vide (minimum 1 caractère) |
| `aspect_ratio` | Rapport d’aspect de sortie. 'auto' en choisit un à partir du prompt et des entrées. (défaut : "auto") | STRING | Oui | Plusieurs options prédéfinies (défaut : "auto") |
| `duration` | Durée du clip en secondes. 'auto' adapte la durée au contenu. (défaut : "auto") | STRING | Oui | "auto" (défaut)<br>Valeurs numériques en secondes |
| `resolution` | Résolution de sortie. (défaut : "720p") | STRING | Oui | Plusieurs options prédéfinies (défaut : "720p") |
| `generate_audio` | Générer un son synchronisé (ambiance, parole, effets). La valeur Off produit une vidéo sans piste audio. (défaut : true) | BOOLEAN | Oui | true<br>false |
| `safety_tolerance` | Tolérance de modération, 0 étant le plus strict. Les requêtes qui envoient des images ou des vidéos sont plafonnées à 2, quelle que soit la valeur définie ici. (paramètre avancé, défaut : 2) | INT | Oui | 0 - 4 (maximum effectif : 2 pour les requêtes vidéo) |
| `seed` | Seed permettant de déterminer si le nœud doit s’exécuter à nouveau ; FLUX 3 choisit lui-même la seed, donc les résultats réels sont non déterministes quelle que soit cette valeur. (paramètre avancé, défaut : 42) | INT | Oui | 0 - 4294967295 (0xFFFFFFFF) |

### Remarques

- `prompt` doit contenir au moins un caractère, sinon la génération échoue. Bien que le champ soit vide par défaut, un prompt non vide est requis pour exécuter le nœud.
- `safety_tolerance` accepte n’importe quelle valeur de 0 à 4, mais comme ce nœud envoie une vidéo à l’API, la tolérance effective est plafonnée à 2, quelle que soit la valeur sélectionnée.
- Lorsque `duration` est défini sur un nombre, il est converti en un nombre entier de secondes. La valeur spéciale "auto" permet au service d’adapter la durée au contenu.
- Les listes exactes d’options pour `aspect_ratio`, `duration` et `resolution` sont définies en interne par le nœud. Les options de résolution incluent au moins "720p" (la valeur par défaut) et "1080p", qui utilise un tarif différent.
- Les champs d’authentification et d’identification du nœud (`auth_token_comfy_org`, `api_key_comfy_org`, `unique_id`) sont masqués et gérés automatiquement par la plateforme.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `video` | Le clip de continuation généré par FLUX 3, qui reprend à partir de la fin de la vidéo source. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3VideoContinuationNode/fr.md)

---
**Source fingerprint (SHA-256):** `4b3a3df86b870edd696d10d352c7123b9c6c60ce0b57910529fca60615efa9f9`
