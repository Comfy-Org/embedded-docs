# ClipSave

Le nœud `CLIPSave` enregistre un modèle d’encodeur de texte CLIP sur disque au format SafeTensors. Il est conçu pour les flux de travail avancés de fusion de modèles et sépare automatiquement le modèle CLIP en ses parties composantes (telles que CLIP-L, CLIP-G ou T5XXL) en fonction de la structure interne du modèle, en enregistrant chaque composant dans un fichier séparé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP à enregistrer. | CLIP | Oui | - |
| `filename_prefix` | Le chemin du préfixe et le nom de fichier pour les fichiers enregistrés. Le nœud ajoute un suffixe de composant (par ex., `_clip_l`, `_clip_g`) et un compteur pour créer des noms de fichiers uniques (défaut : `clip/ComfyUI`). | STRING | Oui | - |
| `prompt` | Les informations d’invite du workflow, enregistrées sous forme de métadonnées dans le fichier de sortie. Ce paramètre est masqué dans l’interface. | PROMPT | Non | - |
| `extra_pnginfo` | Métadonnées supplémentaires, enregistrées sous forme de paires clé-valeur dans le fichier de sortie. Ce paramètre est masqué dans l’interface. | EXTRA_PNGINFO | Non | - |

## Sorties

Ce nœud n’a pas de connexions de sortie. Il enregistre directement les fichiers traités dans le répertoire `ComfyUI/output/`. Les fichiers enregistrés incluent des métadonnées (le format est défini sur « pt », plus l’invite du workflow et toute information PNG supplémentaire), sauf si ComfyUI est démarré avec l’argument `--disable-metadata`.

### Détails des fichiers enregistrés

Le nœud analyse le dictionnaire d’état du modèle CLIP et enregistre des fichiers SafeTensors séparés pour chaque composant détecté. Le composant est identifié par le préfixe de ses clés de paramètres. Les préfixes suivants sont vérifiés :

- `clip_l.` (encodeur de texte CLIP-L)
- `clip_g.` (encodeur de texte CLIP-G)
- `clip_h.` (encodeur de texte CLIP-H)
- `t5xxl.` (encodeur de texte T5-XXL)
- `pile_t5xl.` (encodeur de texte Pile-T5-XL)
- `mt5xl.` (encodeur de texte mT5-XL)
- `umt5xxl.` (encodeur de texte UMT5-XXL)
- `t5base.` (encodeur de texte T5-Base)
- `gemma2_2b.` (encodeur de texte Gemma 2 2B)
- `llama.` (encodeur de texte LLaMA)
- `hydit_clip.` (encodeur de texte Hydit CLIP)
- Préfixe vide (autres composants CLIP)

Pour chaque composant détecté, le nœud crée un fichier nommé `{filename_prefix}_{counter:05}_.safetensors`, où le préfixe du composant est ajouté au préfixe du nom de fichier (par ex., `clip/ComfyUI_clip_l_00001_.safetensors`). Le préfixe `transformer.` est supprimé des clés de paramètres lors de l’enregistrement.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipSave/fr.md)

---
**Source fingerprint (SHA-256):** `4ab9171e4245b10f738f78bac8a5b564c0957dde352e207ec3f9865e4fac0cab`
