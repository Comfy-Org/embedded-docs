> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeImageLists/fr.md)

Le nœud **Fusionner les listes d'images** combine plusieurs listes d'images distinctes en une seule liste continue. Il fonctionne en prenant toutes les images de chaque entrée connectée et en les concaténant dans l'ordre de réception. Cela est utile pour organiser ou regrouper des images provenant de différentes sources en vue d'un traitement ultérieur.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `images` | IMAGE | Oui | - | Une liste d'images à fusionner. Cette entrée peut accepter plusieurs connexions, et chaque liste connectée sera concaténée dans la sortie finale. |

**Remarque :** Ce nœud est conçu pour recevoir plusieurs entrées. Vous pouvez connecter plusieurs listes d'images à la seule prise d'entrée `images`. Le nœud concaténera automatiquement toutes les images de toutes les listes connectées en une seule liste de sortie.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `images` | IMAGE | La liste unique et fusionnée contenant toutes les images de chaque liste d'entrée connectée. |

---
**Source fingerprint (SHA-256):** `8fc53091b817a5036aae022aa841ba11fae0ed3242a969f5ae9072f48e061366`
