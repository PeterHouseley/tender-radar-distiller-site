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

deadline_corridor = """<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1120 680\" role=\"img\" aria-labelledby=\"title desc\">
  <title id=\"title\">Tender deadline corridor</title>
  <desc id=\"desc\">A public procurement deadline corridor showing four live notices moving through clarification, evidence pack, approval and submission gates.</desc>
  <defs>
    <filter id=\"pinshadow\" x=\"-20%\" y=\"-20%\" width=\"140%\" height=\"150%\"><feDropShadow dx=\"0\" dy=\"18\" stdDeviation=\"14\" flood-color=\"#2b2118\" flood-opacity=\"0.24\"/></filter>
    <pattern id=\"corridorGrid\" width=\"44\" height=\"44\" patternUnits=\"userSpaceOnUse\"><path d=\"M44 0H0v44\" fill=\"none\" stroke=\"#fbf6ea\" stroke-opacity=\"0.075\"/></pattern>
  </defs>
  <rect width=\"1120\" height=\"680\" rx=\"22\" fill=\"#251f18\"/>
  <rect width=\"1120\" height=\"680\" rx=\"22\" fill=\"url(#corridorGrid)\"/>
  <path d=\"M92 156H1028M92 286H1028M92 416H1028M92 546H1028\" stroke=\"#fbf6ea\" stroke-opacity=\"0.16\" stroke-width=\"2\"/>
  <g font-family=\"Courier New, monospace\" font-size=\"16\" font-weight=\"900\" letter-spacing=\"2\" fill=\"#efe6d2\"><text x=\"86\" y=\"82\">DEADLINE CORRIDOR / LIVE PROCUREMENT PURSUIT WINDOW</text><text x=\"776\" y=\"82\" fill=\"#ddb36b\">WEEK 33 SAMPLE</text></g>
  <g font-family=\"Courier New, monospace\" font-size=\"14\" font-weight=\"900\" fill=\"#cdbb9d\"><text x=\"108\" y=\"124\">NOTICE FOUND</text><text x=\"340\" y=\"124\">CLARIFY</text><text x=\"548\" y=\"124\">EVIDENCE</text><text x=\"760\" y=\"124\">APPROVAL</text><text x=\"948\" y=\"124\">SUBMIT</text></g>
  <g stroke=\"#b94d24\" stroke-width=\"4\" stroke-dasharray=\"10 12\" stroke-linecap=\"round\"><path d=\"M170 156C282 156 300 156 388 156S518 156 606 156S736 156 836 156S948 156 992 156\"/><path d=\"M170 286C250 286 280 294 360 292S482 268 574 268S720 300 808 300S914 286 970 286\" opacity=\".7\"/><path d=\"M170 416C246 416 300 430 374 430S502 412 610 412S750 456 840 456\" opacity=\".52\"/><path d=\"M170 546C248 546 288 520 372 520S500 552 586 552S710 546 774 546\" opacity=\".38\"/></g>
  <g filter=\"url(#pinshadow)\" font-family=\"Aptos, Segoe UI, sans-serif\" fill=\"#221d17\">
    <g transform=\"translate(104 174) rotate(-1.5)\"><rect width=\"292\" height=\"82\" rx=\"4\" fill=\"#fbf6ea\"/><rect width=\"12\" height=\"82\" fill=\"#29563d\"/><text x=\"28\" y=\"31\" font-size=\"18\" font-weight=\"900\">Facilities maintenance framework</text><text x=\"28\" y=\"58\" font-size=\"14\" font-weight=\"800\" fill=\"#6e6254\">11 days · fit 84 · pursue now</text></g>
    <g transform=\"translate(306 304) rotate(1.2)\"><rect width=\"286\" height=\"82\" rx=\"4\" fill=\"#fbf6ea\"/><rect width=\"12\" height=\"82\" fill=\"#a96e1f\"/><text x=\"28\" y=\"31\" font-size=\"18\" font-weight=\"900\">Retrofit support call-off</text><text x=\"28\" y=\"58\" font-size=\"14\" font-weight=\"800\" fill=\"#6e6254\">clarification first · park 48h</text></g>
    <g transform=\"translate(520 434) rotate(-.8)\"><rect width=\"292\" height=\"82\" rx=\"4\" fill=\"#fbf6ea\"/><rect width=\"12\" height=\"82\" fill=\"#8e2a21\"/><text x=\"28\" y=\"31\" font-size=\"18\" font-weight=\"900\">National multi-lot supply</text><text x=\"28\" y=\"58\" font-size=\"14\" font-weight=\"800\" fill=\"#6e6254\">evidence heavy · no-bid filed</text></g>
    <g transform=\"translate(716 548) rotate(1.4)\"><rect width=\"294\" height=\"82\" rx=\"4\" fill=\"#fbf6ea\"/><rect width=\"12\" height=\"82\" fill=\"#29563d\"/><text x=\"28\" y=\"31\" font-size=\"18\" font-weight=\"900\">Content migration brief</text><text x=\"28\" y=\"58\" font-size=\"14\" font-weight=\"800\" fill=\"#6e6254\">approval ready · skeleton drafted</text></g>
  </g>
  <g font-family=\"Courier New, monospace\" font-weight=\"900\" text-anchor=\"middle\"><g transform=\"translate(980 184) rotate(-8)\"><circle r=\"58\" fill=\"none\" stroke=\"#7db58d\" stroke-width=\"5\"/><text y=\"-6\" font-size=\"15\" fill=\"#7db58d\">BID</text><text y=\"20\" font-size=\"22\" fill=\"#7db58d\">READY</text></g><g transform=\"translate(896 440) rotate(9)\"><circle r=\"52\" fill=\"none\" stroke=\"#e68a78\" stroke-width=\"5\"/><text y=\"-4\" font-size=\"14\" fill=\"#e68a78\">NO-BID</text><text y=\"18\" font-size=\"18\" fill=\"#e68a78\">SAVED</text></g></g>
  <text x=\"86\" y=\"632\" font-family=\"Courier New, monospace\" font-size=\"16\" font-weight=\"900\" letter-spacing=\"2\" fill=\"#cdbb9d\">THE SERVICE SELLS CALENDAR CONTROL: WHAT TO CHASE, WHAT TO QUERY, WHAT TO DROP BEFORE THE WEEK DISAPPEARS.</text>
</svg>"""


