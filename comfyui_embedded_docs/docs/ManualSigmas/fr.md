# Sigmas manuels

Le nœud ManualSigmas vous permet de définir manuellement une séquence personnalisée de niveaux de bruit (sigmas) pour le processus d'échantillonnage. Vous saisissez une liste de nombres sous forme de chaîne, et le nœud les convertit en un tenseur pouvant être utilisé par d'autres nœuds d'échantillonnage. Cela est utile pour tester ou créer des programmes de bruit spécifiques.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `sigmas` | Une chaîne contenant les valeurs sigma. Le nœud extrait tous les nombres de cette chaîne, y compris les décimales et les valeurs négatives. Par exemple, « 1, 0.5, 0.1 » ou « 1 0.5 0.1 ». Par défaut : « 1, 0.5 ». | STRING | Oui | Toute valeur numérique séparée par des virgules ou des espaces |

Remarque : Ce nœud est marqué comme expérimental.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sigmas` | Un tenseur contenant la séquence de valeurs sigma extraites de la chaîne d'entrée. | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ManualSigmas/fr.md)

---
**Source fingerprint (SHA-256):** `19d938ef0eac7343a3138393a039f63632b0763e3884636653c06b91b6f44ed6`
