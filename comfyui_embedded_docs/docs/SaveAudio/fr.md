> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudio/fr.md)

Le nœud SaveAudio enregistre des données audio dans un fichier au format FLAC. Il prend une entrée audio et l'écrit dans le répertoire de sortie spécifié avec le préfixe de nom de fichier donné. Le nœud gère automatiquement la dénomination des fichiers et garantit que l'audio est correctement sauvegardé pour une utilisation ultérieure.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `audio` | AUDIO | Oui | - | Les données audio à sauvegarder |
| `préfixe_du_nom_de_fichier` | STRING | Non | - | Le préfixe pour le nom du fichier de sortie (par défaut : "audio/ComfyUI") |

*Remarque : Les paramètres `prompt` et `extra_pnginfo` sont masqués et gérés automatiquement par le système.*

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| *Aucun* | - | Ce nœud ne renvoie aucune donnée de sortie mais enregistre le fichier audio dans le répertoire de sortie |

---
**Source fingerprint (SHA-256):** `16242dfc45d0f2808a5615e9c1bfe4de4d19e2f5f6b28370f631439021dc72e5`