economics_ledger = """<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1120 660\" role=\"img\" aria-labelledby=\"title desc\">
  <title id=\"title\">Tender pursuit economics ledger</title>
  <desc id=\"desc\">A procurement intelligence ledger comparing portal searching, practical triage and bid-starter escalation for small suppliers.</desc>
  <defs>
    <filter id=\"drop\" x=\"-15%\" y=\"-15%\" width=\"130%\" height=\"140%\"><feDropShadow dx=\"0\" dy=\"20\" stdDeviation=\"16\" flood-color=\"#2b2118\" flood-opacity=\"0.2\"/></filter>
    <pattern id=\"ledger\" width=\"56\" height=\"38\" patternUnits=\"userSpaceOnUse\"><path d=\"M0 38H56M56 0V38\" fill=\"none\" stroke=\"#2b2118\" stroke-opacity=\"0.07\"/></pattern>
  </defs>
  <rect width=\"1120\" height=\"660\" rx=\"24\" fill=\"#efe6d2\"/>
  <rect width=\"1120\" height=\"660\" rx=\"24\" fill=\"url(#ledger)\"/>
  <rect x=\"44\" y=\"38\" width=\"1032\" height=\"584\" rx=\"12\" fill=\"#fbf6ea\" stroke=\"#2b2118\" stroke-opacity=\"0.25\" filter=\"url(#drop)\"/>
  <text x=\"78\" y=\"88\" font-family=\"Courier New, monospace\" font-size=\"20\" font-weight=\"900\" letter-spacing=\"4\" fill=\"#6f2718\">SUPPLIER TIME LEDGER / WEEKLY PURSUIT ECONOMICS</text>
  <text x=\"78\" y=\"138\" font-family=\"Georgia, serif\" font-size=\"48\" font-weight=\"900\" letter-spacing=\"-2\" fill=\"#221d17\">The commercial case in one page.</text>
  <g font-family=\"Aptos, Segoe UI, sans-serif\" font-size=\"18\" fill=\"#221d17\">
    <g transform=\"translate(78 190)\"><rect width=\"286\" height=\"310\" fill=\"#f4ead8\" stroke=\"#cdbb9d\"/><rect width=\"286\" height=\"52\" fill=\"#8e2a21\"/><text x=\"22\" y=\"34\" font-family=\"Courier New, monospace\" font-size=\"15\" font-weight=\"900\" fill=\"#fff\">WITHOUT RADAR</text><text x=\"22\" y=\"104\" font-family=\"Georgia, serif\" font-size=\"68\" font-weight=\"900\" fill=\"#8e2a21\">6–8h</text><text x=\"22\" y=\"142\" font-weight=\"850\">lost to portal sifting</text><path d=\"M22 182H252M22 222H238M22 262H184\" stroke=\"#2b2118\" stroke-width=\"7\" stroke-opacity=\".28\"/><text x=\"22\" y=\"292\" font-family=\"Courier New, monospace\" font-size=\"14\" font-weight=\"900\" fill=\"#6e6254\">false starts, expired lots, giant frameworks</text></g>
    <g transform=\"translate(416 168)\"><rect width=\"286\" height=\"354\" fill=\"#221d17\"/><rect x=\"14\" y=\"14\" width=\"258\" height=\"326\" fill=\"none\" stroke=\"#efe6d2\" stroke-opacity=\".22\"/><text x=\"28\" y=\"54\" font-family=\"Courier New, monospace\" font-size=\"15\" font-weight=\"900\" fill=\"#efe6d2\">WEEKLY RADAR</text><text x=\"28\" y=\"126\" font-family=\"Georgia, serif\" font-size=\"78\" font-weight=\"900\" fill=\"#fbf6ea\">£79</text><text x=\"28\" y=\"166\" font-weight=\"850\" fill=\"#efe6d2\">one action shortlist</text><g font-family=\"Courier New, monospace\" font-size=\"14\" font-weight=\"900\"><text x=\"28\" y=\"222\" fill=\"#7db58d\">PURSUE: 1–3 realistic</text><text x=\"28\" y=\"260\" fill=\"#ddb36b\">PARK: watch / clarify</text><text x=\"28\" y=\"298\" fill=\"#e68a78\">IGNORE: save the week</text></g></g>
    <g transform=\"translate(754 190)\"><rect width=\"286\" height=\"310\" fill=\"#f4ead8\" stroke=\"#cdbb9d\"/><rect width=\"286\" height=\"52\" fill=\"#29563d\"/><text x=\"22\" y=\"34\" font-family=\"Courier New, monospace\" font-size=\"15\" font-weight=\"900\" fill=\"#fff\">WHEN IT IS WORTH IT</text><text x=\"22\" y=\"104\" font-family=\"Georgia, serif\" font-size=\"68\" font-weight=\"900\" fill=\"#29563d\">£250+</text><text x=\"22\" y=\"142\" font-weight=\"850\">bid-starter file</text><path d=\"M22 184H252M22 224H238M22 264H202\" stroke=\"#2b2118\" stroke-width=\"7\" stroke-opacity=\".28\"/><text x=\"22\" y=\"292\" font-family=\"Courier New, monospace\" font-size=\"14\" font-weight=\"900\" fill=\"#6e6254\">evidence map, buyer questions, first response</text></g>
  </g>
  <g stroke=\"#b94d24\" stroke-width=\"5\" stroke-linecap=\"round\" stroke-dasharray=\"12 12\" fill=\"none\"><path d=\"M364 336C392 336 390 336 416 336\"/><path d=\"M702 336C730 336 728 336 754 336\"/></g>
  <g transform=\"translate(762 70) rotate(7)\"><circle cx=\"98\" cy=\"98\" r=\"78\" fill=\"none\" stroke=\"#b94d24\" stroke-width=\"5\"/><text x=\"52\" y=\"88\" font-family=\"Courier New, monospace\" font-size=\"16\" font-weight=\"900\" fill=\"#b94d24\">NO BID</text><text x=\"45\" y=\"114\" font-family=\"Courier New, monospace\" font-size=\"16\" font-weight=\"900\" fill=\"#b94d24\">TIME TAX</text></g>
  <text x=\"78\" y=\"574\" font-family=\"Courier New, monospace\" font-size=\"17\" font-weight=\"900\" letter-spacing=\"2\" fill=\"#6e6254\">LOW-COMMITMENT RADAR → PAID PROOF → OPTIONAL PURSUIT SUPPORT</text>
</svg>"""

