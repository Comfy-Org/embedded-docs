# GuideBasique

Le nœud BasicGuider crée un mécanisme de guidage simple pour le processus d'échantillonnage. Il prend un modèle et des données de conditionnement en entrées et produit un objet guider qui peut être utilisé pour guider le processus de génération pendant l'échantillonnage. Ce nœud fournit la fonctionnalité de guidage fondamentale nécessaire à la génération contrôlée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle à utiliser pour le guidage | MODEL | Oui | - |
| `conditioning` | Les données de conditionnement qui guident le processus de génération | CONDITIONING | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `GUIDER` | Un objet guider qui peut être utilisé pendant le processus d'échantillonnage pour guider la génération | GUIDER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicGuider/fr.md)

---
**Source fingerprint (SHA-256):** `8ea6b56be58ae99baaf13a04c4fadbf8ad921801d8f2ce2aecce768cc34a3b20`
