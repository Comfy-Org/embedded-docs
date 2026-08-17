# CLIPSave

Le nœud `CLIPSave` enregistre un modèle d'encodeur de texte CLIP sur le disque au format SafeTensors. Il est conçu pour les workflows avancés de fusion de modèles et sépare automatiquement le modèle CLIP en ses composants (tels que CLIP-L, CLIP-G ou T5XXL) en fonction de la structure interne du modèle, enregistrant chaque composant dans un fichier distinct.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP à enregistrer. | CLIP | Oui | - |
| `filename_prefix` | Le chemin de préfixe et le nom de fichier pour le(s) fichier(s) enregistré(s). Le nœud ajoute un suffixe de composant (par exemple `_clip_l`, `_clip_g`) et un compteur pour créer des noms de fichiers uniques (défaut : `clip/ComfyUI`). | STRING | Oui | - |
| `prompt` | Les informations du prompt du workflow, enregistrées comme métadonnées dans le fichier de sortie. Ce paramètre est masqué dans l'interface. | PROMPT | Non | - |
| `extra_pnginfo` | Métadonnées supplémentaires, enregistrées sous forme de paires clé-valeur dans le fichier de sortie. Ce paramètre est masqué dans l'interface. | EXTRA_PNGINFO | Non | - |

## Sorties

Ce nœud n'a aucune connexion de sortie. Il enregistre directement les fichiers traités dans le répertoire `ComfyUI/output/`.

### Détails des fichiers enregistrés

Le nœud analyse le dictionnaire d'état du modèle CLIP et enregistre des fichiers SafeTensors distincts pour chaque composant détecté. Le composant est identifié par le préfixe de ses clés de paramètres. Le nœud vérifie les préfixes suivants, dans l'ordre :

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

Pour chaque composant détecté, le nœud crée un fichier nommé `{filename}_{counter:05}_.safetensors` (par exemple, `ComfyUI_clip_l_00001_.safetensors`), où le nom du composant est ajouté au préfixe du nom de fichier et le compteur garantit des noms de fichiers uniques. Lorsqu'un composant est enregistré, le préfixe `transformer.` est supprimé de ses clés de paramètres.

Les métadonnées écrites dans chaque fichier incluent le prompt du workflow et toutes les informations PNG supplémentaires, à moins que l'enregistrement des métadonnées ne soit désactivé avec l'argument de ligne de commande `--disable-metadata`.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSave/fr.md)

---
**Source fingerprint (SHA-256):** `4ab9171e4245b10f738f78bac8a5b564c0957dde352e207ec3f9865e4fac0cab`
