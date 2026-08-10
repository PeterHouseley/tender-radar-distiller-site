#!/usr/bin/env python3
"""Build deterministic visual assets for the Tender Radar Distiller static site."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "generated"
OUT.mkdir(parents=True, exist_ok=True)

triage_board = """<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1100 620\" role=\"img\" aria-labelledby=\"title desc\">
  <title id=\"title\">Tender triage intelligence board</title>
  <desc id=\"desc\">A procurement dossier board showing public notices moving through duplicate removal, fit scoring, evidence burden review and pursue or park decisions.</desc>
  <defs>
    <filter id=\"shadow\" x=\"-10%\" y=\"-10%\" width=\"120%\" height=\"130%\"><feDropShadow dx=\"0\" dy=\"18\" stdDeviation=\"14\" flood-color=\"#2b2118\" flood-opacity=\"0.22\"/></filter>
    <pattern id=\"paper\" width=\"42\" height=\"42\" patternUnits=\"userSpaceOnUse\"><path d=\"M42 0H0v42\" fill=\"none\" stroke=\"#2b2118\" stroke-opacity=\"0.06\"/></pattern>
  </defs>
  <rect width=\"1100\" height=\"620\" rx=\"18\" fill=\"#efe6d2\"/><rect width=\"1100\" height=\"620\" rx=\"18\" fill=\"url(#paper)\"/>
  <rect x=\"38\" y=\"34\" width=\"1024\" height=\"552\" rx=\"10\" fill=\"#fbf6ea\" stroke=\"#2b2118\" stroke-opacity=\"0.28\" filter=\"url(#shadow)\"/>
  <path d=\"M76 112H1024\" stroke=\"#2b2118\" stroke-width=\"3\"/>
  <text x=\"76\" y=\"82\" fill=\"#2b2118\" font-family=\"Courier New, monospace\" font-size=\"24\" font-weight=\"900\" letter-spacing=\"3\">WEEKLY OPPORTUNITY CONTROL BOARD</text>
  <text x=\"824\" y=\"82\" fill=\"#8e2a21\" font-family=\"Courier New, monospace\" font-size=\"18\" font-weight=\"900\">TRD / LIVE FILTER</text>
  <g font-family=\"Courier New, monospace\" font-size=\"17\" font-weight=\"900\" fill=\"#6e6254\"><text x=\"92\" y=\"154\">RAW NOTICES</text><text x=\"322\" y=\"154\">FIT SCORE</text><text x=\"552\" y=\"154\">EVIDENCE LOAD</text><text x=\"806\" y=\"154\">DECISION</text></g>
  <g stroke=\"#2b2118\" stroke-opacity=\"0.22\" stroke-width=\"2\"><path d=\"M258 174v334\"/><path d=\"M500 174v334\"/><path d=\"M752 174v334\"/></g>
  <g font-family=\"Aptos, Segoe UI, sans-serif\" font-size=\"19\" fill=\"#221d17\">
    <g transform=\"translate(82 190) rotate(-1.5)\"><rect width=\"154\" height=\"72\" fill=\"#f4ead8\" stroke=\"#cdbb9d\"/><text x=\"16\" y=\"30\" font-weight=\"800\">Portal feed</text><text x=\"16\" y=\"55\" fill=\"#6e6254\">104 notices</text></g>
    <g transform=\"translate(88 288) rotate(1.4)\"><rect width=\"154\" height=\"72\" fill=\"#f4ead8\" stroke=\"#cdbb9d\"/><text x=\"16\" y=\"30\" font-weight=\"800\">Duplicates</text><text x=\"16\" y=\"55\" fill=\"#8e2a21\">removed early</text></g>
    <g transform=\"translate(82 386) rotate(-.8)\"><rect width=\"154\" height=\"72\" fill=\"#f4ead8\" stroke=\"#cdbb9d\"/><text x=\"16\" y=\"30\" font-weight=\"800\">Frameworks</text><text x=\"16\" y=\"55\" fill=\"#6e6254\">trap checked</text></g>
    <g transform=\"translate(306 196)\"><circle cx=\"56\" cy=\"56\" r=\"54\" fill=\"#29563d\"/><text x=\"26\" y=\"65\" fill=\"#fff\" font-family=\"Georgia,serif\" font-size=\"42\" font-weight=\"900\">88</text><text x=\"122\" y=\"50\" font-weight=\"850\">keyword + buyer fit</text><text x=\"122\" y=\"78\" fill=\"#6e6254\">pursuit quality</text></g>
    <g transform=\"translate(306 342)\"><circle cx=\"56\" cy=\"56\" r=\"54\" fill=\"#a96e1f\"/><text x=\"26\" y=\"65\" fill=\"#fff\" font-family=\"Georgia,serif\" font-size=\"42\" font-weight=\"900\">72</text><text x=\"122\" y=\"50\" font-weight=\"850\">clarify buyer scope</text><text x=\"122\" y=\"78\" fill=\"#6e6254\">watchlist item</text></g>
    <g transform=\"translate(540 196)\"><rect width=\"174\" height=\"66\" fill=\"#221d17\"/><text x=\"18\" y=\"41\" fill=\"#fbf6ea\" font-weight=\"900\">LOW DRAG</text></g><g transform=\"translate(540 286)\"><rect width=\"174\" height=\"66\" fill=\"#b94d24\"/><text x=\"18\" y=\"41\" fill=\"#fff\" font-weight=\"900\">11 DAYS</text></g><g transform=\"translate(540 376)\"><rect width=\"174\" height=\"66\" fill=\"#8e2a21\"/><text x=\"18\" y=\"41\" fill=\"#fff\" font-weight=\"900\">HEAVY BID</text></g>
    <g transform=\"translate(800 188) rotate(-3)\"><rect width=\"186\" height=\"86\" fill=\"#29563d\"/><text x=\"26\" y=\"54\" fill=\"#fff\" font-family=\"Courier New,monospace\" font-weight=\"900\" font-size=\"25\">PURSUE</text></g><g transform=\"translate(812 314) rotate(2)\"><rect width=\"168\" height=\"78\" fill=\"#a96e1f\"/><text x=\"31\" y=\"50\" fill=\"#fff\" font-family=\"Courier New,monospace\" font-weight=\"900\" font-size=\"24\">PARK</text></g><g transform=\"translate(798 430) rotate(-1)\"><rect width=\"190\" height=\"78\" fill=\"#f4ead8\" stroke=\"#8e2a21\" stroke-width=\"3\"/><text x=\"36\" y=\"50\" fill=\"#8e2a21\" font-family=\"Courier New,monospace\" font-weight=\"900\" font-size=\"24\">IGNORE</text></g>
  </g>
  <g stroke=\"#b94d24\" stroke-width=\"4\" stroke-linecap=\"round\" stroke-dasharray=\"10 12\" fill=\"none\" opacity=\"0.68\"><path d=\"M238 225C276 224 274 246 304 248\"/><path d=\"M464 249C500 249 506 228 540 228\"/><path d=\"M714 228C754 226 758 229 800 230\"/><path d=\"M236 424C282 424 270 386 306 390\"/><path d=\"M466 390C510 386 504 410 540 410\"/><path d=\"M714 410C756 412 754 470 798 470\"/></g>
  <text x=\"76\" y=\"556\" fill=\"#6e6254\" font-family=\"Courier New, monospace\" font-size=\"17\" font-weight=\"900\" letter-spacing=\"2\">PUBLIC FEEDS → PRACTICAL SCORING → OPERATOR DECISION FILE</text>
