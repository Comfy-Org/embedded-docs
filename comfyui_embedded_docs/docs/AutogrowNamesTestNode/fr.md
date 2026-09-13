# AutogrowNamesTestNode

Ce nœud est un test pour la fonctionnalité d'entrée Autogrow. Il accepte un groupe dynamique d'entrées FLOAT, chacune avec un nom prédéfini, et combine leurs valeurs en une seule chaîne séparée par des virgules.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `autogrow` | Un groupe d'entrées dynamique. Vous pouvez ajouter plusieurs entrées FLOAT, chacune avec un nom prédéfini parmi la liste : « a », « b » ou « c ». Le nœud accepte toute combinaison de ces entrées nommées. | FLOAT | Oui | Emplacements nommés : `a`, `b`, `c` |

**Remarque :** L'entrée `autogrow` est dynamique. Les entrées FLOAT individuelles nommées « a », « b » et « c » peuvent être ajoutées ou supprimées selon les besoins. Toutes les valeurs fournies sont traitées par le nœud.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Une seule chaîne contenant les valeurs de toutes les entrées FLOAT fournies, réunies par des virgules. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/fr.md)

---
**Source fingerprint (SHA-256):** `dac384c9486ac645d0d292fc891603cbfa6d362baa0a1e939c43257bbc0b06a0`