evidence_matrix = """<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1180 720\" role=\"img\" aria-labelledby=\"title desc\">
  <title id=\"title\">Tender evidence burden matrix</title>
  <desc id=\"desc\">An official procurement dossier-style matrix showing qualification evidence, case studies, policies and accreditations scored before a tender is pursued.</desc>
  <defs>
    <filter id=\"shadow\" x=\"-14%\" y=\"-14%\" width=\"128%\" height=\"136%\"><feDropShadow dx=\"0\" dy=\"22\" stdDeviation=\"18\" flood-color=\"#2b2118\" flood-opacity=\"0.24\"/></filter>
    <pattern id=\"ruled\" width=\"54\" height=\"38\" patternUnits=\"userSpaceOnUse\"><path d=\"M0 38H54M54 0V38\" fill=\"none\" stroke=\"#2b2118\" stroke-opacity=\"0.07\"/></pattern>
  </defs>
  <rect width=\"1180\" height=\"720\" rx=\"26\" fill=\"#efe6d2\"/><rect width=\"1180\" height=\"720\" rx=\"26\" fill=\"url(#ruled)\"/>
  <rect x=\"50\" y=\"44\" width=\"1080\" height=\"632\" rx=\"14\" fill=\"#fbf6ea\" stroke=\"#2b2118\" stroke-opacity=\"0.26\" filter=\"url(#shadow)\"/>
  <g font-family=\"Courier New, monospace\" font-weight=\"900\" letter-spacing=\"3\"><text x=\"84\" y=\"92\" font-size=\"18\" fill=\"#6f2718\">EVIDENCE BURDEN MATRIX / BID ROOM PRE-CHECK</text><text x=\"920\" y=\"92\" font-size=\"15\" fill=\"#8e2a21\">NO-BID TRIGGER VISIBLE</text></g>
  <text x=\"84\" y=\"146\" font-family=\"Georgia, serif\" font-size=\"52\" font-weight=\"900\" letter-spacing=\"-2\" fill=\"#221d17\">Do we have the proof before we burn the week?</text>
  <g transform=\"translate(84 196)\" font-family=\"Aptos, Segoe UI, sans-serif\" fill=\"#221d17\">
    <rect width=\"1012\" height=\"58\" fill=\"#221d17\"/><g fill=\"#fbf6ea\" font-family=\"Courier New, monospace\" font-size=\"15\" font-weight=\"900\"><text x=\"22\" y=\"37\">REQUIREMENT</text><text x=\"330\" y=\"37\">EVIDENCE ON FILE</text><text x=\"610\" y=\"37\">GAP</text><text x=\"820\" y=\"37\">DECISION</text></g>
    <g font-size=\"18\" font-weight=\"820\"><g transform=\"translate(0 76)\"><rect width=\"1012\" height=\"64\" fill=\"#f4ead8\" stroke=\"#cdbb9d\"/><rect width=\"10\" height=\"64\" fill=\"#29563d\"/><text x=\"22\" y=\"40\">3 comparable public-sector projects</text><text x=\"330\" y=\"40\">2 strong, 1 reusable adjacent</text><text x=\"610\" y=\"40\">light rewrite</text><text x=\"820\" y=\"40\" fill=\"#29563d\" font-family=\"Courier New, monospace\" font-weight=\"900\">PURSUE</text></g><g transform=\"translate(0 156)\"><rect width=\"1012\" height=\"64\" fill=\"#fbf6ea\" stroke=\"#cdbb9d\"/><rect width=\"10\" height=\"64\" fill=\"#a96e1f\"/><text x=\"22\" y=\"40\">Cyber, data and insurance policies</text><text x=\"330\" y=\"40\">policy names present</text><text x=\"610\" y=\"40\">expiry dates missing</text><text x=\"820\" y=\"40\" fill=\"#a96e1f\" font-family=\"Courier New, monospace\" font-weight=\"900\">CLARIFY</text></g><g transform=\"translate(0 236)\"><rect width=\"1012\" height=\"64\" fill=\"#f4ead8\" stroke=\"#cdbb9d\"/><rect width=\"10\" height=\"64\" fill=\"#8e2a21\"/><text x=\"22\" y=\"40\">ISO accreditation or named equivalent</text><text x=\"330\" y=\"40\">not evidenced</text><text x=\"610\" y=\"40\">mandatory wording</text><text x=\"820\" y=\"40\" fill=\"#8e2a21\" font-family=\"Courier New, monospace\" font-weight=\"900\">NO-BID RISK</text></g><g transform=\"translate(0 316)\"><rect width=\"1012\" height=\"64\" fill=\"#fbf6ea\" stroke=\"#cdbb9d\"/><rect width=\"10\" height=\"64\" fill=\"#29563d\"/><text x=\"22\" y=\"40\">Social value response</text><text x=\"330\" y=\"40\">local hiring notes ready</text><text x=\"610\" y=\"40\">tailor buyer area</text><text x=\"820\" y=\"40\" fill=\"#29563d\" font-family=\"Courier New, monospace\" font-weight=\"900\">DRAFT</text></g></g>
  </g>
  <g transform=\"translate(790 570) rotate(-6)\" font-family=\"Courier New, monospace\" font-weight=\"900\" text-anchor=\"middle\"><circle cx=\"105\" cy=\"54\" r=\"54\" fill=\"none\" stroke=\"#8e2a21\" stroke-width=\"5\"/><text x=\"105\" y=\"48\" fill=\"#8e2a21\" font-size=\"15\">EVIDENCE</text><text x=\"105\" y=\"72\" fill=\"#8e2a21\" font-size=\"19\">FIRST</text></g>
  <text x=\"84\" y=\"632\" font-family=\"Courier New, monospace\" font-size=\"16\" font-weight=\"900\" letter-spacing=\"2\" fill=\"#6e6254\">THE WEEKLY FILE NOW NAMES THE PROOF GAP BEFORE THE SUPPLIER COMMITS TO WRITING.</text>
</svg>"""

