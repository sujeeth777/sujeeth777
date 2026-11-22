import json, os, urllib.request
from xml.sax.saxutils import escape

TOKEN=os.environ.get("GITHUB_TOKEN")
USER="sujeeth777"
headers={"Accept":"application/vnd.github+json","User-Agent":"sujeeth-profile-sync"}
if TOKEN:
    headers["Authorization"]=f"Bearer {TOKEN}"

def get(url):
    req=urllib.request.Request(url,headers=headers)
    with urllib.request.urlopen(req,timeout=20) as r:
        return json.load(r)

profile=get(f"https://api.github.com/users/{USER}")
repos=get(f"https://api.github.com/users/{USER}/repos?per_page=100&type=owner&sort=updated")
public=[r for r in repos if not r.get("private") and not r.get("fork")]
stars=sum(r.get("stargazers_count",0) for r in public)
followers=profile.get("followers",0)
events=get(f"https://api.github.com/users/{USER}/events/public?per_page=100")
recent=len(events)

def cell(x,y,label,value,w=215):
    return f'<rect x="{x}" y="60" width="{w}" height="92" rx="12" fill="#06130b" stroke="#0c8c4d"/><text x="{x+20}" y="88" fill="#4cff9a" font-family="monospace" font-size="12">{escape(label)}</text><text x="{x+20}" y="125" fill="#e0ffe9" font-family="monospace" font-size="28">{escape(str(value))}</text>'

svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 190" role="img" aria-label="Live GitHub telemetry">
<rect width="1000" height="190" rx="18" fill="#020604"/>
<rect x="1" y="1" width="998" height="188" rx="18" fill="none" stroke="#00ff88" stroke-opacity=".45"/>
<text x="30" y="38" fill="#00ff88" font-family="monospace" font-size="18" font-weight="700">$ github --telemetry</text>
<circle cx="245" cy="32" r="6" fill="#00ff88"><animate attributeName="opacity" values="1;.25;1" dur="1.4s" repeatCount="indefinite"/></circle>
<text x="265" y="38" fill="#7dffb2" font-family="monospace" font-size="12">AUTO-SYNCED BY GITHUB ACTIONS</text>
{cell(30,0,"PUBLIC REPOS",len(public))}
{cell(265,0,"TOTAL STARS",stars)}
{cell(500,0,"FOLLOWERS",followers)}
<rect x="735" y="60" width="235" height="92" rx="12" fill="#06130b" stroke="#0c8c4d"/>
<text x="755" y="88" fill="#4cff9a" font-family="monospace" font-size="12">RECENT EVENTS</text>
<text x="755" y="125" fill="#e0ffe9" font-family="monospace" font-size="28">{recent}</text>
</svg>'''
os.makedirs("assets",exist_ok=True)
with open("assets/github-telemetry.svg","w",encoding="utf-8") as f:
    f.write(svg)
