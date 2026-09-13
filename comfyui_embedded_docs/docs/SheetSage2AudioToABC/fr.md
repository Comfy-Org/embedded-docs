# SheetSage2 Audio vers ABC

Ce nœud transcrit les mélodies vocales et instrumentales d'une musique en notation ABC, un format textuel permettant d'écrire des partitions musicales. Il analyse l'audio connecté et renvoie la notation résultante sous forme de texte, qui peut ensuite être transmise au nœud YuE2 Generate Music en utilisant le mode correspondant.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `audio_encoder` | Le modèle d'encodeur audio utilisé pour analyser l'audio et produire la notation ABC. | AUDIO_ENCODER | Oui | - |
| `audio` | L'audio musical à transcrire en notation ABC. | AUDIO | Oui | - |
| `mode` | Contrôle ce qui est transcrit. "full" génère la mélodie et les accords ; "melody" génère uniquement la mélodie, recommandé pour les reprises. | COMBO | Oui | `"melody"`<br>`"full"` |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `abc` | La musique transcrite en notation ABC, renvoyée sous forme de liste de chaînes de caractères. Connectez-la au nœud YuE2 Generate Music et utilisez le mode correspondant. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SheetSage2AudioToABC/fr.md)

---
**Source fingerprint (SHA-256):** `612d18dedd09b64210087c340b8f304ace8cd7b30b1a6e8e8ba7c749b355a497`