buyer_decision_annex = """<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1180 720\" role=\"img\" aria-labelledby=\"title desc\">
  <title id=\"title\">Buyer decision annex</title>
  <desc id=\"desc\">An official procurement decision annex showing the shortlist cover sheet, no-bid rationale and bid-starter trigger for a supplier tender review.</desc>
  <defs>
    <filter id=\"annexShadow\" x=\"-18%\" y=\"-18%\" width=\"136%\" height=\"145%\"><feDropShadow dx=\"0\" dy=\"24\" stdDeviation=\"18\" flood-color=\"#2b2118\" flood-opacity=\"0.24\"/></filter>
    <pattern id=\"annexGrid\" width=\"46\" height=\"46\" patternUnits=\"userSpaceOnUse\"><path d=\"M46 0H0v46\" fill=\"none\" stroke=\"#2b2118\" stroke-opacity=\"0.055\"/></pattern>
  </defs>
  <rect width=\"1180\" height=\"720\" rx=\"26\" fill=\"#efe6d2\"/>
  <rect width=\"1180\" height=\"720\" rx=\"26\" fill=\"url(#annexGrid)\"/>
  <rect x=\"54\" y=\"46\" width=\"1072\" height=\"628\" rx=\"14\" fill=\"#fbf6ea\" stroke=\"#2b2118\" stroke-opacity=\"0.28\" filter=\"url(#annexShadow)\"/>
  <g font-family=\"Courier New, monospace\" font-weight=\"900\" letter-spacing=\"3\"><text x=\"86\" y=\"96\" font-size=\"18\" fill=\"#6f2718\">BUYER DECISION ANNEX / SAMPLE DOSSIER CLOSE</text><text x=\"878\" y=\"96\" font-size=\"15\" fill=\"#8e2a21\">INTERNAL FORWARD PACK</text></g>
  <text x=\"86\" y=\"150\" font-family=\"Georgia, serif\" font-size=\"54\" font-weight=\"900\" letter-spacing=\"-2\" fill=\"#221d17\">Three pages that make the first sale obvious.</text>
  <g transform=\"translate(96 208)\" filter=\"url(#annexShadow)\" font-family=\"Aptos, Segoe UI, sans-serif\" fill=\"#221d17\">
    <g transform=\"rotate(-2.8)\"><rect width=\"300\" height=\"358\" fill=\"#f4ead8\" stroke=\"#cdbb9d\"/><rect width=\"300\" height=\"54\" fill=\"#221d17\"/><text x=\"22\" y=\"35\" font-family=\"Courier New, monospace\" font-size=\"15\" font-weight=\"900\" fill=\"#fbf6ea\">01 / SHORTLIST</text><text x=\"22\" y=\"100\" font-family=\"Georgia, serif\" font-size=\"44\" font-weight=\"900\" fill=\"#221d17\">7 viable pursuits</text><path d=\"M24 146H264M24 188H226M24 230H250\" stroke=\"#2b2118\" stroke-width=\"8\" stroke-opacity=\".3\"/><rect x=\"24\" y=\"276\" width=\"108\" height=\"38\" fill=\"#29563d\"/><text x=\"42\" y=\"301\" font-family=\"Courier New, monospace\" font-size=\"15\" font-weight=\"900\" fill=\"#fff\">PURSUE</text></g>
    <g transform=\"translate(336 -18) rotate(1.6)\"><rect width=\"318\" height=\"398\" fill=\"#fbf6ea\" stroke=\"#2b2118\" stroke-opacity=\".32\"/><rect width=\"318\" height=\"54\" fill=\"#8e2a21\"/><text x=\"22\" y=\"35\" font-family=\"Courier New, monospace\" font-size=\"15\" font-weight=\"900\" fill=\"#fff\">02 / KILL REASONS</text><g font-size=\"18\" font-weight=\"850\"><text x=\"26\" y=\"104\">× incumbent-shaped framework</text><text x=\"26\" y=\"154\">× mandatory ISO evidence gap</text><text x=\"26\" y=\"204\">× lot size exceeds capacity</text><text x=\"26\" y=\"254\">? clarification before spend</text></g><circle cx=\"240\" cy=\"328\" r=\"48\" fill=\"none\" stroke=\"#8e2a21\" stroke-width=\"5\"/><text x=\"210\" y=\"335\" font-family=\"Courier New, monospace\" font-size=\"17\" font-weight=\"900\" fill=\"#8e2a21\">NO-BID</text></g>
    <g transform=\"translate(708 26) rotate(3.2)\"><rect width=\"300\" height=\"358\" fill=\"#f4ead8\" stroke=\"#cdbb9d\"/><rect width=\"300\" height=\"54\" fill=\"#29563d\"/><text x=\"22\" y=\"35\" font-family=\"Courier New, monospace\" font-size=\"15\" font-weight=\"900\" fill=\"#fff\">03 / STARTER TRIGGER</text><text x=\"22\" y=\"104\" font-family=\"Georgia, serif\" font-size=\"54\" font-weight=\"900\" fill=\"#29563d\">£250+</text><text x=\"22\" y=\"144\" font-size=\"19\" font-weight=\"850\">when a notice survives</text><path d=\"M24 196H264M24 238H232M24 280H246\" stroke=\"#2b2118\" stroke-width=\"8\" stroke-opacity=\".3\"/><rect x=\"24\" y=\"306\" width=\"160\" height=\"32\" fill=\"#221d17\"/><text x=\"36\" y=\"328\" font-family=\"Courier New, monospace\" font-size=\"14\" font-weight=\"900\" fill=\"#fbf6ea\">REQUEST PACK</text></g>
  </g>
  <g stroke=\"#b94d24\" stroke-width=\"5\" stroke-linecap=\"round\" stroke-dasharray=\"12 12\" fill=\"none\"><path d=\"M378 388C408 388 402 388 432 388\"/><path d=\"M750 388C782 388 774 388 804 388\"/></g>
  <text x=\"86\" y=\"632\" font-family=\"Courier New, monospace\" font-size=\"16\" font-weight=\"900\" letter-spacing=\"2\" fill=\"#6e6254\">SAMPLE DOSSIER → FORWARDABLE DECISION PACK → NATURAL BID-STARTER ESCALATION</text>
</svg>"""

