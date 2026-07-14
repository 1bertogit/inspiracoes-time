import json, sys, os
url, titulo, stamp, nota, tags, slug = sys.argv[1:7]
taglist = [t.strip() for t in tags.split(',') if t.strip()] or ["sem-tag"]
meta = {
    "id": slug + "_" + stamp,
    "url": url,
    "titulo": titulo,
    "data": stamp,
    "autor": os.environ.get("USER", ""),
    "nota": nota,
    "tags": taglist,
    "artefatos": {
        "site": "site/",
        "editavel": "editavel.html",
        "screenshot": "screenshot.png" if os.path.exists("screenshot.png") else None,
        "conteudo": "conteudo.md" if os.path.exists("conteudo.md") else None,
    },
}
json.dump(meta, open("meta.json", "w"), ensure_ascii=False, indent=2)
print("==> meta.json OK")
