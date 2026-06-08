Voici la traduction de la documentation technique du nœud ComfyUI, en respectant vos règles de formatage et de terminologie.

---

## Aperçu

Ce nœud ajuste l'échelle de bruit utilisée lors de l'échantillonnage du modèle. Il permet de définir une valeur d'échelle de bruit spécifique, qui contrôle la quantité de bruit appliquée au processus d'échantillonnage du modèle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle auquel appliquer l'ajustement de l'échelle de bruit. | MODEL | Oui | - |
| `échelle_bruit` | Échelle de bruit d'entraînement absolue. Par exemple, pour HiDream-O1 : base : 8.0, dev : 7.5. (par défaut : 1.0) | FLOAT | Oui | 0.0 à 64.0 (pas : 0.01) |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `MODEL` | Le modèle modifié avec la nouvelle échelle de bruit appliquée. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelNoiseScale/fr.md)

---
**Source fingerprint (SHA-256):** `37b77a5d65fb872f45be8ffa4efb65037bc7459bb001babaaf6b526a9a735190`
