# ByteDance Seed

Voici la traduction de la documentation technique du nœud ComfyUI, en respectant les règles établies :

## Aperçu

Générer des réponses textuelles à l'aide des modèles Seed 2.0 de ByteDance. Fournissez une invite textuelle et incluez éventuellement des images ou des vidéos pour un contexte multimodal.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `invite` | Texte d'entrée pour le modèle. | STRING | Oui | N/A |
| `modèle` | Le modèle Seed utilisé pour générer la réponse. | COMBO | Oui | `"Seed 2.0 Pro"`<br>`"Seed 2.0 Lite"`<br>`"Seed 2.0 Mini"` |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats ne sont pas déterministes, quelle que soit la graine. (valeur par défaut : 0) | INT | Oui | 0 à 2147483647 |
| `invite système` | Instructions fondamentales qui dictent le comportement du modèle. (valeur par défaut : "") | STRING | Non | N/A |

**Remarque sur le paramètre `model :** Le paramètre `model` est une liste déroulante dynamique qui accepte également des images et des vidéos. Vous pouvez connecter des entrées d'images et de vidéos à ce paramètre pour fournir un contexte multimodal. Un maximum de 20 images et 4 vidéos est pris en charge par requête.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La réponse textuelle générée par le modèle Seed. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedNode/fr.md)

---
**Source fingerprint (SHA-256):** `d1ef73cf72e88216d40c0cf727f90c40cf783cecabe3be0e7530fe72dba6c172`