</svg>"""

pursuit_file = """<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 980 640\" role=\"img\" aria-labelledby=\"title desc\">
  <title id=\"title\">Bid starter pursuit file stack</title>
  <desc id=\"desc\">A premium procurement dossier visual showing the optional bid starter pack: go no-go memo, evidence checklist, buyer questions and first response skeleton.</desc>
  <defs>
    <filter id=\"soft\" x=\"-20%\" y=\"-20%\" width=\"140%\" height=\"150%\"><feDropShadow dx=\"0\" dy=\"22\" stdDeviation=\"16\" flood-color=\"#2b2118\" flood-opacity=\"0.23\"/></filter>
    <pattern id=\"grid\" width=\"34\" height=\"34\" patternUnits=\"userSpaceOnUse\"><path d=\"M34 0H0v34\" fill=\"none\" stroke=\"#2b2118\" stroke-opacity=\"0.055\"/></pattern>
  </defs>
  <rect width=\"980\" height=\"640\" rx=\"26\" fill=\"#221d17\"/>
  <rect width=\"980\" height=\"640\" rx=\"26\" fill=\"url(#grid)\"/>
  <circle cx=\"790\" cy=\"112\" r=\"150\" fill=\"#b94d24\" opacity=\"0.2\"/>
  <circle cx=\"180\" cy=\"560\" r=\"180\" fill=\"#29563d\" opacity=\"0.22\"/>
  <text x=\"54\" y=\"74\" font-family=\"Courier New, monospace\" font-size=\"18\" font-weight=\"900\" letter-spacing=\"4\" fill=\"#efe6d2\">OPTIONAL BID-STARTER PACK</text>
  <text x=\"54\" y=\"118\" font-family=\"Georgia, serif\" font-size=\"50\" font-weight=\"900\" letter-spacing=\"-2\" fill=\"#fbf6ea\">From shortlist to pursuit file.</text>
  <g filter=\"url(#soft)\">
    <g transform=\"translate(118 178) rotate(-4)\"><rect width=\"305\" height=\"348\" fill=\"#efe6d2\" stroke=\"#cdbb9d\"/><rect x=\"22\" y=\"26\" width=\"132\" height=\"28\" fill=\"#8e2a21\"/><text x=\"32\" y=\"46\" font-family=\"Courier New, monospace\" font-size=\"13\" font-weight=\"900\" fill=\"#fff\">GO / NO-GO</text><path d=\"M22 88H276M22 124H252M22 160H270\" stroke=\"#2b2118\" stroke-opacity=\".42\" stroke-width=\"6\"/><circle cx=\"244\" cy=\"264\" r=\"43\" fill=\"#29563d\"/><text x=\"219\" y=\"274\" font-family=\"Georgia, serif\" font-size=\"30\" font-weight=\"900\" fill=\"#fff\">88</text></g>
    <g transform=\"translate(338 156) rotate(2)\"><rect width=\"326\" height=\"380\" fill=\"#fbf6ea\" stroke=\"#2b2118\" stroke-opacity=\".35\"/><rect width=\"326\" height=\"48\" fill=\"#b94d24\"/><text x=\"22\" y=\"31\" font-family=\"Courier New, monospace\" font-size=\"14\" font-weight=\"900\" letter-spacing=\"2\" fill=\"#fff\">EVIDENCE BURDEN</text><g font-family=\"Aptos, Segoe UI, sans-serif\" font-size=\"17\" font-weight=\"800\" fill=\"#221d17\"><text x=\"28\" y=\"96\">✓ Case studies to reuse</text><text x=\"28\" y=\"142\">✓ Policies to attach</text><text x=\"28\" y=\"188\">? Clarification question</text><text x=\"28\" y=\"234\">× Oversized requirement</text></g><path d=\"M28 288H298M28 322H230\" stroke=\"#cdbb9d\" stroke-width=\"8\"/></g>
    <g transform=\"translate(616 214) rotate(5)\"><rect width=\"254\" height=\"314\" fill=\"#f4ead8\" stroke=\"#cdbb9d\"/><text x=\"24\" y=\"46\" font-family=\"Courier New, monospace\" font-size=\"14\" font-weight=\"900\" fill=\"#6f2718\">FIRST RESPONSE</text><path d=\"M24 82H218M24 118H230M24 154H196M24 220H226M24 256H178\" stroke=\"#2b2118\" stroke-opacity=\".36\" stroke-width=\"7\"/><rect x=\"24\" y=\"176\" width=\"114\" height=\"28\" fill=\"#29563d\"/><text x=\"34\" y=\"196\" font-family=\"Courier New, monospace\" font-size=\"13\" font-weight=\"900\" fill=\"#fff\">BID ANGLE</text></g>
  </g>
  <g font-family=\"Courier New, monospace\" font-size=\"15\" font-weight=\"900\" fill=\"#efe6d2\"><text x=\"54\" y=\"592\" letter-spacing=\"2\">SHORTLISTED NOTICE → BID BURDEN → EVIDENCE MAP → STARTER RESPONSE</text></g>
</svg>"""

for name, svg in {
    "tender-triage-board.svg": triage_board,
    "pursuit-file-stack.svg": pursuit_file,
}.items():
    path = OUT / name
    path.write_text(svg, encoding="utf-8")
    print(path)
