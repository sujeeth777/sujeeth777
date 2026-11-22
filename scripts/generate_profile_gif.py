from PIL import Image, ImageDraw, ImageFont
import math

W,H=1000,1600
FONT="/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
BOLD="/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
def F(n,b=False): return ImageFont.truetype(BOLD if b else FONT,n)

G=(61,255,130); D=(28,145,74); M=(40,205,105); WHT=(180,255,205)
BG=(2,8,5); PANEL=(4,17,10); GRID=(8,45,23)
f11,f12,f14,f16=[F(x) for x in (11,12,14,16)]
f18=F(18,1); f22=F(22,1); f48=F(48,1)

projects=[
("AI-PHISHING-URL-DETECTOR","AI / SECURITY","Python | ML | FastAPI"),
("TINYGPT-100K","AI / SYSTEMS","PyTorch | CUDA | LLM"),
("PRELIGHT","INFRA / AI","NVIDIA | Safety | Python"),
("AI-DRIVEN-PQC","CRYPTOGRAPHY","Post-Quantum | Python"),
("FARMHUB","FULL STACK","React | Node | MongoDB"),
("SUJEETH-TRADING-AI","FINTECH / AI","Python | Analytics")]

def box(d,b,r=14,fill=PANEL,outline=D,width=2):
    d.rounded_rectangle(b,radius=r,fill=fill,outline=outline,width=width)

def glow(d,x,y,s,ft):
    d.text((x+2,y+2),s,font=ft,fill=(3,30,15))
    d.text((x,y),s,font=ft,fill=G)

frames=[]
for k in range(12):
    im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
    for x in range(0,W,40): d.line((x,0,x,H),fill=GRID,width=1)
    for y in range(0,H,40): d.line((0,y,W,y),fill=GRID,width=1)
    scan=(k*125)%H; d.rectangle((0,scan,W,scan+3),fill=(20,100,50))

    box(d,(35,25,965,82),12,fill=(3,14,8))
    for xx,c in ((55,G),(75,(100,190,100)),(95,(40,100,60))):
        d.ellipse((xx,44,xx+10,54),fill=c)
    d.text((125,41),"sujeeth@profile-os:~$",font=f14,fill=WHT)
    d.text((337,41),"./boot"+("_" if k%2==0 else " "),font=f14,fill=G)
    d.text((825,41),f"FRAME {k+1:02d}/12",font=f12,fill=D)

    d.text((60,115),"> INITIALIZING IDENTITY CORE",font=f14,fill=M)
    glow(d,58,150,"SRI SUJEETH",f48)
    d.text((60,208),"COMPUTER SCIENCE | AI | CYBERSECURITY | NETWORKING",font=f16,fill=WHT)
    d.text((60,244),"BUILDING SYSTEMS THAT LOOK LIKE THEY SHOULD NOT EXIST YET.",font=f14,fill=D)

    cx,cy=500,390
    for aa in range(0,360,45):
        ang=math.radians(aa+k*12); pts=[]
        for t in range(0,361,12):
            q=math.radians(t)
            pts.append((cx+180*math.cos(q)*math.cos(ang)-55*math.sin(q)*math.sin(ang),
                        cy+180*math.cos(q)*math.sin(ang)+55*math.sin(q)*math.cos(ang)))
        d.line(pts,fill=D,width=2)
    d.ellipse((445,335,555,445),outline=G,width=3)
    d.ellipse((465,355,535,425),outline=M,width=2)
    for j in range(6):
        a=math.radians(k*30+j*60); x=cx+155*math.cos(a); y=cy+45*math.sin(a)
        d.ellipse((x-6,y-6,x+6,y+6),fill=G)
    glow(d,478,373,"CORE",f18); d.text((451,430),"ONLINE / SECURE",font=f12,fill=WHT)

    box(d,(45,490,955,680)); d.text((70,515),"$ whoami",font=f18,fill=G)
    d.text((70,550),"Sri Sujeeth Sirivella",font=f22,fill=WHT)
    d.text((70,585),"B.Tech CSE | Karunya Institute of Technology and Sciences | 2028",font=f14,fill=M)
    d.text((70,615),"FOCUS:",font=f12,fill=D)
    d.text((145,612),"AI | CYBERSECURITY | NETWORKING | POST-QUANTUM CRYPTOGRAPHY",font=f12,fill=WHT)

    box(d,(45,705,955,845)); d.text((70,730),"$ system --stack",font=f18,fill=G)
    cols=[("LANGUAGES","Python | JavaScript | HTML/CSS"),("AI / ML","PyTorch | scikit-learn | LLM"),("SECURITY","PQC | Web Security | Network Security")]
    for i,(title,items) in enumerate(cols):
        x=70+i*295
        d.text((x,765),title,font=f12,fill=D); d.text((x,790),items,font=f12,fill=WHT)

    d.text((55,890),"$ ls ./projects --featured",font=f18,fill=G)
    for i,(name,cat,tech) in enumerate(projects):
        col,row=i%2,i//2; x=45+col*465; y=930+row*135
        box(d,(x,y,x+435,y+115),10,fill=(3,15,9),outline=(18,100,50))
        d.rectangle((x+15,y+15,x+18,y+100),fill=G)
        d.text((x+32,y+14),name,font=f14,fill=WHT)
        d.text((x+32,y+43),cat,font=f12,fill=M)
        d.text((x+32,y+68),tech,font=f11,fill=D)
        d.rectangle((x+32,y+93,x+390,y+97),fill=(10,55,28))
        p=(k*9+i*37)%100
        d.rectangle((x+32,y+93,x+32+3.58*p,y+97),fill=G)

    box(d,(45,1355,610,1555)); d.text((70,1380),"$ netstat --visual",font=f18,fill=G)
    nodes=[(105,1460),(260,1425),(420,1480),(540,1425)]
    for i,(x,y) in enumerate(nodes):
        d.ellipse((x-16,y-16,x+16,y+16),outline=G,width=2)
        d.text((x-7,y-8),str(i+1),font=f12,fill=WHT)
        if i<len(nodes)-1: d.line((x+16,y,nodes[i+1][0]-16,nodes[i+1][1]),fill=M,width=2)
    a=k/11; x=105+435*a; y=1460-35*a
    d.ellipse((x-5,y-5,x+5,y+5),fill=G)
    d.text((70,1515),"PACKET FLOW | ENCRYPTED | STABLE",font=f11,fill=D)

    box(d,(630,1355,955,1555)); d.text((655,1380),"$ connect --open",font=f18,fill=G)
    d.text((655,1420),"github.com/sujeeth777",font=f12,fill=WHT)
    d.text((655,1450),"linkedin / sri-sujeeth-213593302",font=f11,fill=M)
    d.text((655,1480),"credly / sri-sujeeth-sirivella",font=f11,fill=M)
    d.text((655,1520),"SESSION: ACTIVE",font=f12,fill=G)
    frames.append(im)

frames[0].save("assets/profile-os.gif",save_all=True,append_images=frames[1:],duration=180,loop=0,optimize=True)
