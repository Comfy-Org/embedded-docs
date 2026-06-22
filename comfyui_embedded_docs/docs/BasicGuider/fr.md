# GuideBasique

Le nœud BasicGuider crée un mécanisme de guidage simple pour le processus d'échantillonnage. Il prend un modèle et des données de conditionnement en entrée et produit un objet guideur pouvant être utilisé pour orienter le processus de génération pendant l'échantillonnage. Ce nœud fournit la fonctionnalité de guidage fondamentale nécessaire à une génération contrôlée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle à utiliser pour le guidage | MODEL | Oui | - |
| `conditionnement` | Les données de conditionnement qui orientent le processus de génération | CONDITIONING | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `GUIDER` | Un objet guideur pouvant être utilisé pendant le processus d'échantillonnage pour orienter la génération | GUIDER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicGuider/fr.md)

---
**Source fingerprint (SHA-256):** `012171caea6aacfadaabacb746be104ca783ae5ea5834cc4a67088233b835654`
