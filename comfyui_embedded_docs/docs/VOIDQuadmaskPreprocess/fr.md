# VOIDQuadmaskPreprocess

Voici la traduction de la documentation du nœud VOIDQuadmaskPreprocess :

## Aperçu

Le nœud VOIDQuadmaskPreprocess prépare un masque pour l'infilling VOID en le convertissant en un « quadrimasque » spécial à quatre niveaux. Il prend un masque d'entrée, dilate éventuellement la région principale, puis quantifie les valeurs du masque en quatre niveaux distincts représentant différentes zones sémantiques (objet principal, chevauchement, zone affectée et arrière-plan). Enfin, il inverse et normalise le masque afin que les valeurs de sortie soient comprises dans l'intervalle [0, 1], où 1,0 indique la zone à supprimer et 0,0 la zone à conserver.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `mask` | Le masque d'entrée à prétraiter. | MASK | Oui | N/D |
| `dilate_width` | Rayon de dilatation pour la région du masque principal. Une valeur de 0 signifie qu'aucune dilatation n'est appliquée. (par défaut : 0) | INT | Non | 0 à 50 (pas : 1) |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `quadmask` | Le quadrimasque prétraité avec des valeurs comprises dans [0, 1], représentant quatre niveaux discrets : 1,0 (objet principal à supprimer), ~0,75 (chevauchennent entre l'objet principal et la zone affectée), ~0,50 (zone affectée) et 0,0 (arrière-plan à conserver). | MASK |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDQuadmaskPreprocess/fr.md)

---
**Source fingerprint (SHA-256):** `12dc5ab215b80d81289942457ce2ddffcb9ec41fc738a53ca5fbf1e9181ed439`
