# Sonilo Music 1.5

Le nœud Sonilo Music 1.5 génère une chanson complète avec des voix chantées à partir d'un prompt textuel. Décrivez le genre, l'ambiance, les instruments et les voix, et fournissez éventuellement vos propres paroles ; le nœud envoie la requête au service Sonilo et renvoie la piste finalisée sous forme d'audio. Utilisez-le lorsque vous avez besoin d'une chanson complète plutôt que d'un extrait instrumental.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Description de la chanson : genre, ambiance, instruments et voix. Pour définir vous-même les paroles, ajoutez un bloc `Lyrics:` avec les balises `[Verse]` et `[Chorus]` ; sans cela, le modèle écrit ses propres paroles. Doit contenir de 1 à 2000 caractères après suppression des espaces. | STRING | Oui | 1 à 2000 caractères |
| `duration` | `auto` adapte la longueur de la chanson aux paroles. `custom` utilise la valeur de `seconds`, en coupant les paroles qui ne tiennent pas et en répétant les paroles trop courtes. | DYNAMIC_COMBO | Oui | `"auto"`<br>`"custom"` |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine (par défaut : 42). | INT | Oui | 0 à 18446744073709551615 |

### Paramètres de durée personnalisée (lorsque `duration` est `"custom"`)

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `seconds` | Durée de la chanson générée en secondes (par défaut : 60). | INT | Oui | 10 à 360 |

**Remarque :** L'entrée `prompt` est obligatoire et ne doit pas être vide. Le nœud vérifie qu'elle contient au moins 1 caractère après suppression des espaces et pas plus de 2000.

**Remarque :** L'utilisation est facturée à 0,0032175 $ par seconde de la durée demandée, et l'indicateur de prix suit `duration.seconds` lorsque `custom` est sélectionné.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `audio` | La chanson générée, y compris les parties vocales, sous forme de fichier audio. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloMusic15/fr.md)

---
**Source fingerprint (SHA-256):** `65ccf74ccdfa7a710d8c7bd9871e666d79ceadc7304644fe0101956832ca6024`
