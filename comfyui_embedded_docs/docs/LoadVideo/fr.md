# Charger une vidéo

Voici la traduction en français de la documentation du nœud Load Video, en respectant vos règles :

Le nœud Load Video charge des fichiers vidéo depuis le répertoire d'entrée et les rend disponibles pour le traitement dans le workflow. Il lit les fichiers vidéo depuis le dossier d'entrée désigné et les produit sous forme de données vidéo pouvant être connectées à d'autres nœuds de traitement vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `fichier` | Le fichier vidéo à charger depuis le répertoire d'entrée. La liste déroulante est dynamiquement remplie avec tous les fichiers vidéo trouvés dans le dossier d'entrée de ComfyUI. | STRING | Oui | Plusieurs options disponibles |

**Remarque :** Les options disponibles pour le paramètre `file` sont dynamiquement remplies à partir des fichiers vidéo présents dans le répertoire d'entrée. Seuls les fichiers vidéo avec des types de contenu pris en charge sont affichés. Vous pouvez également télécharger un nouveau fichier vidéo directement via l'interface de sélection de fichiers du nœud.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video` | Les données vidéo chargées qui peuvent être transmises à d'autres nœuds de traitement vidéo pour une manipulation ou une analyse ultérieure. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideo/fr.md)

---
**Source fingerprint (SHA-256):** `e3d18eb43cba34734761b5b147d9fee91fe3ca99db21f9e19a130efc3349cecb`
