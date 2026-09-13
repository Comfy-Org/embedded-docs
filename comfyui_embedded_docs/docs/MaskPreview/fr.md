# MaskPreview

Le nœud MaskPreview affiche un aperçu visuel des données de masque directement dans l’interface ComfyUI, sans les enregistrer dans le répertoire de sortie. Cela vous permet d’inspecter le masque à n’importe quel point de votre flux de travail, tandis que le masque traverse également le nœud sans modification afin de pouvoir continuer à être utilisé en aval.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mask` | Les données de masque à prévisualiser | MASK | Oui | - |
| `filename_prefix` | Préfixe de nom de fichier utilisé pour l’aperçu (par défaut : « ComfyUI ») | STRING | Non | - |
| `prompt` | Informations de prompt pour les métadonnées (fournies automatiquement) | PROMPT | Non | - |
| `extra_pnginfo` | Informations PNG supplémentaires pour les métadonnées (fournies automatiquement) | EXTRA_PNGINFO | Non | - |

Seul `mask` est une entrée visible qui doit être connectée. Les paramètres `filename_prefix`, `prompt` et `extra_pnginfo` sont fournis par le système : `filename_prefix` revient à sa valeur par défaut, tandis que `prompt` et `extra_pnginfo` sont masqués et fournis automatiquement par l’environnement d’exécution ComfyUI.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `mask` | Les mêmes données de masque que celles prévisualisées, renvoyées sans modification afin de pouvoir être utilisées ailleurs dans le flux de travail | MASK |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/fr.md)

---
**Source fingerprint (SHA-256):** `fb7abe8cb6b5ac8a6a38e88ef90a146d16caf41d24c5de95309a94bc3c371d75`
