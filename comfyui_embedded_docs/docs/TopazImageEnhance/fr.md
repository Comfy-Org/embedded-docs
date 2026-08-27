# Topaz Amélioration d'image

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle IA à utiliser pour l'amélioration d'image. | COMBO | Oui | `"Reimagine"` |
| `image` | L'image d'entrée à améliorer. Une seule image est prise en charge. | IMAGE | Oui | - |
| `invite` | Invite de texte facultative pour guider la mise à l'échelle créative (par défaut : vide). | STRING | Non | - |
| `détection du sujet` | Contrôle la partie de l'image sur laquelle l'amélioration se concentre (par défaut : « All »). | COMBO | Non | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `amélioration du visage` | Améliorer les visages (s'ils sont présents) pendant le traitement (par défaut : True). | BOOLEAN | Non | - |
| `créativité de l'amélioration du visage` | Définir le niveau de créativité pour l'amélioration des visages (par défaut : 0.0). | FLOAT | Non | 0.0 - 1.0 |
| `intensité de l'amélioration du visage` | Contrôle la netteté des visages améliorés par rapport à l'arrière-plan (par défaut : 1.0). | FLOAT | Non | 0.0 - 1.0 |
| `rogner pour remplir` | Par défaut, l'image est letterboxée lorsque le rapport hauteur/largeur de sortie diffère. Activer pour recadrer l'image afin de remplir les dimensions de sortie (par défaut : False). | BOOLEAN | Non | - |
| `largeur de sortie` | Une valeur de zéro signifie que le calcul est automatique (généralement la taille d'origine ou output_height si spécifiée) (par défaut : 0). | INT | Non | 0 - 32000 |
| `hauteur de sortie` | Une valeur de zéro signifie que la hauteur de sortie est la même que celle d'origine ou que la largeur de sortie (par défaut : 0). | INT | Non | 0 - 32000 |
| `créativité` | Contrôle le niveau de créativité global de l'amélioration (par défaut : 3). | INT | Non | 1 - 9 |
| `préservation du visage` | Préserver l'identité faciale des sujets (par défaut : True). | BOOLEAN | Non | - |
| `préservation des couleurs` | Préserver les couleurs d'origine (par défaut : True). | BOOLEAN | Non | - |

**Remarque :** Ce nœud ne peut traiter qu'une seule image en entrée. Fournir un lot de plusieurs images entraînera une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image de sortie améliorée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/fr.md)

---
**Source fingerprint (SHA-256):** `1a0e708cdea9ec4f92f7f3aaabbdeea06a8fdab2f91a45ad2dea15f2bc2e8fa3`
