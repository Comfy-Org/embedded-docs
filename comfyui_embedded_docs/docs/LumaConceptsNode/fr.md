# Luma Concepts

Ce document a été généré par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaConceptsNode/en.md)

Contient un ou plusieurs concepts de caméra destinés aux nœuds Luma Texte vers Vidéo et Luma Image vers Vidéo. Ce nœud vous permet de sélectionner jusqu'à quatre concepts de caméra et, éventuellement, de les combiner avec des chaînes de concepts existantes.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `concept1` | Première sélection de concept de caméra parmi les concepts Luma disponibles | STRING | Oui | Plusieurs options disponibles<br>Inclut l'option "None" |
| `concept2` | Deuxième sélection de concept de caméra parmi les concepts Luma disponibles | STRING | Oui | Plusieurs options disponibles<br>Inclut l'option "None" |
| `concept3` | Troisième sélection de concept de caméra parmi les concepts Luma disponibles | STRING | Oui | Plusieurs options disponibles<br>Inclut l'option "None" |
| `concept4` | Quatrième sélection de concept de caméra parmi les concepts Luma disponibles | STRING | Oui | Plusieurs options disponibles<br>Inclut l'option "None" |
| `luma_concepts` | Concepts de caméra optionnels à ajouter à ceux sélectionnés ici | LUMA_CONCEPTS | Non | N/A |

**Remarque :** Tous les paramètres de concept (`concept1` à `concept4`) peuvent être définis sur "None" si vous ne souhaitez pas utiliser les quatre emplacements de concept. Le nœud fusionnera tous les `luma_concepts` fournis avec les concepts sélectionnés pour créer une chaîne de concepts combinée.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `luma_concepts` | Chaîne de concepts de caméra combinée contenant tous les concepts sélectionnés | LUMA_CONCEPTS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaConceptsNode/fr.md)

---
**Source fingerprint (SHA-256):** `d0e334104884eadab86987f188dff079e11ee4a3de05d2537d88fa9d2a30534a`
