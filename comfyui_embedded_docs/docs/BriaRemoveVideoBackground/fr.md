# Bria Remove Video Background

Ce nœud supprime l'arrière-plan d'une vidéo à l'aide du service Bria AI. Il traite la vidéo d'entrée et remplace l'arrière-plan d'origine par une couleur unie de votre choix. L'opération est effectuée via une API externe, et le résultat est renvoyé sous forme d'un nouveau fichier vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `video` | Le fichier vidéo d'entrée à partir duquel l'arrière-plan sera supprimé. | VIDEO | Oui | N/A |
| `background_color` | Couleur d'arrière-plan de la vidéo de sortie. | COMBO | Oui | `"Black"`<br>`"White"`<br>`"Gray"`<br>`"Red"`<br>`"Green"`<br>`"Blue"`<br>`"Yellow"`<br>`"Cyan"`<br>`"Magenta"`<br>`"Orange"` |
| `seed` | Le paramètre `seed` contrôle si le nœud doit s'exécuter à nouveau ; les résultats sont non déterministes quel que soit le seed. (par défaut : 0) | INT | Oui | 0 à 2147483647 |

**Remarque :** La vidéo d'entrée doit avoir une durée de 60 secondes ou moins.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | Le fichier vidéo traité avec l'arrière-plan supprimé et remplacé par la couleur sélectionnée. La vidéo de sortie est encodée en MP4 avec H.264. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveVideoBackground/fr.md)

---
**Source fingerprint (SHA-256):** `dbd6b7393f893be5a40322fc96b90bb3d5f1818bdda7b8109b28f48baac44d59`