for name, svg in {
    "bid-no-bid-scorecard.svg": """<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1180 720\" role=\"img\" aria-labelledby=\"title desc\">
  <title id=\"title\">Bid no-bid scorecard</title>
  <desc id=\"desc\">A procurement dossier scorecard showing a tender opportunity scored across buyer fit, evidence readiness, margin, delivery risk and deadline pressure before a pursue or no-bid recommendation.</desc>
  <defs>
    <filter id=\"scoreShadow\" x=\"-18%\" y=\"-18%\" width=\"136%\" height=\"145%\"><feDropShadow dx=\"0\" dy=\"24\" stdDeviation=\"18\" flood-color=\"#2b2118\" flood-opacity=\"0.25\"/></filter>
    <pattern id=\"scoreGrid\" width=\"44\" height=\"44\" patternUnits=\"userSpaceOnUse\"><path d=\"M44 0H0v44\" fill=\"none\" stroke=\"#2b2118\" stroke-opacity=\"0.055\"/></pattern>
  </defs>
  <rect width=\"1180\" height=\"720\" rx=\"26\" fill=\"#efe6d2\"/><rect width=\"1180\" height=\"720\" rx=\"26\" fill=\"url(#scoreGrid)\"/>
  <rect x=\"54\" y=\"46\" width=\"1072\" height=\"628\" rx=\"14\" fill=\"#fbf6ea\" stroke=\"#2b2118\" stroke-opacity=\"0.28\" filter=\"url(#scoreShadow)\"/>
  <g font-family=\"Courier New, monospace\" font-weight=\"900\" letter-spacing=\"3\"><text x=\"86\" y=\"96\" font-size=\"18\" fill=\"#6f2718\">GO / NO-GO SCORECARD</text><text x=\"848\" y=\"96\" font-size=\"15\" fill=\"#8e2a21\">SUPPLIER DECISION GATE</text></g>
  <text x=\"86\" y=\"150\" font-family=\"Georgia, serif\" font-size=\"54\" font-weight=\"900\" letter-spacing=\"-2\" fill=\"#221d17\">Every tender gets a reasoned call before writing starts.</text>
  <g transform=\"translate(86 205)\" font-family=\"Aptos, Segoe UI, sans-serif\" fill=\"#221d17\">
    <rect width=\"660\" height=\"360\" fill=\"#f4ead8\" stroke=\"#cdbb9d\"/>
    <rect width=\"660\" height=\"54\" fill=\"#221d17\"/><text x=\"24\" y=\"35\" font-family=\"Courier New, monospace\" font-size=\"15\" font-weight=\"900\" fill=\"#fbf6ea\">SCORE DIMENSION</text><text x=\"430\" y=\"35\" font-family=\"Courier New, monospace\" font-size=\"15\" font-weight=\"900\" fill=\"#fbf6ea\">RATING</text>
    <g font-size=\"18\" font-weight=\"850\">
      <g transform=\"translate(0 74)\"><rect width=\"660\" height=\"48\" fill=\"#fbf6ea\"/><text x=\"24\" y=\"31\">Buyer and sector fit</text><rect x=\"360\" y=\"14\" width=\"238\" height=\"18\" fill=\"#d8c9ad\"/><rect x=\"360\" y=\"14\" width=\"202\" height=\"18\" fill=\"#29563d\"/><text x=\"612\" y=\"31\" text-anchor=\"end\" font-family=\"Courier New, monospace\" font-size=\"14\" font-weight=\"900\" fill=\"#29563d\">86</text></g>
      <g transform=\"translate(0 132)\"><rect width=\"660\" height=\"48\" fill=\"#f4ead8\"/><text x=\"24\" y=\"31\">Evidence already on file</text><rect x=\"360\" y=\"14\" width=\"238\" height=\"18\" fill=\"#d8c9ad\"/><rect x=\"360\" y=\"14\" width=\"150\" height=\"18\" fill=\"#a96e1f\"/><text x=\"612\" y=\"31\" text-anchor=\"end\" font-family=\"Courier New, monospace\" font-size=\"14\" font-weight=\"900\" fill=\"#a96e1f\">63</text></g>
      <g transform=\"translate(0 190)\"><rect width=\"660\" height=\"48\" fill=\"#fbf6ea\"/><text x=\"24\" y=\"31\">Delivery risk and capacity</text><rect x=\"360\" y=\"14\" width=\"238\" height=\"18\" fill=\"#d8c9ad\"/><rect x=\"360\" y=\"14\" width=\"112\" height=\"18\" fill=\"#8e2a21\"/><text x=\"612\" y=\"31\" text-anchor=\"end\" font-family=\"Courier New, monospace\" font-size=\"14\" font-weight=\"900\" fill=\"#8e2a21\">47</text></g>
      <g transform=\"translate(0 248)\"><rect width=\"660\" height=\"48\" fill=\"#f4ead8\"/><text x=\"24\" y=\"31\">Margin and strategic value</text><rect x=\"360\" y=\"14\" width=\"238\" height=\"18\" fill=\"#d8c9ad\"/><rect x=\"360\" y=\"14\" width=\"178\" height=\"18\" fill=\"#29563d\"/><text x=\"612\" y=\"31\" text-anchor=\"end\" font-family=\"Courier New, monospace\" font-size=\"14\" font-weight=\"900\" fill=\"#29563d\">75</text></g>
    </g>
  </g>
  <g transform=\"translate(800 214)\" filter=\"url(#scoreShadow)\">
    <rect width=\"250\" height=\"288\" fill=\"#221d17\"/><rect x=\"18\" y=\"18\" width=\"214\" height=\"252\" fill=\"none\" stroke=\"#efe6d2\" stroke-opacity=\".25\"/>
    <text x=\"36\" y=\"66\" font-family=\"Courier New, monospace\" font-size=\"14\" font-weight=\"900\" fill=\"#d8c9ad\">DECISION</text>
    <text x=\"36\" y=\"140\" font-family=\"Georgia, serif\" font-size=\"64\" font-weight=\"900\" fill=\"#ddb36b\">PARK</text>
    <text x=\"36\" y=\"184\" font-family=\"Aptos, Segoe UI, sans-serif\" font-size=\"18\" font-weight=\"850\" fill=\"#fbf6ea\">Clarify capacity and evidence gap before paid bid-starter work.</text>
    <rect x=\"36\" y=\"226\" width=\"154\" height=\"32\" fill=\"#a96e1f\"/><text x=\"50\" y=\"247\" font-family=\"Courier New, monospace\" font-size=\"13\" font-weight=\"900\" fill=\"#fff\">48H REVIEW</text>
  </g>
  <g transform=\"translate(848 538) rotate(-8)\" font-family=\"Courier New, monospace\" text-anchor=\"middle\" font-weight=\"900\"><circle cx=\"105\" cy=\"54\" r=\"54\" fill=\"none\" stroke=\"#8e2a21\" stroke-width=\"5\"/><text x=\"105\" y=\"48\" fill=\"#8e2a21\" font-size=\"15\">NO BLIND</text><text x=\"105\" y=\"72\" fill=\"#8e2a21\" font-size=\"19\">BIDS</text></g>
  <text x=\"86\" y=\"632\" font-family=\"Courier New, monospace\" font-size=\"16\" font-weight=\"900\" letter-spacing=\"2\" fill=\"#6e6254\">FIT + EVIDENCE + RISK + MARGIN → PURSUE, PARK OR KILL WITH A WRITTEN REASON.</text>
</svg>""",
    "buyer-decision-annex.svg": buyer_decision_annex,
    "tender-triage-board.svg": triage_board,
    "pursuit-file-stack.svg": pursuit_file,
    "deadline-corridor.svg": deadline_corridor,
    "tender-economics-ledger.svg": economics_ledger,
    "evidence-burden-matrix.svg": evidence_matrix,
    "weekly-procurement-clock.svg": """<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1120 680\" role=\"img\" aria-labelledby=\"title desc\">
  <title id=\"title\">Weekly procurement operating clock</title>
  <desc id=\"desc\">A premium procurement intelligence visual showing Monday feed capture, Wednesday scoring and Friday pursue, park or ignore dossier delivery.</desc>
  <defs>
    <filter id=\"paperShadow\" x=\"-15%\" y=\"-15%\" width=\"130%\" height=\"145%\"><feDropShadow dx=\"0\" dy=\"22\" stdDeviation=\"18\" flood-color=\"#2b2118\" flood-opacity=\"0.25\"/></filter>
    <pattern id=\"minuteGrid\" width=\"40\" height=\"40\" patternUnits=\"userSpaceOnUse\"><path d=\"M40 0H0v40\" fill=\"none\" stroke=\"#2b2118\" stroke-opacity=\"0.06\"/></pattern>
  </defs>
  <rect width=\"1120\" height=\"680\" rx=\"26\" fill=\"#efe6d2\"/>
  <rect width=\"1120\" height=\"680\" rx=\"26\" fill=\"url(#minuteGrid)\"/>
  <rect x=\"48\" y=\"42\" width=\"1024\" height=\"596\" rx=\"16\" fill=\"#fbf6ea\" stroke=\"#2b2118\" stroke-opacity=\"0.24\" filter=\"url(#paperShadow)\"/>
  <text x=\"82\" y=\"90\" font-family=\"Courier New, monospace\" font-size=\"18\" font-weight=\"900\" letter-spacing=\"4\" fill=\"#6f2718\">WEEKLY PROCUREMENT OPERATING CLOCK</text>
  <text x=\"82\" y=\"138\" font-family=\"Georgia, serif\" font-size=\"50\" font-weight=\"900\" letter-spacing=\"-2\" fill=\"#221d17\">A fixed rhythm beats portal panic.</text>
  <g transform=\"translate(136 186)\">
    <circle cx=\"250\" cy=\"250\" r=\"214\" fill=\"#f4ead8\" stroke=\"#2b2118\" stroke-opacity=\"0.32\" stroke-width=\"3\"/>
    <circle cx=\"250\" cy=\"250\" r=\"168\" fill=\"none\" stroke=\"#cdbb9d\" stroke-width=\"2\" stroke-dasharray=\"8 10\"/>
    <circle cx=\"250\" cy=\"250\" r=\"12\" fill=\"#221d17\"/>
    <g stroke=\"#221d17\" stroke-width=\"4\" stroke-linecap=\"round\" opacity=\"0.75\">
      <path d=\"M250 250L250 92\"/>
      <path d=\"M250 250L386 328\"/>
      <path d=\"M250 250L126 356\"/>
    </g>
    <g font-family=\"Courier New, monospace\" font-weight=\"900\" text-anchor=\"middle\">
      <g transform=\"translate(250 52)\"><rect x=\"-76\" y=\"-24\" width=\"152\" height=\"48\" rx=\"2\" fill=\"#221d17\"/><text y=\"6\" font-size=\"16\" fill=\"#fbf6ea\">MON / SCAN</text></g>
      <g transform=\"translate(446 363)\"><rect x=\"-92\" y=\"-24\" width=\"184\" height=\"48\" rx=\"2\" fill=\"#a96e1f\"/><text y=\"6\" font-size=\"16\" fill=\"#fff\">WED / SCORE</text></g>
      <g transform=\"translate(68 390)\"><rect x=\"-88\" y=\"-24\" width=\"176\" height=\"48\" rx=\"2\" fill=\"#29563d\"/><text y=\"6\" font-size=\"16\" fill=\"#fff\">FRI / FILE</text></g>
    </g>
    <g fill=\"none\" stroke=\"#b94d24\" stroke-width=\"10\" stroke-linecap=\"round\"><path d=\"M250 36A214 214 0 0 1 446 363\"/><path d=\"M446 363A214 214 0 0 1 68 390\" opacity=\"0.75\"/><path d=\"M68 390A214 214 0 0 1 250 36\" opacity=\"0.5\"/></g>
  </g>
  <g transform=\"translate(650 196)\" font-family=\"Aptos, Segoe UI, sans-serif\" fill=\"#221d17\">
    <g transform=\"rotate(-1)\"><rect width=\"346\" height=\"96\" fill=\"#f4ead8\" stroke=\"#cdbb9d\"/><rect width=\"12\" height=\"96\" fill=\"#221d17\"/><text x=\"28\" y=\"34\" font-family=\"Georgia, serif\" font-size=\"26\" font-weight=\"900\">Feed intake</text><text x=\"28\" y=\"64\" font-size=\"16\" font-weight=\"800\" fill=\"#6e6254\">Find a Tender + Contracts Finder sweep</text></g>
    <g transform=\"translate(22 132) rotate(1.2)\"><rect width=\"346\" height=\"96\" fill=\"#fbf6ea\" stroke=\"#cdbb9d\"/><rect width=\"12\" height=\"96\" fill=\"#a96e1f\"/><text x=\"28\" y=\"34\" font-family=\"Georgia, serif\" font-size=\"26\" font-weight=\"900\">Score & clarify</text><text x=\"28\" y=\"64\" font-size=\"16\" font-weight=\"800\" fill=\"#6e6254\">fit, evidence drag, deadline pressure</text></g>
    <g transform=\"translate(-8 264) rotate(-.8)\"><rect width=\"346\" height=\"112\" fill=\"#221d17\"/><rect width=\"12\" height=\"112\" fill=\"#29563d\"/><text x=\"28\" y=\"38\" font-family=\"Georgia, serif\" font-size=\"28\" font-weight=\"900\" fill=\"#fbf6ea\">Decision dossier</text><text x=\"28\" y=\"70\" font-size=\"16\" font-weight=\"800\" fill=\"#d8c9ad\">pursue / park / ignore plus next moves</text><text x=\"28\" y=\"96\" font-family=\"Courier New, monospace\" font-size=\"14\" font-weight=\"900\" fill=\"#7db58d\">OPTIONAL: BID-STARTER FILE</text></g>
  </g>
  <text x=\"82\" y=\"600\" font-family=\"Courier New, monospace\" font-size=\"16\" font-weight=\"900\" letter-spacing=\"2\" fill=\"#6e6254\">REPEATABLE RHYTHM → LOWER DECISION FRICTION → CLEAR WEEKLY REASON TO STAY SUBSCRIBED</text>
</svg>""",
}.items():
    path = OUT / name
    path.write_text(svg, encoding="utf-8")
    print(path)

award_route_map = """<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1180 720\" role=\"img\" aria-labelledby=\"title desc\">
  <title id=\"title\">Tender award route map</title>
  <desc id=\"desc\">An official procurement route-to-award map showing buyer route, evaluation weighting, evidence readiness and next actions for shortlisted tenders.</desc>
  <defs>
    <filter id=\"routeShadow\" x=\"-16%\" y=\"-16%\" width=\"132%\" height=\"142%\"><feDropShadow dx=\"0\" dy=\"24\" stdDeviation=\"18\" flood-color=\"#2b2118\" flood-opacity=\"0.24\"/></filter>
    <pattern id=\"routeGrid\" width=\"48\" height=\"42\" patternUnits=\"userSpaceOnUse\"><path d=\"M0 42H48M48 0V42\" fill=\"none\" stroke=\"#2b2118\" stroke-opacity=\"0.06\"/></pattern>
  </defs>
  <rect width=\"1180\" height=\"720\" rx=\"26\" fill=\"#efe6d2\"/><rect width=\"1180\" height=\"720\" rx=\"26\" fill=\"url(#routeGrid)\"/>
  <rect x=\"54\" y=\"46\" width=\"1072\" height=\"628\" rx=\"14\" fill=\"#fbf6ea\" stroke=\"#2b2118\" stroke-opacity=\"0.27\" filter=\"url(#routeShadow)\"/>
  <text x=\"86\" y=\"96\" font-family=\"Courier New, monospace\" font-size=\"18\" font-weight=\"900\" letter-spacing=\"4\" fill=\"#6f2718\">AWARD ROUTE MAP / PROCUREMENT ROUTE-TO-WIN</text>
  <text x=\"86\" y=\"150\" font-family=\"Georgia, serif\" font-size=\"54\" font-weight=\"900\" letter-spacing=\"-2\" fill=\"#221d17\">Can this notice become a winnable bid?</text>
  <g transform=\"translate(94 206)\" font-family=\"Aptos, Segoe UI, sans-serif\" fill=\"#221d17\">
    <rect width=\"992\" height=\"64\" fill=\"#221d17\"/><g fill=\"#fbf6ea\" font-family=\"Courier New, monospace\" font-size=\"15\" font-weight=\"900\"><text x=\"24\" y=\"40\">NOTICE</text><text x=\"300\" y=\"40\">BUYER ROUTE</text><text x=\"518\" y=\"40\">WEIGHTING</text><text x=\"704\" y=\"40\">PROOF STATUS</text><text x=\"874\" y=\"40\">ACTION</text></g>
    <g font-size=\"18\" font-weight=\"830\">
      <g transform=\"translate(0 86)\"><rect width=\"992\" height=\"78\" fill=\"#f4ead8\" stroke=\"#cdbb9d\"/><rect width=\"12\" height=\"78\" fill=\"#29563d\"/><text x=\"26\" y=\"34\" font-family=\"Georgia, serif\" font-size=\"23\" font-weight=\"900\">Facilities framework</text><text x=\"26\" y=\"58\" fill=\"#6e6254\" font-size=\"15\">SME-friendly lot</text><text x=\"300\" y=\"48\">Open call-off</text><text x=\"518\" y=\"48\">Quality 70%</text><text x=\"704\" y=\"48\">2 case studies ready</text><text x=\"874\" y=\"48\" fill=\"#29563d\" font-family=\"Courier New, monospace\" font-weight=\"900\">PURSUE</text></g>
      <g transform=\"translate(0 184)\"><rect width=\"992\" height=\"78\" fill=\"#fbf6ea\" stroke=\"#cdbb9d\"/><rect width=\"12\" height=\"78\" fill=\"#a96e1f\"/><text x=\"26\" y=\"34\" font-family=\"Georgia, serif\" font-size=\"23\" font-weight=\"900\">Retrofit support</text><text x=\"26\" y=\"58\" fill=\"#6e6254\" font-size=\"15\">scope unclear</text><text x=\"300\" y=\"48\">Clarification window</text><text x=\"518\" y=\"48\">Method 45%</text><text x=\"704\" y=\"48\">policy dates missing</text><text x=\"874\" y=\"48\" fill=\"#a96e1f\" font-family=\"Courier New, monospace\" font-weight=\"900\">ASK</text></g>
      <g transform=\"translate(0 282)\"><rect width=\"992\" height=\"78\" fill=\"#f4ead8\" stroke=\"#cdbb9d\"/><rect width=\"12\" height=\"78\" fill=\"#8e2a21\"/><text x=\"26\" y=\"34\" font-family=\"Georgia, serif\" font-size=\"23\" font-weight=\"900\">National multi-lot</text><text x=\"26\" y=\"58\" fill=\"#6e6254\" font-size=\"15\">incumbent shaped</text><text x=\"300\" y=\"48\">Oversized route</text><text x=\"518\" y=\"48\">Price 60%</text><text x=\"704\" y=\"48\">ISO gap</text><text x=\"874\" y=\"48\" fill=\"#8e2a21\" font-family=\"Courier New, monospace\" font-weight=\"900\">NO-BID</text></g>
    </g>
  </g>
  <g transform=\"translate(806 566) rotate(-7)\" font-family=\"Courier New, monospace\" font-weight=\"900\" text-anchor=\"middle\"><circle cx=\"92\" cy=\"50\" r=\"52\" fill=\"none\" stroke=\"#29563d\" stroke-width=\"5\"/><text x=\"92\" y=\"43\" fill=\"#29563d\" font-size=\"14\">ROUTE</text><text x=\"92\" y=\"68\" fill=\"#29563d\" font-size=\"19\">FILED</text></g>
  <text x=\"86\" y=\"632\" font-family=\"Courier New, monospace\" font-size=\"16\" font-weight=\"900\" letter-spacing=\"2\" fill=\"#6e6254\">BUYER ROUTE → SCORING REALITY → EVIDENCE READINESS → NEXT ACTION NAMED</text>
</svg>"""
award_path = OUT / "award-route-map.svg"
award_path.write_text(award_route_map, encoding="utf-8")
print(award_path)
